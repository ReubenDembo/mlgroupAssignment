# core pkgs
import streamlit as st 

# EDA pkgs
import pandas as pd
import numpy as np

# pickle pkg
import pickle

def main():
	pickle_in = open('obessity_classifier.pkl', 'rb')
	classifier = pickle.load(pickle_in)


	st.title('Artificial Intelligence End of Semester Project')
	if st.checkbox('ABOUT'):
		st.header('Tutorial on how to use the Web Application')
		st.write('''
			How to use the web 
			gguit
			''')

		st.header('ABOUT')
		st.write('''
			anything about the app
			''')

	if st.checkbox('Model'):
		st.header('Predicting using trained Model')
		Age = st.number_input('Enter Age',1)
		Weight = st.number_input('Enter Weight',1)
		family_history_with_overweight = st.text_input('family_history_with_overweight','Enter Yes or No')
		FAVC = st.number_input('Enter FAVC',1)
		CAEC = st.number_input('Enter CAEC',1)

		if st.button('Predict'):
			if family_history_with_overweight == 'Yes':
				family_history_with_overweight=1
			else:
				family_history_with_overweight=0

			arr=[[Age, Weight,family_history_with_overweight, FAVC, CAEC]]
			prediction = classifier.predict(arr)

			if prediction == 1:
				st.success('Obesity_Type_I')
				accuracy = classifier.score(arr,prediction)
				st.success('Accuracy is {}'.format(accuracy))

			if prediction == 2:
				st.success('Obesity_Type_III')
				accuracy = classifier.score(arr,prediction)
				st.success('Accuracy is {}'.format(accuracy))

			if prediction == 3:
				st.success('Obesity_Type_II')
				accuracy = classifier.score(arr,prediction)
				st.success('Accuracy is {}'.format(accuracy))

			if prediction == 4:
				st.success('Overweight_Level_I')
				accuracy = classifier.score(arr,prediction)
				st.success('Accuracy is {}'.format(accuracy))

			if prediction == 5:
				st.success('Overweight_Level_II')
				accuracy = classifier.score(arr,prediction)
				st.success('Accuracy is {}'.format(accuracy))

			if prediction == 6:
				st.success('Normal_Weight')
				accuracy = classifier.score(arr,prediction)
				st.success('Accuracy is {}'.format(accuracy))

			if prediction == 7:
				st.success('Insufficient_Weight')
				accuracy = classifier.score(arr,prediction)
				st.success('Accuracy is {}'.format(accuracy))



		
if __name__ == '__main__':
	main()