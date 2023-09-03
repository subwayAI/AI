import os
import sys
import json

import torch
import torch.nn as nn
from torchvision import transforms, datasets, utils
import matplotlib.pyplot as plt
import numpy as np
import torch.optim as optim
from tqdm import tqdm

from modelbam1 import AlexNet
import os
os.environ['CUDA_VISIBLE_DEVICES'] ='0'

def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("using {} device.".format(device))

    data_transform = {
        "train": transforms.Compose([transforms.RandomResizedCrop(64),
                                     transforms.RandomHorizontalFlip(),
                                     transforms.ToTensor(),
                                     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]),
        "val": transforms.Compose([transforms.Resize((64, 64)),  # cannot 224, must (224, 224)
                                   transforms.ToTensor(),
                                   transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])}

    data_root = os.path.abspath(os.path.join(os.getcwd(), "../.."))  # get data root path
    image_path = os.path.join("../trainkaihedu/")  # flower data set path
    print(image_path)
    assert os.path.exists(image_path), "{} path does not exist.".format(image_path)
    train_dataset = datasets.ImageFolder(root=os.path.join(image_path, "train"),
                                         transform=data_transform["val"])
    train_num = len(train_dataset)
   
    # {'daisy':0, 'dandelion':1, 'roses':2, 'sunflower':3, 'tulips':4}
    flower_list = train_dataset.class_to_idx
    print(flower_list)
    cla_dict = dict((val, key) for key, val in flower_list.items())
    # write dict into json file
    print(cla_dict)
    json_str = json.dumps(cla_dict, indent=4)
    print(json_str)
    with open('class_indices.json', 'w') as json_file:
        json_file.write(json_str)

    batch_size = 32
    nw = min([os.cpu_count(), batch_size if batch_size > 1 else 0, 0])  # number of workers
    print('Using {} dataloader workers every process'.format(nw))

    train_loader = torch.utils.data.DataLoader(train_dataset,
                                               batch_size=batch_size, shuffle=True,
                                               num_workers=nw)

    validate_dataset = datasets.ImageFolder(root=os.path.join(image_path, "san"),
                                            transform=data_transform["val"])
    val_num = len(validate_dataset)
    validate_loader = torch.utils.data.DataLoader(validate_dataset,
                                                  batch_size=32, shuffle=False,
                                                  num_workers=nw)

    print("using {} images for training, {} images for validation.".format(train_num,
                                                                           val_num))
    # test_data_iter = iter(validate_loader)
    # test_image, test_label = test_data_iter.next()
    #
    # def imshow(img):
    #     img = img / 2 + 0.5  # unnormalize
    #     npimg = img.numpy()
    #     plt.imshow(np.transpose(npimg, (1, 2, 0)))
    #     plt.show()
    #
    # print(' '.join('%5s' % cla_dict[test_label[j].item()] for j in range(4)))
    # imshow(utils.make_grid(test_image))

    net = AlexNet(num_classes=3, init_weights=True)

    net.to(device)
    loss_function = nn.CrossEntropyLoss()
    # pata = list(net.parameters())
    optimizer = optim.Adam(net.parameters(), lr=0.0001)

    epochs = 101
    save_path = './AlexNet.pth'
    best_acc = 0.0
    train_steps = len(train_loader)
    for epoch in range(epochs):
        # train
        net.train()
        running_loss = 0.0
        train_bar = tqdm(train_loader, file=sys.stdout)
        for step, data in enumerate(train_bar):
            images, labels = data
            optimizer.zero_grad()
            outputs = net(images.to(device))
            loss = loss_function(outputs, labels.to(device))
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()

            train_bar.desc = "train epoch[{}/{}] loss:{:.3f}".format(epoch + 1,
                                                                     epochs,
                                                                     loss)

        # validate
        net.eval()
        acc = 0.0  # accumulate accurate number / epoch
        with torch.no_grad():
            val_bar = tqdm(validate_loader, file=sys.stdout)
            for val_data in val_bar:
                val_images, val_labels = val_data
                outputs = net(val_images.to(device))
                predict_y = torch.max(outputs, dim=1)[1]
                acc += torch.eq(predict_y, val_labels.to(device)).sum().item()

        val_accurate = acc / val_num
        print('[epoch %d] train_loss: %.3f  val_accuracy: %.3f' %
              (epoch + 1, running_loss / train_steps, val_accurate))

        if val_accurate > best_acc:
            best_acc = val_accurate
            torch.save(net.state_dict(), save_path)

    print('Finished Training')


if __name__ == '__main__':
    main()


'''
0%|████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:01<00:00,  8.07it/s]
[epoch 195] train_loss: 0.457  val_accuracy: 0.810
train epoch[196/201] loss:0.334: 100%|███████████████████████████████████████████████████| 9/9 [00:01<00:00,  5.16it/s]
100%|████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:01<00:00,  8.55it/s]
[epoch 196] train_loss: 0.451  val_accuracy: 0.755
train epoch[197/201] loss:0.265: 100%|███████████████████████████████████████████████████| 9/9 [00:01<00:00,  7.12it/s]
100%|████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:01<00:00,  8.38it/s]
[epoch 197] train_loss: 0.483  val_accuracy: 0.733
train epoch[198/201] loss:0.292: 100%|███████████████████████████████████████████████████| 9/9 [00:01<00:00,  6.79it/s]
100%|████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:01<00:00,  8.00it/s]
[epoch 198] train_loss: 0.540  val_accuracy: 0.755
train epoch[199/201] loss:0.470: 100%|███████████████████████████████████████████████████| 9/9 [00:01<00:00,  5.29it/s]
100%|████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:01<00:00,  8.48it/s]
[epoch 199] train_loss: 0.551  val_accuracy: 0.744
train epoch[200/201] loss:0.382: 100%|███████████████████████████████████████████████████| 9/9 [00:01<00:00,  7.12it/s]
100%|████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:01<00:00,  8.70it/s]
[epoch 200] train_loss: 0.538  val_accuracy: 0.806
train epoch[201/201] loss:0.574: 100%|███████████████████████████████████████████████████| 9/9 [00:01<00:00,  6.85it/s]
100%|████████████████████████████████████████████████████████████████████████████████████| 9/9 [00:01<00:00,  7.60it/s]
[epoch 201] train_loss: 0.470  val_accuracy: 0.824

'''