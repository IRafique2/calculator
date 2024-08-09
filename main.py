import streamlit as st

def main():
    st.title("Simple Calculator")

    st.write("Choose an operation:")
    operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    result = None
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero")
        st.write(f"The result is: {result}")

if __name__ == "__main__":
    main()
