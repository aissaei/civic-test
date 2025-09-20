import streamlit as st
import random

# --- Civic test questions. Expand this list for more!
QUESTIONS = [
    {
        "question": "What is the supreme law of the land?",
        "choices": [
            "The Constitution", "The President", "The Supreme Court", "The Declaration of Independence"
        ],
        "answer": "The Constitution"
    },
    {
        "question": "What does the Constitution do?",
        "choices": [
            "Sets up the government", "Declares war", "Chooses the President", "Establishes taxes"
        ],
        "answer": "Sets up the government"
    },
    {
        "question": "The idea of self-government is in the first three words of the Constitution. What are these words?",
        "choices": [
            "We the People", "Of the People", "Liberty and Justice", "Justice For All"
        ],
        "answer": "We the People"
    },
    {
        "question": "What is an amendment?",
        "choices": [
            "A change (to the Constitution)", "A tax", "A kind of law", "A treaty"
        ],
        "answer": "A change (to the Constitution)"
    },
    {
        "question": "What do we call the first ten amendments to the Constitution?",
        "choices": [
            "The Bill of Rights", "The Preamble", "The Federalist Papers", "The Articles"
        ],
        "answer": "The Bill of Rights"
    },
    {
        "question": "What is one right or freedom from the First Amendment?",
        "choices": [
            "Speech", "Voting", "Bear arms", "Trial by jury"
        ],
        "answer": "Speech"
    },
    {
        "question": "How many amendments does the Constitution have?",
        "choices": [
            "27", "10", "23", "50"
        ],
        "answer": "27"
    },
    {
        "question": "What did the Declaration of Independence do?",
        "choices": [
            "Declared our independence", "Established the Constitution", "Freed the slaves", "Started the American Revolution"
        ],
        "answer": "Declared our independence"
    },
    {
        "question": "What are two rights in the Declaration of Independence?",
        "choices": [
            "Life and pursuit of happiness", "Speech and press", "Liberty and property", "Work and travel"
        ],
        "answer": "Life and pursuit of happiness"
    },
    {
        "question": "What is freedom of religion?",
        "choices": [
            "Practice any religion, or not practice", "You must go to church", "Follow the government religion", "Worship only on Sundays"
        ],
        "answer": "Practice any religion, or not practice"
    },
    {
        "question": "What is the economic system in the United States?",
        "choices": [
            "Capitalist economy", "Socialist economy", "Monarchy", "Feudalism"
        ],
        "answer": "Capitalist economy"
    },
    {
        "question": "What is the rule of law?",
        "choices": [
            "Everyone must follow the law", "Only leaders obey the law", "Law is optional", "The wealthy make laws"
        ],
        "answer": "Everyone must follow the law"
    },
    {
        "question": "Name one branch or part of the government.",
        "choices": [
            "Congress", "Military", "Police", "School Board"
        ],
        "answer": "Congress"
    },
    {
        "question": "What stops one branch of government from becoming too powerful?",
        "choices": [
            "Checks and balances", "A new election", "Impeachment", "A military"
        ],
        "answer": "Checks and balances"
    },
    {
        "question": "Who is in charge of the executive branch?",
        "choices": [
            "The President", "The Chief Justice", "The Speaker of the House", "The Secretary of State"
        ],
        "answer": "The President"
    },
    {
        "question": "Who makes federal laws?",
        "choices": [
            "Congress", "The Supreme Court", "The President", "State legislatures"
        ],
        "answer": "Congress"
    },
    {
        "question": "What are the two parts of the U.S. Congress?",
        "choices": [
            "The Senate and House", "The President and Vice President", "The Supreme Court and Congress", "Senate and Cabinet"
        ],
        "answer": "The Senate and House"
    },
    {
        "question": "How many U.S. Senators are there?",
        "choices": [
            "100", "50", "435", "200"
        ],
        "answer": "100"
    },
    {
        "question": "We elect a U.S. Senator for how many years?",
        "choices": [
            "6", "4", "2", "8"
        ],
        "answer": "6"
    },
    {
        "question": "Who is one of your state’s U.S. Senators now?*",
        "choices": [
            "Answers will vary", "Joe Biden", "John Roberts", "Nancy Pelosi"
        ],
        "answer": "Answers will vary"
    },
    {
        "question": "The House of Representatives has how many voting members?",
        "choices": [
            "435", "50", "100", "400"
        ],
        "answer": "435"
    },
    {
        "question": "We elect a U.S. Representative for how many years?",
        "choices": [
            "2", "4", "6", "8"
        ],
        "answer": "2"
    },
    {
        "question": "Name your U.S. Representative.",
        "choices": [
            "Answers will vary", "Kamala Harris", "Barack Obama", "Donald Trump"
        ],
        "answer": "Answers will vary"
    },
    {
        "question": "Who does a U.S. Senator represent?",
        "choices": [
            "All people of the state", "Only people of the city", "Congress", "The Cabinet"
        ],
        "answer": "All people of the state"
    },
    {
        "question": "Why do some states have more Representatives than other states?",
        "choices": [
            "State population", "Geographic size", "Date of statehood", "Governor decision"
        ],
        "answer": "State population"
    },
    {
        "question": "We elect a President for how many years?",
        "choices": [
            "4", "2", "6", "8"
        ],
        "answer": "4"
    },
    {
        "question": "In what month do we vote for President?",
        "choices": [
            "November", "January", "July", "September"
        ],
        "answer": "November"
    },
    {
        "question": "What is the name of the President of the United States now?",
        "choices": [
            "Answers will vary", "Joe Biden", "Donald Trump", "Kamala Harris"
        ],
        "answer": "Answers will vary"
    },
    {
        "question": "What is the name of the Vice President of the United States now?",
        "choices": [
            "Answers will vary", "Joe Biden", "Kevin McCarthy", "Nancy Pelosi"
        ],
        "answer": "Answers will vary"
    },
    {
        "question": "If the President can no longer serve, who becomes President?",
        "choices": [
            "The Vice President", "The Chief Justice", "The Speaker", "The Secretary of State"
        ],
        "answer": "The Vice President"
    },
    {
        "question": "If both the President and the Vice President can no longer serve, who becomes President?",
        "choices": [
            "The Speaker of the House", "The Secretary of State", "The Chief Justice", "The Senate Majority Leader"
        ],
        "answer": "The Speaker of the House"
    },
    {
        "question": "Who is the Commander in Chief of the military?",
        "choices": [
            "The President", "The Vice President", "The Secretary of Defense", "The Attorney General"
        ],
        "answer": "The President"
    },
    {
        "question": "Who signs bills to become laws?",
        "choices": [
            "The President", "The Chief Justice", "The Speaker of the House", "The Vice President"
        ],
        "answer": "The President"
    },
    {
        "question": "Who vetoes bills?",
        "choices": [
            "The President", "The Supreme Court", "Congress", "The Secretary of State"
        ],
        "answer": "The President"
    },
    {
        "question": "What does the President's Cabinet do?",
        "choices": [
            "Advises the President", "Leads Congress", "Interprets laws", "Elects the President"
        ],
        "answer": "Advises the President"
    },
    {
        "question": "What are two Cabinet-level positions?",
        "choices": [
            "Secretary of State and Secretary of Education", "Chief Justice and Speaker", "Senator and Mayor", "Ambassador and Judge"
        ],
        "answer": "Secretary of State and Secretary of Education"
    },
    {
        "question": "What does the judicial branch do?",
        "choices": [
            "Interprets laws", "Makes laws", "Enforces laws", "Sets budgets"
        ],
        "answer": "Interprets laws"
    },
    {
        "question": "What is the highest court in the United States?",
        "choices": [
            "The Supreme Court", "The District Court", "The Court of Appeals", "The State Court"
        ],
        "answer": "The Supreme Court"
    },
    {
        "question": "How many justices are on the Supreme Court?",
        "choices": [
            "9", "12", "7", "8"
        ],
        "answer": "9"
    },
    {
        "question": "Who is the Chief Justice of the United States now?",
        "choices": [
            "Answers will vary", "John Roberts", "Sonia Sotomayor", "Clarence Thomas"
        ],
        "answer": "Answers will vary"
    },
    {
        "question": "Under our Constitution, some powers belong to the federal government. What is one power of the federal government?",
        "choices": [
            "To print money", "Provide schooling", "Set speed limits", "Issue driver's licenses"
        ],
        "answer": "To print money"
    },
    {
        "question": "Under our Constitution, some powers belong to the states. What is one power of the states?",
        "choices": [
            "Provide schooling and education", "Print money", "Maintain an army", "Sign treaties"
        ],
        "answer": "Provide schooling and education"
    },
    {
        "question": "Who is the Governor of your state now?",
        "choices": [
            "Answers will vary", "Joe Biden", "Kamala Harris", "Nancy Pelosi"
        ],
        "answer": "Answers will vary"
    },
    {
        "question": "What is the capital of your state?",
        "choices": [
            "Answers will vary", "Washington, D.C.", "New York City", "Los Angeles"
        ],
        "answer": "Answers will vary"
    },
    {
        "question": "What are the two major political parties in the United States?",
        "choices": [
            "Democratic and Republican", "Democratic and Socialist", "Libertarian and Green", "Tea and Green"
        ],
        "answer": "Democratic and Republican"
    },
    {
        "question": "What is the political party of the President now?",
        "choices": [
            "Answers will vary", "Democratic", "Republican", "Green"
        ],
        "answer": "Answers will vary"
    },
    {
        "question": "What is the name of the Speaker of the House of Representatives now?",
        "choices": [
            "Answers will vary", "Nancy Pelosi", "Kevin McCarthy", "Chuck Schumer"
        ],
        "answer": "Answers will vary"
    },
    {
        "question": "There are four amendments to the Constitution about who can vote. Describe one.",
        "choices": [
            "Citizens 18 and older can vote", "Only men can vote", "You must own property to vote", "Only taxpayers can vote"
        ],
        "answer": "Citizens 18 and older can vote"
    },
    {
        "question": "What is one responsibility that is only for United States citizens?",
        "choices": [
            "Serve on a jury", "Pay taxes", "Obey the law", "Attend school"
        ],
        "answer": "Serve on a jury"
    },
    {
        "question": "Name one right only for United States citizens.",
        "choices": [
            "Vote in a federal election", "Work in the U.S.", "Own property", "Freedom of speech"
        ],
        "answer": "Vote in a federal election"
    },
    {
        "question": "What are two rights of everyone living in the United States?",
        "choices": [
            "Freedom of speech and freedom of religion", "The right to vote and own land", "Healthcare and housing", "The right to travel and marry"
        ],
        "answer": "Freedom of speech and freedom of religion"
    },
    {
        "question": "What do we show loyalty to when we say the Pledge of Allegiance?",
        "choices": [
            "The United States", "The President", "The government", "The Constitution"
        ],
        "answer": "The United States"
    },
    {
        "question": "What is one promise you make when you become a United States citizen?",
        "choices": [
            "Obey the laws of the United States", "Speak only English", "Work for the federal government", "Own a home"
        ],
        "answer": "Obey the laws of the United States"
    },
    {
        "question": "How old do citizens have to be to vote for President?",
        "choices": [
            "18 and older", "16 and older", "21 and older", "25 and older"
        ],
        "answer": "18 and older"
    },
    {
        "question": "What are two ways that Americans can participate in their democracy?",
        "choices": [
            "Vote and join a civic group", "Join the military and pay taxes", "Own a business and pay taxes", "Travel and work"
        ],
        "answer": "Vote and join a civic group"
    },
    {
        "question": "When is the last day you can send in federal income tax forms?",
        "choices": [
            "April 15", "January 1", "December 31", "July 4"
        ],
        "answer": "April 15"
    },
    {
        "question": "When must all men register for the Selective Service?",
        "choices": [
            "Between 18 and 26", "Between 16 and 18", "At age 17", "At age 21"
        ],
        "answer": "Between 18 and 26"
    },
    {
        "question": "What is one reason colonists came to America?",
        "choices": [
            "Freedom", "To escape taxes", "To build railroads", "To buy land"
        ],
        "answer": "Freedom"
    },
    {
        "question": "Who lived in America before the Europeans arrived?",
        "choices": [
            "Native Americans", "Africans", "Spanish", "Asians"
        ],
        "answer": "Native Americans"
    },
    {
        "question": "What group of people was taken to America and sold as slaves?",
        "choices": [
            "Africans", "Europeans", "Asians", "Native Americans"
        ],
        "answer": "Africans"
    },
    {
        "question": "Why did the colonists fight the British?",
        "choices": [
            "Because of high taxes", "For land", "To end slavery", "Over language"
        ],
        "answer": "Because of high taxes"
    },
    {
        "question": "Who wrote the Declaration of Independence?",
        "choices": [
            "Thomas Jefferson", "George Washington", "Abraham Lincoln", "James Madison"
        ],
        "answer": "Thomas Jefferson"
    },
    {
        "question": "When was the Declaration of Independence adopted?",
        "choices": [
            "July 4, 1776", "July 4, 1789", "July 4, 1800", "December 7, 1941"
        ],
        "answer": "July 4, 1776"
    },
    {
        "question": "There were 13 original states. Name three.",
        "choices": [
            "New York, Virginia, Georgia", "Texas, Nevada, Florida", "Ohio, California, Illinois", "Hawaii, Oregon, Utah"
        ],
        "answer": "New York, Virginia, Georgia"
    },
    {
        "question": "What happened at the Constitutional Convention?",
        "choices": [
            "The Constitution was written", "The Declaration of Independence was signed", "The Civil War started", "The Louisiana Purchase was made"
        ],
        "answer": "The Constitution was written"
    },
    {
        "question": "When was the Constitution written?",
        "choices": [
            "1787", "1776", "1800", "1861"
        ],
        "answer": "1787"
    },
    {
        "question": "The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers.",
        "choices": [
            "James Madison", "John F. Kennedy", "Thomas Jefferson", "George Bush"
        ],
        "answer": "James Madison"
    },
    {
        "question": "What is one thing Benjamin Franklin is famous for?",
        "choices": [
            "U.S. diplomat", "President", "Writing the Federalist Papers", "Inventing the telegraph"
        ],
        "answer": "U.S. diplomat"
    },
    {
        "question": "Who is the 'Father of Our Country'?",
        "choices": [
            "George Washington", "Abraham Lincoln", "Thomas Jefferson", "Alexander Hamilton"
        ],
        "answer": "George Washington"
    },
    {
        "question": "Who was the first President?",
        "choices": [
            "George Washington", "John Adams", "Abraham Lincoln", "Andrew Jackson"
        ],
        "answer": "George Washington"
    },
    {
        "question": "What territory did the United States buy from France in 1803?",
        "choices": [
            "Louisiana", "Florida", "Alaska", "Hawaii"
        ],
        "answer": "Louisiana"
    },
    {
        "question": "Name one war fought by the United States in the 1800s.",
        "choices": [
            "Civil War", "World War I", "Korean War", "Vietnam War"
        ],
        "answer": "Civil War"
    },
    {
        "question": "Name the U.S. war between the North and the South.",
        "choices": [
            "The Civil War", "Revolutionary War", "World War II", "Spanish-American War"
        ],
        "answer": "The Civil War"
    },
    {
        "question": "Name one problem that led to the Civil War.",
        "choices": [
            "Slavery", "Prohibition", "Taxes", "Women's suffrage"
        ],
        "answer": "Slavery"
    },
    {
        "question": "What was one important thing Abraham Lincoln did?",
        "choices": [
            "Freed the slaves", "Defeated the British", "Started the New Deal", "Suffrage for women"
        ],
        "answer": "Freed the slaves"
    },
    {
        "question": "What did the Emancipation Proclamation do?",
        "choices": [
            "Freed the slaves", "Freed the colonists", "Ended Prohibition", "Started the Civil War"
        ],
        "answer": "Freed the slaves"
    },
    {
        "question": "What did Susan B. Anthony do?",
        "choices": [
            "Fought for women's rights", "Fought for civil rights", "Ended slavery", "Was First Lady"
        ],
        "answer": "Fought for women's rights"
    },
    {
        "question": "Name one war fought by the United States in the 1900s.",
        "choices": [
            "World War I", "French and Indian War", "Mexican-American War", "Spanish-American War"
        ],
        "answer": "World War I"
    },
    {
        "question": "Who was President during World War I?",
        "choices": [
            "Woodrow Wilson", "Franklin Roosevelt", "Harry Truman", "Dwight Eisenhower"
        ],
        "answer": "Woodrow Wilson"
    },
    {
        "question": "Who was President during the Great Depression and World War II?",
        "choices": [
            "Franklin Roosevelt", "Abraham Lincoln", "John F. Kennedy", "Calvin Coolidge"
        ],
        "answer": "Franklin Roosevelt"
    },
    {
        "question": "Who did the United States fight in World War II?",
        "choices": [
            "Japan, Germany, and Italy", "England, France, and Russia", "China, Korea, and Vietnam", "Spain, Portugal, and Brazil"
        ],
        "answer": "Japan, Germany, and Italy"
    },
    {
        "question": "Before he was President, Eisenhower was a general. What war was he in?",
        "choices": [
            "World War II", "Vietnam War", "Civil War", "Korean War"
        ],
        "answer": "World War II"
    },
    {
        "question": "During the Cold War, what was the main concern of the United States?",
        "choices": [
            "Communism", "Nazism", "Colonialism", "Fascism"
        ],
        "answer": "Communism"
    },
    {
        "question": "What movement tried to end racial discrimination?",
        "choices": [
            "Civil rights movement", "Labor movement", "Peace movement", "Women's movement"
        ],
        "answer": "Civil rights movement"
    },
    {
        "question": "What did Martin Luther King, Jr. do?",
        "choices": [
            "Fought for civil rights", "Was President", "Discovered America", "Wrote the Constitution"
        ],
        "answer": "Fought for civil rights"
    },
    {
        "question": "What major event happened on September 11, 2001, in the United States?",
        "choices": [
            "Terrorists attacked the United States", "Earthquake in California", "Moon landing", "Stock market crash"
        ],
        "answer": "Terrorists attacked the United States"
    },
    {
        "question": "Name one American Indian tribe in the United States.",
        "choices": [
            "Cherokee", "Zulu", "Huns", "Inca"
        ],
        "answer": "Cherokee"
    },
    {
        "question": "Name one of the two longest rivers in the United States.",
        "choices": [
            "Mississippi", "Amazon", "Colorado", "Nile"
        ],
        "answer": "Mississippi"
    },
    {
        "question": "What ocean is on the West Coast of the United States?",
        "choices": [
            "Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"
        ],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What ocean is on the East Coast of the United States?",
        "choices": [
            "Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Southern Ocean"
        ],
        "answer": "Atlantic Ocean"
    },
    {
        "question": "Name one U.S. territory.",
        "choices": [
            "Puerto Rico", "Greenland", "Jamaica", "Fiji"
        ],
        "answer": "Puerto Rico"
    },
    {
        "question": "Name one state that borders Canada.",
        "choices": [
            "Maine", "California", "Texas", "Florida"
        ],
        "answer": "Maine"
    },
    {
        "question": "Name one state that borders Mexico.",
        "choices": [
            "California", "Washington", "Oregon", "Alaska"
        ],
        "answer": "California"
    },
    {
        "question": "What is the capital of the United States?",
        "choices": [
            "Washington, D.C.", "Los Angeles", "New York", "Chicago"
        ],
        "answer": "Washington, D.C."
    },
    {
        "question": "Where is the Statue of Liberty?",
        "choices": [
            "New York", "Texas", "California", "Virginia"
        ],
        "answer": "New York"
    },
    {
        "question": "Why does the flag have 13 stripes?",
        "choices": [
            "They represent the original colonies", "They represent presidents", "They stand for lucky number", "They represent 13 wars"
        ],
        "answer": "They represent the original colonies"
    },
    {
        "question": "Why does the flag have 50 stars?",
        "choices": [
            "One for each state", "One for each president", "Number of colonies", "Number of wars"
        ],
        "answer": "One for each state"
    },
    {
        "question": "What is the name of the national anthem?",
        "choices": [
            "The Star-Spangled Banner", "America the Beautiful", "God Bless America", "Yankee Doodle"
        ],
        "answer": "The Star-Spangled Banner"
    },
    {
        "question": "When do we celebrate Independence Day?",
        "choices": [
            "July 4", "June 14", "July 14", "September 1"
        ],
        "answer": "July 4"
    },
    {
        "question": "Name two national U.S. holidays.",
        "choices": [
            "Thanksgiving and Independence Day", "Labor Day and Boxing Day", "Flag Day and Arbor Day", "Easter and Christmas"
        ],
        "answer": "Thanksgiving and Independence Day"
    }
]


