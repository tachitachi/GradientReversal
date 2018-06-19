# GradientReversal

Implements the Gradient Reversal layer from Unsupervised Domain Adaptation by Backpropagation (https://arxiv.org/abs/1409.7495) and Domain-Adversarial Training of Neural Networks (https://arxiv.org/abs/1505.07818) in Tensorflow.

The forward pass is the identify function, but the backward pass multiplies the gradients by -lambda.
