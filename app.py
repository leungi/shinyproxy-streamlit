import streamlit as st 

def main():
	"""Deploying Streamlit App In Docker"""

	st.title("Streamlit App")
	st.header("Deploying Streamlit in Docker")


	activities = ["EDA","Plots"]

	choices = st.sidebar.selectbox('Select Activities',activities)

	if choices == 'EDA':
		st.subheader("EDA")

	elif choices == 'Plots':
		st.subheader("Visualization")


if __name__ == '__main__':
	main()