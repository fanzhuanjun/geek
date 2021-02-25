# 1. 预处理

## 1.1处理缺失值和异常样本


```
import numpy as np
import pandas as pd
import codecs
pd.set_option('max_colwidth',100) # 完整显示
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.style import use
use("fivethirtyeight")
from scipy.stats import norm

```


```
path = 'c:/pwork/fanza项目/DVD生数据.csv'
with codecs.open(path, 'r', 'utf-8', 'ignore') as f:
    data = pd.read_csv(f, header=None)
```


```
data.columns = [
    'url', '発売日', '収録時間', '出演者', '監督', 'シリーズ', 'メーカー', 'レーベル', 'ジャンル', '品番', 'wu',
    'title', '価格', 'img', '紹介', '平均評価', '総評価数' 
]
data = data.drop('wu', axis=1)
```


```
data.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>発売日</th>
      <th>収録時間</th>
      <th>出演者</th>
      <th>監督</th>
      <th>シリーズ</th>
      <th>メーカー</th>
      <th>レーベル</th>
      <th>ジャンル</th>
      <th>品番</th>
      <th>title</th>
      <th>価格</th>
      <th>img</th>
      <th>紹介</th>
      <th>平均評価</th>
      <th>総評価数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=18sprd1298/?dmmref=aMonoDvd_List/</td>
      <td>2020/06/25</td>
      <td>115分</td>
      <td>時田こずえ</td>
      <td>九十九究太</td>
      <td>代理出産の母</td>
      <td>タカラ映像</td>
      <td>ALEDDIN</td>
      <td>熟女 人妻・主婦 近親相姦 単体作品 中出し サンプル動画</td>
      <td>18sprd1298</td>
      <td>代理出産の母 時田こずえ</td>
      <td>2,458円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/18sprd1298/18sprd1298ps.jpg</td>
      <td>私達夫婦はある事で悩んでいた。そんな最中突然の義母の来訪に驚く私。すると奥から妻が少し寂しげな顔で現れた。妻はあることをお願いする為に義母を呼んでいた。妻は自分が不妊症であることを告げ、代理出...</td>
      <td>3点</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=odv433bod/?dmmref=aMonoDvd_List/</td>
      <td>2020/08/05</td>
      <td>80分</td>
      <td>神崎まゆみ</td>
      <td>----</td>
      <td>----</td>
      <td>大塚フロッピー</td>
      <td>大塚フロッピー</td>
      <td>スカトロ 単体作品 アナル 放尿・お漏らし 脱糞 サンプル動画 Blu-ray（ブルーレイ） ディスクオンデマンド 2010年代後半（DOD）</td>
      <td>odv433bod</td>
      <td>本人が自ら選んだ快楽脱糞行為 1 神崎まゆみ （ブルーレイディスク） （BOD）</td>
      <td>6,380円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/odv433bod/odv433bodps.jpg</td>
      <td>2017年11月19日発売の商品です\n\n願望1:イク顔と局部をドアップで見られたい…願望2:パンティの中にウンコをたっぷりお漏らししてみたい…女性にだってあまり大きな声で言えない願望がある...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=h_1001oyaj138dod/?dmmref=aMonoDvd_List/</td>
      <td>2020/07/20</td>
      <td>100分</td>
      <td>深田さえこ</td>
      <td>----</td>
      <td>----</td>
      <td>青春舎</td>
      <td>青春舎</td>
      <td>熟女 近親相姦 単体作品 中出し ディスクオンデマンド 2010年代後半（DOD）</td>
      <td>h_1001oyaj138dod</td>
      <td>親族相姦閉経を迎えた母 深田さえこ52歳 （DOD）</td>
      <td>1,540円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/h_1001oyaj138dod/h_1001oyaj138dodps.jpg</td>
      <td>2017年2月21日発売の商品です\n\n本能の赴くままさえこに襲い掛かる息子。母と息子の禁断関係が今始まる…イッテもイッテも終わらない抜かず中出し近親相姦！\n\n■ディスクオンデマンド商品...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```
