print "You just received two new emails. Theirs subjects reads \"Congratulations, you get the job!\"(1) " \
      "and \"New course : coding procedurally generated levels\"(2). Which email do you want to open?"

email = raw_input("> ")

if email == "1":
    print "You open the first email and see that this crappy company you applied last week want you to be in. They " \
          "liked your cover letter so much that they want to you to start working for them as of tomorrow."
    print "As expected you start working at this new company but there's like 'a little problem' : "
    print "It's the first day and your boss already want you to handle all of the user's requests and to fix the shitty " \
          "systems developed by the other developers of the company. What do you do ?"
    print "1. Do the job"
    print "2. Punch him in the mouth"

    job = raw_input("> ")

    if job == "1":
        i = 2
        while i <= 5 and job != "2":
            if i >= 5:
                print "You're dead."
                i += 1
            else:
                print "It's now day %d and there's way more work than yesterday. What do you do ?" % i
                print "1. Do the job, you're good at it"
                print "2. Shoryuken the shit out of your boss"
                i += 1

                job = raw_input("> ")

        print "You're free now. Go make something you like."

    elif job == "2":
        print "You're free now. Go make something you like."

elif email == "2":
    print "You open the second email. It's a cool course about creating levels procedurally."
    print "You take the course and you're really passionate about what you're learning."
    print "After you finished the course you start a personnal project with what you learned."
    print "You're project is really well received by people and you're earning money doing what you like. Yaaay !"
else:
    print "Either you thinked out of the box or you did random things with the prompt. Good job !"
