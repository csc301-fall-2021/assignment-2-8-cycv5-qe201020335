# Web API for Covid-19 data
assignment-2-8-cycv5-qe201020335
## Pair Programming

Our team did pair programming throughout the entire project. For the most part we only work on the code together when one of us is stuck, but we did do some real pair programming together as well.

From the beginning, Yichen tried to start with writing the basic structure for a flask app. Since Tianhe has more experience in API development, Yichen asked Tianhe to help him with the overall structure of the app. That includes setting up the flask structure, the different routes in our app as well as different HTTP methods that we would like to support. Tianhe has no experience in databases so he was stuck. Yichen took over and showed him how to set up a database, define the schemas and turn the user input (the csv files) into entries in the database. Yichen also completed the methods for querying data from the database. You will notice that in the commit, Yichen uses mostly placeholders or hardcoded values for user input. That is because he didn’t know how to properly get the HTTP requests from the users and parse them to get the relevant information. Tianhe then helped Yichen implement the code for getting information from the requests. Together the team did some code review as well as developed the proper APIs to put onto Swagger.

As a group we think the experience was very positive. We usually do pair programming without even noticing it. Online video chatting and code sharing apps (codeTogether for example) make this experience easier than ever. Compared to simply dividing the work, pair programming gives the benefit of learning something new in the process and thinking together when stuck. We helped each other along the way and caught plenty of mistakes/typos in the code that otherwise wouldn’t be noticed that quickly. A small negative would be that the two of us must have a common time slot in our busy schedule to sit down and work together. This could be unviable for some, but fortunately it worked out well for us.

## Program Design

The program structure can easily be viewed on Swagger.
* Uploads: The upload route lets you upload your files. We think it would be very clear to have the type of the file you are uploading in the route.

  * /time_series/<data_type> (post, put):
This is for uploading time_series data. The data_type specifies what the numbers in the csv form represent (death, confirmed, active or recovered).

  * /daily_report (post, put):
This is for uploading a daily report. The program will parse the information for you.

* Queries
  * /cases (get):
This is where you can make queries on the data. Again, we think this is very intuitive to have a route for querying data. Parameters of the query will be supplied as parameters of the request.

The main objective is to make this program as clear as possible without super long routes or unclear names. And we made sure that post, put and get methods are implemented in their most intuitive ways, e.g. querying data would be a get and uploading a file to the system would be a post.

* Database: We design the database so that we can store only the relevant information. We have 4 tables in our database representing the death, confirmed, active and recovered table. Within each table, we have country_region, state_province, combined_key, cases, and date. This results in a fast search speed and any relevant information can be found within those four tables.