print(f"样本数:{data.shape}")
```

    样本数:(45957, 16)
    


```
data = data.dropna(how='all')
data.shape
```




    (45957, 16)




```
data[data['title'].isnull()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>発売日</th>
      <th>収録時間</th>
      <th>出演者</th>
      <th>監督</th>
      <th>シリーズ</th>
      <th>メーカー</th>
      <th>レーベル</th>
      <th>ジャンル</th>
      <th>品番</th>
      <th>title</th>
      <th>価格</th>
      <th>img</th>
      <th>紹介</th>
      <th>平均評価</th>
      <th>総評価数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>260</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=84scpx303dod/?dmmref=aMonoDvd_Lhttps://www.dmm.co....</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>699</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=84scpx284dod/?dmmref=aMonoDvd_Lhttps://www.dmm.co....</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>806</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=84tkscpx394a/?dmmref=aMonoDvd_List/</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1278</th>
      <td>、対象商品が最大35％オフ！</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1279</th>
      <td>さらに、対象商品をご購入いただいた方10，000名様に、発送順に人気AV女優のカード全16種のうち、ランダムで1枚をプレゼント！！</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>45419</th>
      <td>ご注文から到着まで1週間程度かかる場合がございます。</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>45420</th>
      <td>※ディスクオンデマンド商品を複数同時にご注文いただいた場合は日本郵便の通常配送となります。</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>45421</th>
      <td>※複数の注文が同時に発送される場合、日本郵便の通常配送で同梱発送となる可能性があります。</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>45422</th>
      <td>注文確定後3時間以降はお客様都合によるキャンセルができません。"</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>45809</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1474siin008tk/?dmmref=aMonoDvd_List/</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>316 rows × 16 columns</p>
</div>




```
data.iloc[1270:1282,]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>発売日</th>
      <th>収録時間</th>
      <th>出演者</th>
      <th>監督</th>
      <th>シリーズ</th>
      <th>メーカー</th>
      <th>レーベル</th>
      <th>ジャンル</th>
      <th>品番</th>
      <th>title</th>
      <th>価格</th>
      <th>img</th>
      <th>紹介</th>
      <th>平均評価</th>
      <th>総評価数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1270</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=h_1000spye142dod/?dmmref=aMonoDvd_List/</td>
      <td>2020/08/18</td>
      <td>90分</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>SPYEYE</td>
      <td>SPYEYE</td>
      <td>女子校生 その他フェチ パンチラ 盗撮・のぞき 素人 ディスクオンデマンド 2010年代後半（DOD）</td>
      <td>h_1000spye142dod</td>
      <td>ローアングル女子校生通学路 （DOD）</td>
      <td>1,760円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/h_1000spye142dod/h_1000spye142dodps.jpg</td>
      <td>2017年11月7日発売の商品です\n\nバス車内にカメラを設置し、通学中の女子校生のパンティーを超接写！パンティーからはみ出す秘部、ハミ毛…イ●スタ世代の女子校生の下半身を徹底調査！\n\n...</td>
      <td>1点</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1271</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=84thth005/?dmmref=aMonoDvd_List/</td>
      <td>2020/05/15</td>
      <td>300分</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>ケイ・エム・プロデュース</td>
      <td>3000 スリーサウザンド</td>
      <td>制服 女子校生 中出し フェラ 4時間以上作品 サンプル動画</td>
      <td>84thth005</td>
      <td>憧れてた地元の先輩の気になる制服の中身は…</td>
      <td>2,622円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/84thth005/84thth005ps.jpg</td>
      <td>男は若かりし頃、誰しも年上の女性に憧れを抱く。僕より少し年上の制服姿の先輩。その年齢差が大人の色香を醸し出し僕に先輩の裸を連想させる。憧れの先輩を投影出来る30人のSEXを300分お届けします...</td>
      <td>3点</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1272</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=h_8978basx041/?dmmref=aMonoDvd_List/</td>
      <td>2020/05/01</td>
      <td>114分</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>サルトル映像出版</td>
      <td>熱血特価（BASEMENT9）</td>
      <td>キャバ嬢・風俗嬢 人妻・主婦 ローション・オイル アウトレット</td>
      <td>h_8978basx041</td>
      <td>【アウトレット】‘人妻お座敷マットヘルス体験入店本番挿入’ 旦那さんには内緒でお座敷マットヘルスに体験入店してあまりの気持ち良さにダメと言われても自らおちんちんをずっぽり挿入していくエッチな奥様たち</td>
      <td>1,628円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/h_8978basx041/h_8978basx041ps.jpg</td>
      <td>生活費の足しに…自分の小遣い稼ぎの為に…と一度も風俗経験のない人妻たちが非本番系のお座敷マットヘルス風俗店に面接に訪れて体験入店を試みる。しかし、講習中にキモチよくなってしまった欲求不満妻達は...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1273</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=h_254kir015/?dmmref=aMonoDvd_List/</td>
      <td>2020/08/20</td>
      <td>90分</td>
      <td>彩葉みおり</td>
      <td>----</td>
      <td>----</td>
      <td>STAR PARADISE</td>
      <td>KIRei（スターパラダイス）</td>
      <td>職業色々 巨乳 単体作品 イタズラ 中出し サンプル動画</td>
      <td>h_254kir015</td>
      <td>「わたし何でもやります」就職活動中の女子大生がハメられたセクハラ面接 彩葉みおり</td>
      <td>1,851円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/h_254kir015/h_254kir015ps.jpg</td>
      <td>抜群のスタイルで、小顔メガネな真面目っ娘が会社面接の担当官にセクハラされ放題！！「ウチは小さいが業界では名の通った会社。ヤル気のある人間しか必要ないんだよ。」女子大生のカラダをくまなくチェック...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1274</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_707mbdd2043tk/?dmmref=aMonoDvd_List/</td>
      <td>2020/08/21</td>
      <td>90分</td>
      <td>宇佐木あいか</td>
      <td>----</td>
      <td>ぱんつ日記</td>
      <td>メディアブランド</td>
      <td>制服グラビア</td>
      <td>単体作品 アイドル・芸能人 イメージビデオ サンプル動画 特典付き・セット商品</td>
      <td>n_707mbdd2043tk</td>
      <td>【数量限定】ぱんつ日記/宇佐木あいか チェキ付き</td>
      <td>3,328円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_707mbdd2043tk/n_707mbdd2043tkps.jpg</td>
      <td>スレンダー美少女・宇佐木あいかが迷い込むフェティシズムの森…女子校生愛好家に送るぱんつ日記の第2弾は可憐な美少女に襲いかかる。頬を赤く染めながら必死に応えるあいかちゃんの健気な姿に胸が締め付け...</td>
      <td>4点</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1275</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=2cwm146dod/?dmmref=aMonoDvd_List/</td>
      <td>2020/08/22</td>
      <td>130分</td>
      <td>立花くるみ</td>
      <td>五右衛門</td>
      <td>くちびる</td>
      <td>ワープエンタテインメント</td>
      <td>Washing machine</td>
      <td>美少女 ミニ系 その他フェチ ドキュメンタリー 単体作品 キス・接吻 サンプル動画 ディスクオンデマンド 2010年代前半（DOD）</td>
      <td>2cwm146dod</td>
      <td>くちびる 立花くるみ （DOD）</td>
      <td>1,757円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/2cwm146dod/2cwm146dodps.jpg</td>
      <td>2012年8月3日発売の商品です\n\n少女ノ唇ヲ蹂躙スル-。初夏の陽射しに輝く黒髪が…無防備に曝け出された柔肌が…小さな果実のような紅い唇が…放蕩な日々の中でやり場を失った男たちの劣情をいた...</td>
      <td>4点</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>1276</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=hhap001/?dmmref=aMonoDvd_List/</td>
      <td>2020/07/07</td>
      <td>480分</td>
      <td>----</td>
      <td>----</td>
      <td>BEST痴●</td>
      <td>アパッチ</td>
      <td>HHHグループ</td>
      <td>辱め 鬼畜 女子校生 ベスト・総集編 4時間以上作品 サンプル動画 トリプルハッピーキャンペーン</td>
      <td>hhap001</td>
      <td>BEST痴● ～被害に遭った20人の女子●生～</td>
      <td>2,130円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/hhap001/hhap001ps.jpg</td>
      <td>女子●生20名を犯しまくる怒涛の痴●作品集がここに！満員電車、本屋、バックヤード、エレベーターに駐輪場など、パンツ内大量射精！ノーピストン中出し、乳首こねくり回し、ノド奥イラマ、拘束輪●、膝立...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1277</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=h_859ten028/?dmmref=aMonoDvd_List/</td>
      <td>2020/05/01</td>
      <td>130分</td>
      <td>皆野あい</td>
      <td>天馬ハル</td>
      <td>湯けむり天獄</td>
      <td>ヴァンアソシエイツ</td>
      <td>TENMA</td>
      <td>ミニ系 SM 単体作品 温泉 縛り・緊縛 サンプル動画 スパンキング 蝋燭</td>
      <td>h_859ten028</td>
      <td>湯けむり天獄～縄情の宿～14 天縄の愛 編 皆野あい</td>
      <td>4,224円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/h_859ten028/h_859ten028ps.jpg</td>
      <td>あの【皆野あい】が緊縛温泉にやってきた！！孤高の縛師・天馬ハルの超大ヒットシリーズ「湯けむり天獄」シーズン2！第4弾！シリーズ14作目！湯けむり濡れつ縄愛撫あいの無垢な柔肌の秘部から甘い蜜が垂...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1278</th>
      <td>、対象商品が最大35％オフ！</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1279</th>
      <td>さらに、対象商品をご購入いただいた方10，000名様に、発送順に人気AV女優のカード全16種のうち、ランダムで1枚をプレゼント！！</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1280</th>
      <td>※セール期間前に注文された予約商品は価格保証が適用されません。</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1281</th>
      <td>※カードのプレゼントは準備数がなくなり次第告知なく終了いたします。初回版・限定版・予約商品・特典付き商品・セット商品に関するご注意"</td>
      <td>5点</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```
data.iloc[[260, 699, 806],]
#出现空值，原因是因为link的错误。
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>発売日</th>
      <th>収録時間</th>
      <th>出演者</th>
      <th>監督</th>
      <th>シリーズ</th>
      <th>メーカー</th>
      <th>レーベル</th>
      <th>ジャンル</th>
      <th>品番</th>
      <th>title</th>
      <th>価格</th>
      <th>img</th>
      <th>紹介</th>
      <th>平均評価</th>
      <th>総評価数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>260</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=84scpx303dod/?dmmref=aMonoDvd_Lhttps://www.dmm.co....</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>699</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=84scpx284dod/?dmmref=aMonoDvd_Lhttps://www.dmm.co....</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>806</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=84tkscpx394a/?dmmref=aMonoDvd_List/</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```
#直接删除异常值
data_dropna = data[data['img'].notnull()]
```


```
data_dropna.shape
```




    (45640, 16)




```
data_dropna.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 45640 entries, 0 to 45956
    Data columns (total 16 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   url     45640 non-null  object 
     1   発売日     45640 non-null  object 
     2   収録時間    45640 non-null  object 
     3   出演者     45640 non-null  object 
     4   監督      45640 non-null  object 
     5   シリーズ    45640 non-null  object 
     6   メーカー    45640 non-null  object 
     7   レーベル    45640 non-null  object 
     8   ジャンル    45640 non-null  object 
     9   品番      45640 non-null  object 
     10  title   45640 non-null  object 
     11  価格      45173 non-null  object 
     12  img     45640 non-null  object 
     13  紹介      45599 non-null  object 
     14  平均評価    29264 non-null  object 
     15  総評価数    29264 non-null  float64
    dtypes: float64(1), object(15)
    memory usage: 5.9+ MB
    


```
#没有异常
data_dropna[data_dropna['紹介'].isnull()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>発売日</th>
      <th>収録時間</th>
      <th>出演者</th>
      <th>監督</th>
      <th>シリーズ</th>
      <th>メーカー</th>
      <th>レーベル</th>
      <th>ジャンル</th>
      <th>品番</th>
      <th>title</th>
      <th>価格</th>
      <th>img</th>
      <th>紹介</th>
      <th>平均評価</th>
      <th>総評価数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2762</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd90/?dmmref=aMonoDvd_List/</td>
      <td>2020/05/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd90</td>
      <td>ツンデレ娘 奥手な初体験</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd90/n_1132oppd90ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2815</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd89/?dmmref=aMonoDvd_List/</td>
      <td>2020/05/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd89</td>
      <td>快感ヒロイン ぷるるん捜査線</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd89/n_1132oppd89ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2841</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd88/?dmmref=aMonoDvd_List/</td>
      <td>2020/05/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd88</td>
      <td>むっちり討ち入り 桃色忠臣蔵</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd88/n_1132oppd88ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2847</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132ksd43/?dmmref=aMonoDvd_List/</td>
      <td>2020/05/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132ksd43</td>
      <td>性具を売る女</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132ksd43/n_1132ksd43ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5669</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd93/?dmmref=aMonoDvd_List/</td>
      <td>2020/06/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd93</td>
      <td>人妻の吐息 淫らに愛して</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd93/n_1132oppd93ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5691</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd91/?dmmref=aMonoDvd_List/</td>
      <td>2020/06/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd91</td>
      <td>激イキ奥様 仕組まれた快楽</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd91/n_1132oppd91ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8952</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd96/?dmmref=aMonoDvd_List/</td>
      <td>2020/07/03</td>
      <td>----</td>
      <td>霜月るな\n神楽アイネ\n三上あや香</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd96</td>
      <td>ギャル番外地 シメさせてもらいます</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd96/n_1132oppd96ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8961</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd95/?dmmref=aMonoDvd_List/</td>
      <td>2020/07/03</td>
      <td>----</td>
      <td>涼南佳奈\n水城奈緒\n成沢きさき\n初美りん\n西森エリカ</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd95</td>
      <td>5人の女 愛と金とセックスと…</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd95/n_1132oppd95ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8966</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd94/?dmmref=aMonoDvd_List/</td>
      <td>2020/07/03</td>
      <td>----</td>
      <td>佐倉絆\n橘メアリー\n原美織</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd94</td>
      <td>溢れる淫汁 いけいけ、タイガー</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd94/n_1132oppd94ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11220</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd98/?dmmref=aMonoDvd_List/</td>
      <td>2020/08/05</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd98</td>
      <td>バージン協奏曲 それゆけ純白パンツ！</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd98/n_1132oppd98ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11231</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd97/?dmmref=aMonoDvd_List/</td>
      <td>2020/08/05</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd97</td>
      <td>濡れ絵筆 家庭教師と息子の嫁</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd97/n_1132oppd97ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13008</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd87/?dmmref=aMonoDvd_List/</td>
      <td>2020/04/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd87</td>
      <td>痴●電車 食い込み夢マッチ</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd87/n_1132oppd87ps.jpg</td>
      <td>NaN</td>
      <td>3点</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>13019</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd86/?dmmref=aMonoDvd_List/</td>
      <td>2020/04/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd86</td>
      <td>豊満OL 寝取られ人事</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd86/n_1132oppd86ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13027</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd85/?dmmref=aMonoDvd_List/</td>
      <td>2020/04/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd85</td>
      <td>師匠の女将さん いじりいじられ</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd85/n_1132oppd85ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14403</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd84/?dmmref=aMonoDvd_List/</td>
      <td>2020/03/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd84</td>
      <td>ピンク・ゾーン2 淫乱と円盤</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd84/n_1132oppd84ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14414</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd83/?dmmref=aMonoDvd_List/</td>
      <td>2020/03/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd83</td>
      <td>冷たい女 闇に響くよがり声</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd83/n_1132oppd83ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14433</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd82/?dmmref=aMonoDvd_List/</td>
      <td>2020/03/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd82</td>
      <td>日本夜伽話 パコってめでたし</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd82/n_1132oppd82ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19739</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd81/?dmmref=aMonoDvd_List/</td>
      <td>2020/02/04</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd81</td>
      <td>美乳夜曲 乱れる白肌</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd81/n_1132oppd81ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19747</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd80/?dmmref=aMonoDvd_List/</td>
      <td>2020/02/04</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd80</td>
      <td>熟女の誘惑 入れ食いの宿</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd80/n_1132oppd80ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19755</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd79/?dmmref=aMonoDvd_List/</td>
      <td>2020/02/04</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd79</td>
      <td>パンチラ病院 おとうさん大興奮！</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd79/n_1132oppd79ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20332</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd75/?dmmref=aMonoDvd_List/</td>
      <td>2019/12/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd75</td>
      <td>愛人生活 きみとなら…</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd75/n_1132oppd75ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20343</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd74/?dmmref=aMonoDvd_List/</td>
      <td>2019/12/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd74</td>
      <td>性鬼人間第二号～イキナサイ～</td>
      <td>2,613円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd74/n_1132oppd74ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20348</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd73/?dmmref=aMonoDvd_List/</td>
      <td>2019/12/03</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd73</td>
      <td>変態おやじ ラブ・ミー！イッてんだぁ～</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd73/n_1132oppd73ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23058</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd69/?dmmref=aMonoDvd_List/</td>
      <td>2019/10/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd69</td>
      <td>SEXアドベンチャー ワンダー・エロス</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd69/n_1132oppd69ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23065</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd68/?dmmref=aMonoDvd_List/</td>
      <td>2019/10/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd68</td>
      <td>フェチづくし 痴情の虜</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd68/n_1132oppd68ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23075</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd67/?dmmref=aMonoDvd_List/</td>
      <td>2019/10/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd67</td>
      <td>溺れるふたり ふやけるほど愛して</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd67/n_1132oppd67ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23262</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd78/?dmmref=aMonoDvd_List/</td>
      <td>2020/01/07</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd78</td>
      <td>白衣の妹 無防備なお尻</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd78/n_1132oppd78ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23269</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd77/?dmmref=aMonoDvd_List/</td>
      <td>2020/01/07</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd77</td>
      <td>誰にでもイヤラシイ秘密がある</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd77/n_1132oppd77ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23282</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd76/?dmmref=aMonoDvd_List/</td>
      <td>2020/01/07</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd76</td>
      <td>結婚前夜 やさしく挿れて</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd76/n_1132oppd76ps.jpg</td>
      <td>NaN</td>
      <td>5点</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>23889</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd63/?dmmref=aMonoDvd_List/</td>
      <td>2019/08/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd63</td>
      <td>だまされてペロペロ わかれて貰います</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd63/n_1132oppd63ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23899</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd62/?dmmref=aMonoDvd_List/</td>
      <td>2019/08/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd62</td>
      <td>煩悩チン貸住宅 淫らな我が家</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd62/n_1132oppd62ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23915</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd61/?dmmref=aMonoDvd_List/</td>
      <td>2019/08/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd61</td>
      <td>色慾怪談 ヌルっと入ります</td>
      <td>2,970円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd61/n_1132oppd61ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39125</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_627hpbn159/?dmmref=aMonoDvd_List/</td>
      <td>2019/11/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>サンプル動画 ドラマ エロス</td>
      <td>n_627hpbn159</td>
      <td>さすらいの恋人 眩暈</td>
      <td>2,200円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_627hpbn159/n_627hpbn159ps.jpg</td>
      <td>NaN</td>
      <td>3点</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>39142</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_627hpbn158/?dmmref=aMonoDvd_List/</td>
      <td>2019/11/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ドラマ エロス</td>
      <td>n_627hpbn158</td>
      <td>桃色身体検査</td>
      <td>2,200円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_627hpbn158/n_627hpbn158ps.jpg</td>
      <td>NaN</td>
      <td>4点</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>39156</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_627hpbn155/?dmmref=aMonoDvd_List/</td>
      <td>2019/11/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ドラマ エロス</td>
      <td>n_627hpbn155</td>
      <td>情婦はセーラー服</td>
      <td>3,003円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_627hpbn155/n_627hpbn155ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39167</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_627hpbn153/?dmmref=aMonoDvd_List/</td>
      <td>2019/11/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ドラマ エロス</td>
      <td>n_627hpbn153</td>
      <td>SEXハイウェイ 女の駐車場</td>
      <td>3,003円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_627hpbn153/n_627hpbn153ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39181</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_627hpbn152/?dmmref=aMonoDvd_List/</td>
      <td>2019/11/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>昼下りの情事</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ドラマ エロス</td>
      <td>n_627hpbn152</td>
      <td>昼下りの情事 すすり泣き</td>
      <td>3,003円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_627hpbn152/n_627hpbn152ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39189</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_627hpbn151/?dmmref=aMonoDvd_List/</td>
      <td>2019/11/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ハピネット・ピクチャーズ</td>
      <td>ドラマ エロス</td>
      <td>n_627hpbn151</td>
      <td>肉体犯罪海岸 ピラニヤの群れ</td>
      <td>3,003円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_627hpbn151/n_627hpbn151ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39207</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd72/?dmmref=aMonoDvd_List/</td>
      <td>2019/11/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd72</td>
      <td>福マン婦人 ねっとり寝取られ</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd72/n_1132oppd72ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39215</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd71/?dmmref=aMonoDvd_List/</td>
      <td>2019/11/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd71</td>
      <td>続・未亡人下宿 エロすぎちゃってごめんなさい</td>
      <td>2,970円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd71/n_1132oppd71ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39254</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=n_1132oppd70/?dmmref=aMonoDvd_List/</td>
      <td>2019/11/02</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>スターボード</td>
      <td>スターボード</td>
      <td>ドラマ エロス</td>
      <td>n_1132oppd70</td>
      <td>悶絶女優 銀幕の乳房</td>
      <td>2,791円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/n_1132oppd70/n_1132oppd70ps.jpg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```
print(f"删除后的样本数：{data_dropna.shape}")
```

    删除后的样本数：(45640, 16)
    


```
data_dropna[data_dropna['title'].str.contains("数量")]['title']
```




    74                                【数量限定】VictimGirlsR 私は、負けません！ 深田結梨 逢見リカ 逢見リカパンティとチェキ付き
    84                                【数量限定】VictimGirlsR 私は、負けません！ 深田結梨 逢見リカ 深田結梨パンティとチェキ付き
    90       【数量限定】様々なシチュエーションで痴女たちが男を上から目線で陵●する騎乗位！パンストを見せつけ破れた穴からパンティずらして強●挿入！3 デジタル写真集付き
    103                               【数量限定】ノーブラノーパンで挑発してくるスケベ奥さんが隣に引っ越してきた！ 浜崎真緒 デジタル写真集付き
    117                              【数量限定】ノーブラノーパンで挑発してくるスケベ奥さんが隣に引っ越してきた！ 浜崎真緒 パンティとチェキ付き
                                                  ...                                      
    21548                                                  【数量限定】Nudie Doll/アリー・アディソン チェキ付き
    21579                                                         【数量限定】シースルーラブ/星奈あかね チェキ付き
    21613                                                         【数量限定】蒼いフォトグラフ/星那美月 チェキ付き
    21628                                                               【数量限定】濡蓮/杏ちゃむ チェキ付き
    24168                                                         【数量限定】kmp超得お楽しみDVD10作品パック
    Name: title, Length: 946, dtype: object




```
# 删除打折的重复样本，标题为数量限定
data_dropna = data_dropna[~data_dropna['title'].str.contains("【数量限定")]
data_dropna.shape
```




    (44697, 16)




```
#无异常
# data_dropna[data_dropna['title'].str.contains("数量")].shape
```


```
#删除相同样本
data_dropna = data_dropna.drop_duplicates()
data_dropna.shape
```




    (44697, 16)



## 1.2 数据类型转换


```
data_dropna.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>発売日</th>
      <th>収録時間</th>
      <th>出演者</th>
      <th>監督</th>
      <th>シリーズ</th>
      <th>メーカー</th>
      <th>レーベル</th>
      <th>ジャンル</th>
      <th>品番</th>
      <th>title</th>
      <th>価格</th>
      <th>img</th>
      <th>紹介</th>
      <th>平均評価</th>
      <th>総評価数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=18sprd1298/?dmmref=aMonoDvd_List/</td>
      <td>2020/06/25</td>
      <td>115分</td>
      <td>時田こずえ</td>
      <td>九十九究太</td>
      <td>代理出産の母</td>
      <td>タカラ映像</td>
      <td>ALEDDIN</td>
      <td>熟女 人妻・主婦 近親相姦 単体作品 中出し サンプル動画</td>
      <td>18sprd1298</td>
      <td>代理出産の母 時田こずえ</td>
      <td>2,458円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/18sprd1298/18sprd1298ps.jpg</td>
      <td>私達夫婦はある事で悩んでいた。そんな最中突然の義母の来訪に驚く私。すると奥から妻が少し寂しげな顔で現れた。妻はあることをお願いする為に義母を呼んでいた。妻は自分が不妊症であることを告げ、代理出...</td>
      <td>3点</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=odv433bod/?dmmref=aMonoDvd_List/</td>
      <td>2020/08/05</td>
      <td>80分</td>
      <td>神崎まゆみ</td>
      <td>----</td>
      <td>----</td>
      <td>大塚フロッピー</td>
      <td>大塚フロッピー</td>
      <td>スカトロ 単体作品 アナル 放尿・お漏らし 脱糞 サンプル動画 Blu-ray（ブルーレイ） ディスクオンデマンド 2010年代後半（DOD）</td>
      <td>odv433bod</td>
      <td>本人が自ら選んだ快楽脱糞行為 1 神崎まゆみ （ブルーレイディスク） （BOD）</td>
      <td>6,380円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/odv433bod/odv433bodps.jpg</td>
      <td>2017年11月19日発売の商品です\n\n願望1:イク顔と局部をドアップで見られたい…願望2:パンティの中にウンコをたっぷりお漏らししてみたい…女性にだってあまり大きな声で言えない願望がある...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=h_1001oyaj138dod/?dmmref=aMonoDvd_List/</td>
      <td>2020/07/20</td>
      <td>100分</td>
      <td>深田さえこ</td>
      <td>----</td>
      <td>----</td>
      <td>青春舎</td>
      <td>青春舎</td>
      <td>熟女 近親相姦 単体作品 中出し ディスクオンデマンド 2010年代後半（DOD）</td>
      <td>h_1001oyaj138dod</td>
      <td>親族相姦閉経を迎えた母 深田さえこ52歳 （DOD）</td>
      <td>1,540円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/h_1001oyaj138dod/h_1001oyaj138dodps.jpg</td>
      <td>2017年2月21日発売の商品です\n\n本能の赴くままさえこに襲い掛かる息子。母と息子の禁断関係が今始まる…イッテもイッテも終わらない抜かず中出し近親相姦！\n\n■ディスクオンデマンド商品...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=h_086abba482/?dmmref=aMonoDvd_List/</td>
      <td>2020/08/06</td>
      <td>480分</td>
      <td>----</td>
      <td>----</td>
      <td>----</td>
      <td>センタービレッジ</td>
      <td>センタービレッジ</td>
      <td>熟女 人妻・主婦 中出し ベスト・総集編 4時間以上作品 サンプル動画 CVC・熟女ラボ30％オフセール</td>
      <td>h_086abba482</td>
      <td>中年オヤジのねっとり変態中出しSEXの後に若い鬼畜チ●ポで種付け追姦ピストンされた熟女～俺の方がいいだろう！！あいつのザーメンを掻き出すほどたっぷりと出してやるよ～ 50連発8時間2枚組</td>
      <td>2,926円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/h_086abba482/h_086abba482ps.jpg</td>
      <td>親父とたっぷり楽しんだのか？貧乳スレンダー熟女のドロついたマンコに押し入る若きデカチンが残った精子を引っ掻き回し追撃ザーメンをくらわせる！！夫と息子の2人分の濃厚スペルマが溢れる蜜壺…中年オヤ...</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=18tlso003dod/?dmmref=aMonoDvd_List/</td>
      <td>2020/06/24</td>
      <td>120分</td>
      <td>結城みさ</td>
      <td>路上・コーマン</td>
      <td>み～んな一緒に筆おろしましょ</td>
      <td>タカラ映像</td>
      <td>Thalasso</td>
      <td>クンニ 熟女 人妻・主婦 童貞 単体作品 サンプル動画 ディスクオンデマンド 2010年代前半（DOD）</td>
      <td>18tlso003dod</td>
      <td>み～んな一緒に筆おろしましょ 結城みさ （DOD）</td>
      <td>2,500円</td>
      <td>https://pics.dmm.co.jp/mono/movie/adult/18tlso003dod/18tlso003dodps.jpg</td>
      <td>2010年11月4日発売の商品です\n\n人妻でもあり、母であり、アダルト女優でもある結城みさが、筆下ろしという行為を通し、童貞の欲望を優しく受け止めるエロさ、母性を感じさせる包み込むような性...</td>
      <td>3.8点</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>




```
data_dropna['発売日'] = pd.to_datetime(data_dropna['発売日'])
data_dropna['価格'] = data_dropna['価格'].str.replace(",", "").str.replace("円", "").astype("float")
data_dropna['平均評価'] = data_dropna['平均評価'].str.replace("点", "")
data_dropna['総評価数'] = data_dropna['総評価数'].astype('float')
```


```
data_dropna['平均評価'] = data_dropna['平均評価'].astype("float")
data_dropna["総分数"] = data_dropna['平均評価'] * data_dropna['総評価数']
```


```
data_dropna.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 44697 entries, 0 to 45956
    Data columns (total 17 columns):
     #   Column  Non-Null Count  Dtype         
    ---  ------  --------------  -----         
     0   url     44697 non-null  object        
     1   発売日     44697 non-null  datetime64[ns]
     2   収録時間    44697 non-null  object        
     3   出演者     44697 non-null  object        
     4   監督      44697 non-null  object        
     5   シリーズ    44697 non-null  object        
     6   メーカー    44697 non-null  object        
     7   レーベル    44697 non-null  object        
     8   ジャンル    44697 non-null  object        
     9   品番      44697 non-null  object        
     10  title   44697 non-null  object        
     11  価格      44232 non-null  float64       
     12  img     44697 non-null  object        
     13  紹介      44656 non-null  object        
     14  平均評価    28589 non-null  float64       
     15  総評価数    28589 non-null  float64       
     16  総分数     28589 non-null  float64       
    dtypes: datetime64[ns](1), float64(4), object(12)
    memory usage: 6.1+ MB
    


```
data_dropna.to_csv("c:/pwork/fanza项目/DVD整理后数据.csv", encoding='utf_8_sig')
```

# 2. 描述统计及可视化分析


```
data_dropna.describe().round(2)
#评价数只有5.42，买DVD的人可能并不多。
#对评价数最多和总分数最多的作品有兴趣，可以继续研究
#有多少作品是没有评价的？
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>価格</th>
      <th>平均評価</th>
      <th>総評価数</th>
      <th>総分数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>44232.00</td>
      <td>28589.00</td>
      <td>28589.00</td>
      <td>28589.00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2192.04</td>
      <td>3.93</td>
      <td>5.42</td>
      <td>22.03</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1153.29</td>
      <td>0.94</td>
      <td>9.32</td>
      <td>39.05</td>
    </tr>
    <tr>
      <th>min</th>
      <td>94.00</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1540.00</td>
      <td>3.50</td>
      <td>1.00</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2130.00</td>
      <td>4.00</td>
      <td>3.00</td>
      <td>12.00</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2556.00</td>
      <td>4.67</td>
      <td>6.00</td>
      <td>24.01</td>
    </tr>
    <tr>
      <th>max</th>
      <td>35648.00</td>
      <td>5.00</td>
      <td>315.00</td>
      <td>1338.75</td>
    </tr>
  </tbody>
</table>
</div>




```
data2019 = data_dropna[data_dropna['発売日'].dt.year == 2019]
data2020 = data_dropna[data_dropna['発売日'].dt.year == 2020]
```


```
print(f"有{data_dropna['平均評価'].isnull().sum()}个样本无评价！")
```

    有16108个样本无评价！
    


```
data_dropna.sort_values(ascending=False, by='総評価数')[:10][['url', 'title', '発売日', '出演者']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>title</th>
      <th>発売日</th>
      <th>出演者</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15860</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7ipx019/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】FIRST IMPRESSION 120 完美 PERFECT BEAUTY 森月茉由【アウトレット】</td>
      <td>2020-03-06</td>
      <td>森月茉由</td>
    </tr>
    <tr>
      <th>38016</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7miae108/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】乳首をず～っとこねくりっ放し性交 椎名そら【アウトレット】</td>
      <td>2019-10-04</td>
      <td>椎名そら</td>
    </tr>
    <tr>
      <th>10093</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7mide502/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】中出し4本番 芸能人MOODYZデビュー解禁SP！！ 仲村みう【アウトレット】</td>
      <td>2020-07-06</td>
      <td>仲村みう</td>
    </tr>
    <tr>
      <th>16209</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7snis919/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】最高級アイドル風俗マンションへようこそ 三上悠亜の密着性感テクニック150分フルコース【アウトレット】</td>
      <td>2020-03-06</td>
      <td>三上悠亜</td>
    </tr>
    <tr>
      <th>28328</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7ipx043/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】リピーター続出！噂の本番できちゃうおっパブ店 Gカップグラドル巨乳嬢を味わい尽くせ！ 桜空もも【アウトレット】</td>
      <td>2019-11-06</td>
      <td>桜空もも</td>
    </tr>
    <tr>
      <th>38024</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7pgd949/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】同窓会NTR～妻の最低な元カレが盗撮した浮気中出し映像～【アウトレット】</td>
      <td>2019-10-04</td>
      <td>----</td>
    </tr>
    <tr>
      <th>10106</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7ssni190/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】新人NO.1STYLE 河北彩花AVデビュー【アウトレット】</td>
      <td>2020-07-06</td>
      <td>河北彩花</td>
    </tr>
    <tr>
      <th>24051</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=blor128/?dmmref=aMonoDvd_List/</td>
      <td>ボーイッシュで男友達みたいな彼女は隠れ巨乳でした！ 飲み会とかで盛り上げてくれる面白い女子を半泣きアクメに追い込んだ！</td>
      <td>2019-08-25</td>
      <td>----</td>
    </tr>
    <tr>
      <th>8209</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7adn115/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】不埒な姦係 年下男と巨乳妻 松下紗栄子【アウトレット】</td>
      <td>2020-06-05</td>
      <td>松下紗栄子</td>
    </tr>
    <tr>
      <th>7530</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7snis964/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】汁汗だくだく唾液涎ダラダラ国民的アイドルの本気汁全漏らし性交 三上悠亜【アウトレット】</td>
      <td>2020-08-06</td>
      <td>三上悠亜</td>
    </tr>
  </tbody>
</table>
</div>




```
#读取图片
from skimage import io
def readImg(img_src):
    image = io.imread(img_src)
    io.imshow(image)
    plt.grid(False)
    io.show()
```


```
# print('销量领先：')
# for i in data_dropna.sort_values(by='総評価数', ascending=False)[:5]['img']:
#     i = i.replace('ps.jpg', 'pl.jpg')
#     readImg(i)
```


```
# print('综合领先：')
# for i in data_dropna.sort_values(by='総分数', ascending=False)[:5]['img']:
#     i = i.replace('ps.jpg', 'pl.jpg')
#     readImg(i)
```


```
data_dropna.sort_values(ascending=False, by='総分数')[:10][['url', 'title', '発売日', '出演者', '価格']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>title</th>
      <th>発売日</th>
      <th>出演者</th>
      <th>価格</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15860</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7ipx019/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】FIRST IMPRESSION 120 完美 PERFECT BEAUTY 森月茉由【アウトレット】</td>
      <td>2020-03-06</td>
      <td>森月茉由</td>
      <td>1134.0</td>
    </tr>
    <tr>
      <th>38016</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7miae108/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】乳首をず～っとこねくりっ放し性交 椎名そら【アウトレット】</td>
      <td>2019-10-04</td>
      <td>椎名そら</td>
      <td>1155.0</td>
    </tr>
    <tr>
      <th>16209</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7snis919/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】最高級アイドル風俗マンションへようこそ 三上悠亜の密着性感テクニック150分フルコース【アウトレット】</td>
      <td>2020-03-06</td>
      <td>三上悠亜</td>
      <td>1134.0</td>
    </tr>
    <tr>
      <th>38024</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7pgd949/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】同窓会NTR～妻の最低な元カレが盗撮した浮気中出し映像～【アウトレット】</td>
      <td>2019-10-04</td>
      <td>----</td>
      <td>1155.0</td>
    </tr>
    <tr>
      <th>28328</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7ipx043/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】リピーター続出！噂の本番できちゃうおっパブ店 Gカップグラドル巨乳嬢を味わい尽くせ！ 桜空もも【アウトレット】</td>
      <td>2019-11-06</td>
      <td>桜空もも</td>
      <td>1155.0</td>
    </tr>
    <tr>
      <th>10093</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7mide502/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】中出し4本番 芸能人MOODYZデビュー解禁SP！！ 仲村みう【アウトレット】</td>
      <td>2020-07-06</td>
      <td>仲村みう</td>
      <td>1134.0</td>
    </tr>
    <tr>
      <th>10106</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7ssni190/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】新人NO.1STYLE 河北彩花AVデビュー【アウトレット】</td>
      <td>2020-07-06</td>
      <td>河北彩花</td>
      <td>1134.0</td>
    </tr>
    <tr>
      <th>24051</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=blor128/?dmmref=aMonoDvd_List/</td>
      <td>ボーイッシュで男友達みたいな彼女は隠れ巨乳でした！ 飲み会とかで盛り上げてくれる面白い女子を半泣きアクメに追い込んだ！</td>
      <td>2019-08-25</td>
      <td>----</td>
      <td>2458.0</td>
    </tr>
    <tr>
      <th>7530</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7snis964/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】汁汗だくだく唾液涎ダラダラ国民的アイドルの本気汁全漏らし性交 三上悠亜【アウトレット】</td>
      <td>2020-08-06</td>
      <td>三上悠亜</td>
      <td>1134.0</td>
    </tr>
    <tr>
      <th>8209</th>
      <td>https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=7adn115/?dmmref=aMonoDvd_List/</td>
      <td>【ベストヒッツ】不埒な姦係 年下男と巨乳妻 松下紗栄子【アウトレット】</td>
      <td>2020-06-05</td>
      <td>松下紗栄子</td>
      <td>1134.0</td>
    </tr>
  </tbody>
</table>
</div>



因变量的可视化


```
plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #用来正常显示中文标签

sns.distplot(data_dropna["平均評価"], fit=norm)
```




    <AxesSubplot:xlabel='平均評価'>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_36_1.png)



```
sns.distplot(np.log(data_dropna["平均評価"]), fit=norm)
```




    <AxesSubplot:xlabel='平均評価'>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_37_1.png)



```
sns.distplot(data_dropna["総分数"], fit=norm)
```




    <AxesSubplot:xlabel='総分数'>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_38_1.png)



