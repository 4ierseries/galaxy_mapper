from flask import Flask, render_template
import pandas as pd
import plotly.graph_objects as go

app = Flask(__name__)

data = pd.read_csv('data.csv')

data = data.dropna(subset=['ra', 'dec', 'z'])
data['Distance'] = data['z'] * 3.0e5 / 70.0  # Hubble's Law: Distance = z * speed_of_light / Hubble_constant

@app.route('/')
def index():
    # Create the 3D plot using Plotly with always visible modebar
    fig = go.Figure(data=[go.Scatter3d(
        x=data['ra'],
        y=data['dec'],
        z=data['Distance'],
        mode='markers',
    )])

    config = {'displayModeBar': True}
    plot_html = fig.to_html(full_html=False, config=config)
    return render_template('index.html', plot_html=plot_html)

if __name__ == '__main__':
    app.run(debug=True)
