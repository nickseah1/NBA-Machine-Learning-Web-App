from dash.dependencies import Input, Output
from dash import dcc
from dash import html

from app import app

layout = [dcc.Markdown("""



### Welcome to the NBA Machine Learning Hub !




###### **Description of Applications**
  
 
**Predict NBA All-Stars:** Predict if a hypothetical player will be a NBA All-Star based on their points, rebounds, assists, steals, and blocks  

**Predict NBA Player Salary:** Predict the expected percentage of a team's salary cap a player should be worth based on their statistics  

**Visualize NBA Diversity:** Choose a country to see how the total number of NBA players from that country has changed over time


"""),]
          #html.Img(src='/assets/NBAImage.png'),]