```
sns.distplot(np.log(data_dropna["総分数"]), fit=norm)
```




    <AxesSubplot:xlabel='総分数'>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_39_1.png)



```
sns.distplot(data_dropna["総評価数"], fit=norm)
```




    <AxesSubplot:xlabel='総評価数'>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_40_1.png)



```
sns.distplot(np.log(data_dropna["総評価数"]), fit=norm)
```




    <AxesSubplot:xlabel='総評価数'>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_41_1.png)



```
data_dropna['発売日'].dt.year.value_counts()
```




    2019    23989
    2020    20708
    Name: 発売日, dtype: int64




```
data_dropna['発売日'].dt.month.value_counts()
```




    5     5529
    8     5218
    7     5209
    6     4724
    4     4593
    3     3500
    10    3150
    2     3129
    1     2502
    12    2430
    9     2369
    11    2344
    Name: 発売日, dtype: int64




```
mon = data_dropna['発売日'].dt.month.value_counts()
# sort_index 很重要
mon.sort_index().plot()
plt.title("全样本发行数量")
plt.xlabel("月份")
plt.xticks([i for i in range(1, 13)])
```




    ([<matplotlib.axis.XTick at 0x1fe86996430>,
      <matplotlib.axis.XTick at 0x1fe86996400>,
      <matplotlib.axis.XTick at 0x1fe869b8880>,
      <matplotlib.axis.XTick at 0x1fe869cf280>,
      <matplotlib.axis.XTick at 0x1fe869cf5e0>,
      <matplotlib.axis.XTick at 0x1fe869cfaf0>,
      <matplotlib.axis.XTick at 0x1fe869d5040>,
      <matplotlib.axis.XTick at 0x1fe869d5550>,
      <matplotlib.axis.XTick at 0x1fe8698df40>,
      <matplotlib.axis.XTick at 0x1fe869d5d90>,
      <matplotlib.axis.XTick at 0x1fe869db2e0>,
      <matplotlib.axis.XTick at 0x1fe869db7f0>],
     [Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, ''),
      Text(0, 0, '')])




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_44_1.png)



