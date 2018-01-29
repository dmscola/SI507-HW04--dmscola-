user_question = ""
while(user_question!= "quit"):


	def question():
		print("What is your question?")
		question = input()
		return question

	user_question = question()

	if user_question.endswith("?"):
		pass
	else:
		print("I’m sorry, I can only answer questions.")

