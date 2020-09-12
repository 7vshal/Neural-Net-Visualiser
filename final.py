import streamlit as lit
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import random
model=tf.keras.models.load_model('model.h5')
feature_model=tf.keras.models.Model(
    model.inputs,
    [layer.output for layer in model.layers]
)
_, (x_test,_)=tf.keras.datasets.mnist.load_data()
x_test=x_test/255.

def get_prediction():
    index=np.random.choice(x_test.shape[0])
    image=x_test[index,:,:]
    image_arr=np.reshape(image,(1,784))
    return feature_model.predict(image_arr),image

lit.title('Neural Network Visualiser')
lit.sidebar.markdown('## Input image')
if lit.button('Get random prediction'):
    preds,image=get_prediction()
    image=np.reshape(image,(28,28))
    lit.sidebar.image(image,width=150)
    
    for layer,p in enumerate(preds):
        
        numbers=np.squeeze(np.array(p))
        plt.figure(figsize=(32,4))
        if(layer==2):
            row=1
            column=10
        else:
            row=2
            col=16
        for i,number in enumerate(numbers):
            plt.subplot(row,col,i+1)
            plt.imshow(number*np.ones((8,8,3)).astype('float32'))
            plt.xticks([])
            plt.yticks([])
            
            if layer==2:
                plt.xlabel(str(i),fontsize=40)
        plt.subplots_adjust(wspace=0.05,hspace=0.05)
        plt.tight_layout()
        lit.text('Layer {}'.format(layer+1))
        lit.pyplot()

