import pandas as pd

# List of survey questions
questions = [
    '1. How happy do you feel on a daily basis (in %)?',
    '2. How often do you feel stressed?',
    '3. Do you feel connected to others in your school community?',
    '4. Do you feel comfortable asking for help with mental health concerns?',
    '5. How often do you engage in physical activity?',
    '6. How often do you engage in activities that bring you joy or fulfillment?',
    '7. How often do you engage in activities that promote relaxation or mindfulness?'
]

# Empty dictionary to store survey responses
survey_data = {}

# Loop through each question and collect responses
for question in questions:
    try:
        response = int(input(question + ' '))

        # Ensure the response is within a valid range
        if 0 <= response <= 100:
            survey_data[question] = response
            
            if response >= 80:
                print("Feeling Happy")
            elif 50 <= response < 80:
                print("Feeling better")
                reason = input("We consider your response. Can you tell us the reason? ")
                survey_data['Reason for feeling better'] = reason
                
                additional_support = input("Do you need any additional support from us (yes/no)? ").lower()
                survey_data['Need additional support'] = additional_support
                
                if additional_support == 'yes':
                    support_needed = input("What kind of help do you need from us? ")
                    survey_data['Support needed'] = support_needed
                    print("We will provide additional support to you.")
                else:
                    print("Proceeding to the next question.")
            else:
                print("Feeling Sad")
                reason = input("What makes you feel sad? ")
                survey_data['Reason for feeling sad'] = reason
                
                additional_support = input("Do you need any additional support from us (yes/no)? ").lower()
                survey_data['Need additional support'] = additional_support
                
                if additional_support == 'yes':
                    support_needed = input("What kind of help do you need from us? ")
                    survey_data['Support needed'] = support_needed
                    print("We will provide additional support to you.")
                else:
                    print("Proceeding to the next question.")
        else:
            print("Please enter a value between 0 and 100.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")

# Convert the survey data to a Pandas DataFrame
survey_df = pd.DataFrame([survey_data])

# Save the survey data to a CSV file
survey_df.to_csv('happiness_index_survey.csv', index=False)

print("Survey data has been saved to 'happiness_index_survey.csv'.")
