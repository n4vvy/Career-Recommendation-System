# Career-Recommendation-System

The Career Recommendation System is implemented using Python and Tkinter. The program contains a graphical user interface, a predefined collection of career profiles, and a scoring function that compares user selections with the available careers.

The application works locally and does not require internet access during execution.

# Software and Tools Used

Tool / Technology    Purpose
Python 3             Main programming language
Tkinter              Graphical user interface
VS Code              Writing and running the program
Python sets          Comparing skills and interests
Python dictionaries  Storing career profiles
Python sorting       Ranking career recommendations

# xplanation of the Implementation

Career database: The careers dictionary stores six career profiles. Each profile contains the skills required, relevant interests, a short description, and suggested learning areas.

Input collection: The user enters a name and selects skills and interests using Tkinter list boxes. The multiple-selection feature allows the user to choose more than one item.

Set operations: The & operator calculates the intersection between the user's selections and a career's predefined skills or interests. This identifies the matching items.

Score calculation: The program calculates a skill score and an interest score. The final score combines the two using the selected weights.

Recommendation ranking: Each career with a score greater than zero is added to the results. The results are sorted from highest to lowest score, and the top three are displayed.

Result presentation: The text box displays the career title, matching score, description, and suggested learning areas.

Input validation: The program checks that the user has entered a name and selected at least one skill and one interest. If the requirements are not satisfied, an error message is displayed.

# Results Analysis

The expected behavior of the application is that it generates career recommendations based on the user's selected skills and interests. Careers with stronger matches should generally appear higher in the result list.

The scoring approach makes the recommendation process understandable because users can see the matching percentage and read a description of each career.

The system also supports multiple recommendations, allowing users to explore several possible professional directions rather than receiving only one result.

However, the results depend on the career profiles and scoring weights. A career may receive a low score even when it could be suitable for a user if its profile does not contain the selected skills or interests.

The matching percentage is therefore a relative score within this prototype, not a scientifically validated measure of aptitude, personality, employability, or future success.

A further limitation is that the program uses manually defined career information. The quality of the recommendations could improve through broader career profiles, user feedback, and updated occupational information.


