```
data2019['発売日'].dt.month.value_counts().sort_index().plot()
data2020['発売日'].dt.month.value_counts().sort_index().plot()

plt.title("2019与2020发行数量")
plt.xlabel("月份")
plt.xticks([i for i in range(1, 13)])
plt.legend(["2019年", "2020年"])
# 由于我们搜集的数据样本有限，2019年只有3-12月数据，而2020年有1-9月份数据。
# 无法进行总量的比较
```




    <matplotlib.legend.Legend at 0x1fe86a34640>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_45_1.png)


从女优角度分析


```
print("发片最多的女优：")
data_dropna['出演者'].value_counts()[1:10]
```

    发片最多的女优：
    




    深田えいみ    136
    波多野結衣    123
    渚みつき     111
    凛音とうか    107
    篠田ゆう     106
    永瀬ゆい      99
    今井夏帆      94
    美谷朱里      93
    篠崎かんな     89
    Name: 出演者, dtype: int64




```
print("2019年发片最多的女优：")
print(data2019['出演者'].value_counts()[1:10])
print("---"*10)
print("2020年发片最多的女优：")
print(data2020['出演者'].value_counts()[1:10])
```

    2019年发片最多的女优：
    深田えいみ    85
    凛音とうか    70
    篠崎かんな    67
    波多野結衣    64
    美谷朱里     63
    渚みつき     63
    稲場るか     58
    篠田ゆう     53
    八乃つばさ    52
    Name: 出演者, dtype: int64
    ------------------------------
    2020年发片最多的女优：
    波多野結衣                 59
    松本いちか                 59
    永瀬ゆい                  56
    川上奈々美                 54
    篠田ゆう                  53
    今井夏帆                  52
    深田えいみ                 51
    渚みつき                  48
    澤村レイコ（高坂保奈美、高坂ますみ）    47
    Name: 出演者, dtype: int64
    

