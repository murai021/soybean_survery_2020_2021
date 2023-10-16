###
Here you need a df with a 'State' column with average protein values of each state on the 'Protein' column. Color scale is customizable. 
You would need to have had the df created already with pandas. 

df = dataframe
### 

import plotly.express as px
fig = px.choropleth(df,
                    locations='State',
                    locationmode="USA-states",
                    scope="usa",
                    color='Protein_content',
                    color_continuous_scale="Viridis_r",
                    labels={'Protein':'Protein content (g/100g)'},
                    )
fig.update_layout(
    title_text='Protein content by state (2020)',
    title_x=0.5,
    title_font=dict(size=24, color='black', family="Arial, bold")
)


fig.update_coloraxes(colorbar_tickfont=dict(size=22, color = 'black', family="Arial, bold"))


fig.show()