NUM_QUESTIONS = 100  # Number of questions per quiz; adjust as needed

def get_random_questions(num):
    return random.sample(QUESTIONS, min(num, len(QUESTIONS)))

def main():
    st.title("N400 Civic Test Practice Quiz")
    st.write("Answer the following randomly-selected civic questions. Good luck!")

    # Session state setup
    if "quiz" not in st.session_state:
        st.session_state.quiz = get_random_questions(NUM_QUESTIONS)
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.selected = [None] * NUM_QUESTIONS
        st.session_state.show_result = False

    # Main quiz loop
    if st.session_state.q_index < len(st.session_state.quiz) and not st.session_state.show_result:
        idx = st.session_state.q_index
        q = st.session_state.quiz[idx]
        st.subheader(f"Question {idx + 1} of {len(st.session_state.quiz)}")
        st.write(q["question"])
        choices = q["choices"].copy()
        random.shuffle(choices)
        option = st.radio(
            "Select your answer:",
            choices,
            key=f"q{idx}"
        )
        if st.button("Submit", key=f"submit{idx}"):
            st.session_state.selected[idx] = option
            if option == q["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is: {q['answer']}")
            st.session_state.q_index += 1

    # Show results
    if (st.session_state.q_index >= len(st.session_state.quiz)) or st.session_state.show_result:
        st.write("## Quiz Complete!")
        st.write(f"Your final score is {st.session_state.score} out of {len(st.session_state.quiz)}.")
        if st.button("Restart Quiz"):
            for k in ["quiz", "q_index", "score", "selected", "show_result"]:
                del st.session_state[k]
            st.experimental_rerun()
        else:
            for i, q in enumerate(st.session_state.quiz):
                st.write(f"**Q{i+1}:** {q['question']}")
                st.write(f"Your answer: {st.session_state.selected[i]}")
                st.write(f"Correct answer: {q['answer']}")
                st.write("---")

if __name__ == "__main__":
    main()