2019年和两个年度中发片最多的女优均是深田えいみ。松本いちか在总榜单上没有名字，而在2020年居然位居前首，说明她是2020年才走红的新星。

波多野結衣两年的出片数均不菲。


```
listA = data2019['出演者'].value_counts()[1:15].index
listB = data2020['出演者'].value_counts()[1:15].index
print("两个年度均出现的女优")
print(list(set(listA).union(set(listB))))
print("---"*10)
print("两个年度的交集")
print([i for i in listA if i in listB])
print("---"*10)
print("求差集，在2020中但不在2019中")
print(list(set(listB).difference(set(listA))))
```

    两个年度均出现的女优
    ['永瀬ゆい', '澤村レイコ（高坂保奈美、高坂ますみ）', '奏音かのん', '今井夏帆', '篠崎かんな', '川上奈々美', '有坂深雪', '松本菜奈実', '深田えいみ', '風間ゆみ', '篠田ゆう', '美谷朱里', '美園和花', '波多野結衣', '枢木あおい', '八乃つばさ', '渚みつき', '冬愛ことね', '凛音とうか', '松本いちか', '永井マリア', '稲場るか']
    ------------------------------
    两个年度的交集
    ['深田えいみ', '凛音とうか', '波多野結衣', '渚みつき', '篠田ゆう', '永瀬ゆい']
    ------------------------------
    求差集，在2020中但不在2019中
    ['奏音かのん', '澤村レイコ（高坂保奈美、高坂ますみ）', '美園和花', '今井夏帆', '松本いちか', '永井マリア', '川上奈々美', '風間ゆみ']
    


