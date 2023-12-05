from flask import render_template, Blueprint, send_file
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

score = Blueprint('score', __name__)

@score.route('/page1')
def score_page1():
    df = pd.read_csv('score.csv', index_col='번호')
    df2 = df[['이름', '학교', '키', 'SW특기']]
    df3 = df[['이름', '국어', '영어', '수학']]
    return render_template('page1.html',
                            table2=df2.to_html(classes='table table-striped', table_id='tbl2'),
                            table3=df3.to_html(classes='table table-striped', table_id='tbl3'))

@score.route('/graph')
def score_graph():

    return render_template('graph.html')

@score.route('/chart/<subject>')
def score_chart(subject):
    plt.figure(figsize=(10,5), dpi=50)
    df = pd.read_csv('score.csv', index_col='번호')
    x=df['이름'].values
    y=df[subject].values
    plt.bar(x, y, color='pink')
    # plt.show()
    img = BytesIO()
    plt.savefig(img, format='png', dpi=100)
    img.seek(0)
    return send_file(img, mimetype='image/png')

@score.route('/chart2')
def score_chart2():
    df=ps.read_csv('score.csv', index_col='번호')
    x=df['이름'].values
    kor=df['국어'].values
    eng=df['영어'].values
    mat=df['수학'].values
    index = np.arange(8)

    w = 0.25
    plt.figure(figsize=(10,5), dpi=80)
    plt.bar(index - w,kor, color='pink',width=w, label='국어')
    plt.bar(index,eng,color='skyblue', width=w, label='영어')
    plt.bar(index+ w ,eng,color='yellowgreen', width=w, label='수학')
    plt.legend(ncol=3)
    plt.xticks(index, x, rotation=30)
    img = BytesIO()
    plt.savefig(img, format='png', dpi=100)
    img.seek(0)
    return send_file(img, mimetype='image/png')

