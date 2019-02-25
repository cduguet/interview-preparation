


# 7 steps of Machine Learning

1. Gather Data
2. Prepare Data
3. Choose Model
4. Train Model
5. Evaluate Model
6. Hyperparameter Tuning
7. Prediction

# Overfitting

- When the training set is too small and there is no variety 
- When we have too many parameters for such a small training set 

# Vanishing Gradient Problem
It happens when the earlier layers do not converge fast enough, because of too small gradients.

- too many layers
- sigmoid/tanh activation functions 
- too small data training set

Solutions:
- Use RELU
- Use ResNet

## recommendations:
 - Hidden layers with not much dimensionality

# Transfer Learning:
When we want to use an already trained model.  
4 cases: 
 - New Dataset is small and similar: 
    Freeze all VGG19 model layers and train only classifiers (FC layers)
 - New Data set is large and similar:
    train whole model. optionally can freeze the first few layers (edge detection)
 - New Data set is small and different:
    add a few FC layers and output on top and train only these 
 - Big data set and different: 
    Train whole network. Maybe can choose your own. 