```
data_dropna.groupby("出演者")["総評価数"].sum().sort_values(ascending=False)[1:10]
#総評価数最靠前的女优
```




    出演者
    三上悠亜      1444.0
    高橋しょう子    1183.0
    深田えいみ     1093.0
    根尾あかり      937.0
    橋本ありな      885.0
    山岸逢花       862.0
    松下紗栄子      857.0
    美谷朱里       844.0
    七沢みあ       788.0
    Name: 総評価数, dtype: float64




```
data_dropna.groupby("出演者")["総分数"].sum().sort_values(ascending=False)[1:10]
#平均分最靠前的女优
```




    出演者
    三上悠亜      5936.91
    高橋しょう子    4538.16
    深田えいみ     4515.62
    根尾あかり     4139.56
    橋本ありな     3711.70
    山岸逢花      3647.72
    七沢みあ      3590.01
    松下紗栄子     3578.88
    美谷朱里      3568.38
    Name: 総分数, dtype: float64




```
data_dropna['yearmonth'] = data_dropna['発売日'].map(lambda x: 100*x.year + x.month)
data_dropna['yearmonth'].head(5)
```




    0    202006
    1    202008
    2    202007
    3    202008
    4    202006
    Name: yearmonth, dtype: int64




```
data_dropna['yearmonth'].value_counts().sort_index().plot(kind='bar')
```




    <AxesSubplot:>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_54_1.png)



