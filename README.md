#$ **RNN Loss Gradient Equation** $

The following equation represents the backpropagation step for calculating the loss gradient in a Recurrent Neural Network (RNN):

$$
\frac{\partial L_t}{\partial h_t} = \frac{\partial L_{t+1}}{\partial h_{t+1}} \odot \tanh'(h_t) + \frac{\partial L_t}{\partial o_t} \odot W_o^T \odot \sigma'(z_t)
$$
