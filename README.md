


<h1 align='center'> Hack - A - Dog</h1>
<h3 align='center'> Group project created by Kyera Francis, Tanner Zuleeg, Mark Dunlea Tate</h3>
 

## Features

- State-of-the-art Hotdog Identification: Our cutting-edge AI will determine whether that suspicious-looking snack is a hotdog or a culinary decoy.
- Real-time Hotdog Recognition: Snap a pic, upload it, and let the app analyze the hotdog potential. Instant results, no more food identity crises.
- Shazam-like Experience: Like the iconic music identification app, but for hotdogs. Because every meal deserves its own theme song!

## How to Use

1. Click on the "Choose an image" button.
2. Upload a picture of your food item.
3. Wait for the magic to happen as SEEFOOD reveals the hotdog truth.


## Model

- **Convolutional Magic:** Our model uses convolutional layers to capture intricate patterns and features in food images.

- **Pooling Perfection:** Max-pooling layers efficiently downsample the image, focusing on the most essential details and enhancing the model's ability to discern the nuances of a hotdog.

- **Flatten and Decide:** The flattening layer prepares the extracted features for decision-making.

## Dataset Composition

- **Hotdog Images (1500):** A rich assortment of hotdog images captured in different contexts, angles, and presentations.

- **Non-Hotdog Images (1500):** A diverse selection of food images that do not include hotdogs. 


| Layer (type)              | Output Shape          | Param #      |
|---------------------------|-----------------------|--------------|
| conv2d                    | (None, 297, 297, 32)  | 896          |
| max_pooling2d             | (None, 148, 148, 32)  | 0            |
| conv2d_1                  | (None, 146, 146, 64)  | 18,496       |
| max_pooling2d_1           | (None, 73, 73, 64)    | 0            |
| flatten                   | (None, 341056)        | 0            |
| dense                     | (None, 64)            | 21,827,648   |
| dense_1                   | (None, 1)             | 65           |

Total params: 21,847,105
Trainable params: 21,847,105
Non-trainable params: 0



**Disclaimer:** SEEFOOD is not responsible for any existential crises induced by discovering your favorite snack isn't a hotdog.