```
data_dropna[data_dropna['出演者']=='松本いちか']['yearmonth'].value_counts().sort_index().plot(kind='bar')
```




    <AxesSubplot:>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_55_1.png)



```
data_dropna[data_dropna['出演者']=='波多野結衣']['yearmonth'].value_counts().sort_index().plot(kind='bar')
```




    <AxesSubplot:>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_56_1.png)



```
data_dropna[data_dropna['出演者']=='深田えいみ']['yearmonth'].value_counts().sort_index().plot(kind='bar')
```




    <AxesSubplot:>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_57_1.png)


其他变量


```
data_dropna['監督'].value_counts(ascending=False)[1:10]
```




    K太郎          631
    TODO         391
    BIRDMAN鉄平    309
    豆沢豆太郎        281
    三島六三郎        270
    うさぴょん。       240
    キョウセイ        201
    ドラゴン西川       195
    杉ノ木          187
    Name: 監督, dtype: int64




```
data_dropna['メーカー'].value_counts(ascending=False)[1:10]
```




    プレステージ             1684
    STAR PARADISE      1454
    エスワン ナンバーワンスタイル     854
    ムーディーズ              789
    SODクリエイト            780
    マドンナ                770
    なでしこ                734
    ROCKET              627
    アロマ企画               610
    Name: メーカー, dtype: int64




```
data_dropna['レーベル'].value_counts(ascending=False)[1:10]
```




    ----             1968
    卍GROUP           1239
    Nadeshiko         734
    S1 NO.1 STYLE     720
    Madonna           645
    REAL（レアルワークス）     594
    S級素人              591
    HHHグループ           573
    ROCKET            554
    Name: レーベル, dtype: int64




```
data_dropna['ジャンル'][0]
```




    '熟女\xa0人妻・主婦\xa0近親相姦\xa0単体作品\xa0中出し\xa0サンプル動画'




```
# 多响应变量转化为虚拟变量
x = data_dropna['ジャンル'].str.get_dummies('\xa0')
```


```
x.sum().sort_values(ascending=False)[:20]
```




    サンプル動画           36034
    単体作品             18689
    中出し              15145
    ディスクオンデマンド       11498
    巨乳               11322
    人妻・主婦            10616
    熟女               10387
    4時間以上作品           9494
    アウトレット            5435
    素人                5348
    ベスト・総集編           5095
    美少女               4931
    2010年代後半（DOD）     4646
    2010年代前半（DOD）     4636
    痴女                3952
    フェラ               3780
    寝取り・寝取られ・NTR      3381
    近親相姦              3191
    デジモ               3098
    ドラマ               3047
    dtype: int64




```
x.shape
```




    (44697, 309)




```
x.sum().sort_values(ascending=False)[:20].index
```




    Index(['サンプル動画', '単体作品', '中出し', 'ディスクオンデマンド', '巨乳', '人妻・主婦', '熟女', '4時間以上作品',
           'アウトレット', '素人', 'ベスト・総集編', '美少女', '2010年代後半（DOD）', '2010年代前半（DOD）',
           '痴女', 'フェラ', '寝取り・寝取られ・NTR', '近親相姦', 'デジモ', 'ドラマ'],
          dtype='object')




```
data_x = pd.concat([data_dropna, x], axis=1)
# 合并数据集
```


```
for i in x.sum().sort_values(ascending=False)[:20].index:
    print(data_x.groupby(by=i)['平均評価'].mean())
```

    サンプル動画
    0    3.498115
    1    3.986321
    Name: 平均評価, dtype: float64
    単体作品
    0    3.827645
    1    4.036298
    Name: 平均評価, dtype: float64
    中出し
    0    3.907012
    1    3.983067
    Name: 平均評価, dtype: float64
    ディスクオンデマンド
    0    4.025965
    1    3.556132
    Name: 平均評価, dtype: float64
    巨乳
    0    3.913343
    1    3.989678
    Name: 平均評価, dtype: float64
    人妻・主婦
    0    3.931329
    1    3.945124
    Name: 平均評価, dtype: float64
    熟女
    0    3.947723
    1    3.876919
    Name: 平均評価, dtype: float64
    4時間以上作品
    0    3.941679
    1    3.889255
    Name: 平均評価, dtype: float64
    アウトレット
    0    3.938991
    1    3.907428
    Name: 平均評価, dtype: float64
    素人
    0    3.937730
    1    3.908251
    Name: 平均評価, dtype: float64
    ベスト・総集編
    0    3.948546
    1    3.734955
    Name: 平均評価, dtype: float64
    美少女
    0    3.913598
    1    4.082442
    Name: 平均評価, dtype: float64
    2010年代後半（DOD）
    0    3.940082
    1    3.859673
    Name: 平均評価, dtype: float64
    2010年代前半（DOD）
    0    3.985047
    1    3.393682
    Name: 平均評価, dtype: float64
    痴女
    0    3.915758
    1    4.106780
    Name: 平均評価, dtype: float64
    フェラ
    0    3.926728
    1    4.016783
    Name: 平均評価, dtype: float64
    寝取り・寝取られ・NTR
    0    3.925947
    1    4.025221
    Name: 平均評価, dtype: float64
    近親相姦
    0    3.940144
    1    3.849944
    Name: 平均評価, dtype: float64
    デジモ
    0    3.917748
    1    4.106449
    Name: 平均評価, dtype: float64
    ドラマ
    0    3.931164
    1    3.975640
    Name: 平均評価, dtype: float64
    


```
g = pd.concat([x, data_dropna['総分数']], axis=1)

k = 15
cols = g.corr()['総分数'].sort_values(ascending=False).index[:k]

f, ax = plt.subplots(figsize=(15, 15))
hm = sns.heatmap(XXX[cols].corr(), cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 15},
                )
```


![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_69_0.png)



```

```

# 3. 模型建立


```
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

tree = DecisionTreeRegressor(random_state=42)
tree_params = {"max_depth": [None, 1, 3, 5, 7, 9]}
```


```
data_dropna.columns
```




    Index(['url', '発売日', '収録時間', '出演者', '監督', 'シリーズ', 'メーカー', 'レーベル', 'ジャンル', '品番',
           'title', '価格', 'img', '紹介', '平均評価', '総評価数', '総分数', 'yearmonth'],
          dtype='object')




```
y1 = data_dropna['平均評価'].fillna(-999)
y2 = data_dropna['総評価数'].fillna(-999)
y3 = np.log(data_dropna['総分数']).fillna(-999)
```


```
sns.distplot(y3)
```




    <AxesSubplot:xlabel='総分数'>




![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_75_1.png)



```
X1_train, X1_test, y1_train, y1_test = train_test_split(x, y1)
```


```
X2_train, X2_test, y2_train, y2_test = train_test_split(x, y2)
```


```
X3_train, X3_test, y3_train, y3_test = train_test_split(x, y3)
```


```
grid1 = GridSearchCV(tree, tree_params)
grid2 = GridSearchCV(tree, tree_params)
grid3 = GridSearchCV(tree, tree_params)
```


```
grid1.fit(X1_train, y1_train)
print(grid1.score(X1_test, y1_test))
print(grid1.best_params_)
```

    0.3267716774876863
    {'max_depth': 9}
    


```
grid2.fit(X2_train, y2_train)
print(grid2.score(X2_test, y2_test))
print(grid2.best_params_)
```

    0.3479745580676441
    {'max_depth': 9}
    


```
grid3.fit(X3_train, y3_train)
print(grid3.score(X3_test, y3_test))
print(grid3.best_params_)
```

    0.33831420331975026
    {'max_depth': 9}
    


```
a = list(data_dropna.columns)
a.pop(-1)
```




    'yearmonth'




```
a.pop(-6)
```




    '価格'




```
g_data = data_x.dropna(subset=['総評価数'])
y1 = g_data['平均評価']
y2 = g_data['総評価数']
y3 = np.log(g_data['総分数'])
X = g_data.drop(a, axis=1)
```


```
X1_train, X1_test, y1_train, y1_test = train_test_split(X, y1)
X2_train, X2_test, y2_train, y2_test = train_test_split(X, y2)
X3_train, X3_test, y3_train, y3_test = train_test_split(X, y3)
```


```
X3_train['価格'] = X3_train['価格'].fillna(X3_train['価格'].mean())
X3_test['価格'] = X3_test['価格'].fillna(X3_train['価格'].mean())
```

    <ipython-input-201-24e01926719e>:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      X3_train['価格'] = X3_train['価格'].fillna(X3_train['価格'].mean())
    <ipython-input-201-24e01926719e>:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      X3_test['価格'] = X3_test['価格'].fillna(X3_train['価格'].mean())
    


```
grid1 = GridSearchCV(tree, tree_params)
grid2 = GridSearchCV(tree, tree_params)
grid3 = GridSearchCV(tree, tree_params)
```


```
grid1.fit(X1_train, y1_train)
print(grid1.score(X1_test, y1_test))
print(grid1.best_params_)
```


```
grid2.fit(X2_train, y2_train)
print(grid2.score(X2_test, y2_test))
print(grid2.best_params_)
```


```
grid3.fit(X3_train, y3_train)
print(grid3.score(X3_test, y3_test))
print(grid3.best_params_)
```

    0.33247728985988545
    {'max_depth': 9}
    

看来直接删除样本并不是一个很好的做法


```
data_dropna['出演者']
```


```
# x2 = data_dropna['出演者'].str.get_dummies('\n')
x2 = pd.get_dummies(data_dropna[['出演者', '監督']])
```


```
XX = pd.concat([x, x2], axis=1)
y1 = data_dropna['平均評価'].fillna(-999)
y2 = data_dropna['総評価数'].fillna(-999)
y3 = data_dropna['総分数'].fillna(-999)
Xy = pd.concat([x, x2, y1, y2, y3], axis=1)
```


```
jiandu = data_dropna['監督'].value_counts(ascending=False)[1:50].index
meka = data_dropna['メーカー'].value_counts(ascending=False)[1:50].index
nvyou = data_dropna['出演者'].value_counts(ascending=False)[1:50].index
```


```
XX
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>----</th>
      <th>10枚組</th>
      <th>16時間以上作品</th>
      <th>2000年代（DOD）</th>
      <th>2010年代前半（DOD）</th>
      <th>2010年代後半（DOD）</th>
      <th>2020年代前半（DOD）</th>
      <th>3D</th>
      <th>3P・4P</th>
      <th>4時間以上作品</th>
      <th>...</th>
      <th>監督_黒心愛</th>
      <th>監督_黒松繁</th>
      <th>監督_黒田悠斗</th>
      <th>監督_黒谷真人</th>
      <th>監督_黒赤銀蔵</th>
      <th>監督_黒龍武</th>
      <th>監督_龍太</th>
      <th>監督_＆龍</th>
      <th>監督_［Jo］Style</th>
      <th>監督_［不倫］風俗資料考証会</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>45952</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>45953</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>45954</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>45955</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>45956</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>44697 rows × 14276 columns</p>
</div>




```
cols = [*["監督_" + i for i in jiandu], *["出演者_" + i for i in nvyou], '平均評価', '総評価数', '総分数']
```


```
XXX = pd.concat([x, Xy[cols]], axis=1)
```


```
k = 15
cols = XXX.corr()['平均評価'].sort_values(ascending=False).index[:k]

f, ax = plt.subplots(figsize=(15, 15))
hm = sns.heatmap(XXX[cols].corr(), cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 15},
                )
```


![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_100_0.png)



```
k = 15
cols = XXX.corr()['総評価数'].sort_values(ascending=False).index[:k]

f, ax = plt.subplots(figsize=(15, 15))
hm = sns.heatmap(XXX[cols].corr(), cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 15},
                )
```


![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_101_0.png)



```
k = 15
cols = XXX.corr()['総分数'].sort_values(ascending=False).index[:k]

f, ax = plt.subplots(figsize=(15, 15))
hm = sns.heatmap(XXX[cols].corr(), cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 15},
                )
```


![png](dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_files/dmm%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A-01_102_0.png)



```
cols = [*["監督_" + i for i in jiandu], *["出演者_" + i for i in nvyou]]
XX = pd.concat([x, Xy[cols]], axis=1)

X1_train, X1_test, y1_train, y1_test = train_test_split(XX, y1)
X2_train, X2_test, y2_train, y2_test = train_test_split(XX, y2)
X3_train, X3_test, y3_train, y3_test = train_test_split(XX, y3)
```


```
grid1 = GridSearchCV(tree, tree_params)
grid2 = GridSearchCV(tree, tree_params)
grid3 = GridSearchCV(tree, tree_params)
```


```
grid1.fit(X1_train, y1_train)
print(grid1.score(X1_test, y1_test))
print(grid1.best_params_)
```

    0.33458158547350136
    {'max_depth': 9}
    


```
grid2.fit(X2_train, y2_train)
print(grid2.score(X2_test, y2_test))
print(grid2.best_params_)
```

    0.3372253416011918
    {'max_depth': 9}
    


```
grid3.fit(X3_train, y3_train)
print(grid3.score(X3_test, y3_test))
print(grid3.best_params_)
```

    0.34738521038636416
    {'max_depth': 9}
    


```

```
