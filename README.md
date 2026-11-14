# 昭和の思い出広場 Ver.2.1

高知県内のデイサービスやシニアサロン向け・高齢者レクリエーション用ブラウザアプリケーション（Ver.2.1）です。  
外部ライブラリ不要、インストール不要で、ブラウザがあればパソコン・タブレット・スマートフォンのいずれでもオフラインで完全に動作します。

---

## 🌟 Ver.2.1 での主な改善点

1. **3択クイズの正解位置を均等に分散（①:10問、②:10問、③:10問）**
   - 全問が①番になっていた重大な不具合を完全修正。①②③が各10回ずつ均等に正解となり、同じ番号が3回以上連続しないよう配慮しました。
2. **スタッフ読み上げガイド（ルビ付き原稿）機能の新設**
   - 合成音声の読み間違い（「はりまや橋」「高知城」など）を防ぐため、音声ファイル未配置時は低品質な音声を鳴らさず、スタッフが温かく自然な肉声で読み上げられる「📖 スタッフ読み上げガイド（ふりがな・抑揚ヒント付き）」を画面上にワンタッチ表示できるように改善しました。
3. **AivisSpeech による高品質音声一括生成への対応**
   - お手元のパソコンにインストールされている AivisSpeech (ポート10101) を利用して、全30問分のWAV音声ファイルを一括生成できるツール `generate_audio_aivisspeech.py` を用意しました。
   - 生成されたWAVファイルを配置すると、アプリ側が自動検知して高品質な音声再生に切り替わります。
4. **全30問の画像生成用プロンプト・推奨ファイル名カタログの完備**
   - 回答後の視覚的な回想を促すため、全30問について「題材」「必要な画像の内容」「推奨ファイル名」「画像生成用プロンプト」を完全に定義・構造化しました。
   - 第1問（はりまや橋）および第6問（昭和歌謡ステージ）には実画像が配置されています。

---

## 📂 ファイル構成

```
showa-memory-quiz/
├── audio/                     # AivisSpeechで一括生成したWAV音声の配置先
├── images/
│   ├── q01_harimayabashi.jpg  # 第1問 はりまや橋（実画像）
│   └── showa-kayo-singer.png  # 第6問 昭和歌謡ステージ（AIイラスト）
├── generate_audio_aivisspeech.py # AivisSpeech音声一括生成スクリプト
├── quiz_data.json             # 全30問の完全データ（読み原稿・ルビ・プロンプト定義）
├── index.html                 # アプリケーション本体（Ver.2.1 UI）
├── style.css                  # 昭和レトロ配色・高視認性スタイル・レスポンシブ
├── script.js                  # クイズロジック・効果音・スタッフガイド・音声再生
└── README.md                  # 取扱説明書・スタッフ用ガイド・画像カタログ
```

※作業前のバックアップ：
- Ver.1 一式：`showa-memory-quiz-v1-backup/`
- Ver.2 一式：`showa-memory-quiz-v2-backup/`

---

## 📊 全30問の正解番号・選択肢一覧（①②③の分布）

| 第 | ジャンル | 正解番号 | 正解の選択肢 | 選択肢① | 選択肢② | 選択肢③ |
|:---:|:---|:---:|:---|:---|:---|:---|
| 1 | 高知・名所 | **②** | はりまや橋 | めがね橋 | **はりまや橋** | 錦帯橋（きんたいきょう） |
| 2 | 高知・お城 | **③** | 高知城（鷹城） | 松山城 | 丸亀城 | **高知城（鷹城）** |
| 3 | 高知・街の風景 | **①** | 日曜市（にちよういち） | **日曜市（にちよういち）** | 朝市 | 蚤の市（のみのいち） |
| 4 | 高知・伝統祭り | **②** | よさこい祭り | 阿波おどり | **よさこい祭り** | 新居浜太鼓祭り |
| 5 | 高知・名勝海岸 | **③** | 桂浜（かつらはま） | 室戸岬（むろとみさき） | 足摺岬（あしずりみさき） | **桂浜（かつらはま）** |
| 6 | 昭和歌謡・名曲 | **①** | リンゴ追分（おいわけ） | **リンゴ追分（おいわけ）** | 瀬戸の花嫁 | 青い山脈 |
| 7 | 高知・歴史の英雄 | **③** | 坂本龍馬 | 板垣退助 | 中岡慎太郎 | **坂本龍馬** |
| 8 | 高知・清流 | **②** | 四万十川（しまんとがわ） | 仁淀川（によどがわ） | **四万十川（しまんとがわ）** | 吉野川 |
| 9 | 高知・郷土の味 | **①** | 皿鉢（さわち）料理 | **皿鉢（さわち）料理** | しっぽく料理 | 会席料理 |
| 10 | 高知・懐かしの味 | **③** | ぼうしパン | コッペパン | あんパン | **ぼうしパン** |
| 11 | 高知・路面電車 | **②** | とさでん交通（路面電車） | モノレール | **とさでん交通（路面電車）** | ケーブルカー |
| 12 | 四国・徳島伝統 | **①** | 阿波おどり | **阿波おどり** | 花笠音頭 | ソーラン節 |
| 13 | 四国・香川名物 | **②** | 讃岐うどん | 祖谷（いや）そば | **讃岐うどん** | そうめん |
| 14 | 四国・愛媛名湯 | **①** | 道後温泉（どうごおんせん） | **道後温泉（どうごおんせん）** | 別府温泉 | 有馬温泉 |
| 15 | 高知・ふるさとの果物 | **③** | 土佐文旦（ぶんたん） | 温州みかん | リンゴ | **土佐文旦（ぶんたん）** |
| 16 | 昭和家電・暮らし | **①** | 電気冷蔵庫 | **電気冷蔵庫** | 電子レンジ | エアコン（クーラー） |
| 17 | 懐かしのおやつ | **③** | ラムネ | サイダー | 麦茶 | **ラムネ** |
| 18 | 子どもの外遊び | **②** | けんけんぱ | かくれんぼ | **けんけんぱ** | だるまさんがころんだ |
| 19 | 昭和テレビ・ヒーロー | **③** | 仮面ライダー | 月光仮面 | ウルトラマン | **仮面ライダー** |
| 20 | 懐かしの学校給食 | **①** | あげパン | **あげパン** | あんパン | メロンパン |
| 21 | 昭和の暖房・道具 | **②** | 湯たんぽ（ゆたんぽ） | 火鉢（ひばち） | **湯たんぽ（ゆたんぽ）** | 豆炭こたつ |
| 22 | 街の社交場 | **①** | 駄菓子屋（だがしや）さん | **駄菓子屋（だがしや）さん** | 文房具屋さん | よろず屋さん |
| 23 | 昭和の音楽・レコード | **②** | レコード | カセットテープ | **レコード** | ソノシート |
| 24 | 街角の娯楽・紙芝居 | **③** | 紙芝居（かみしばい） | 人形劇 | 幻灯機（げんとうき） | **紙芝居（かみしばい）** |
| 25 | 昭和の乗り物 | **②** | オート三輪（ミゼットなど） | リヤカー | **オート三輪（ミゼットなど）** | 軽トラック |
| 26 | 昭和の通信・道具 | **③** | 黒電話（ダイヤル式） | プッシュホン | 糸電話 | **黒電話（ダイヤル式）** |
| 27 | 夏の風物詩・暮らし | **①** | 蚊帳（かや） | **蚊帳（かや）** | すだれ | のれん |
| 28 | 昭和の大ブーム | **③** | フラフープ | ホッピング | ダッコちゃん | **フラフープ** |
| 29 | 昭和のシンボル | **①** | 東京タワー | **東京タワー** | 通天閣（つうてんかく） | 京都タワー |
| 30 | 四国・自然の恵み | **②** | 鳴門の渦潮（なるとのうずしお） | 潮岬の白波 | **鳴門の渦潮（なるとのうずしお）** | 室戸の三角波 |

**【正解番号の集計結果】**
- **① 番が正解の問題**：10問（第3, 6, 9, 12, 14, 16, 20, 22, 27, 29問）
- **② 番が正解の問題**：10問（第1, 4, 8, 11, 13, 18, 21, 23, 25, 30問）
- **③ 番が正解の問題**：10問（第2, 5, 7, 10, 15, 17, 19, 24, 26, 28問）
- ※同じ番号の3連続はなく、バランス良く分散されています。

---

## 🎙️ 音声機能の使い方と AivisSpeech による一括生成

### 基本運用（スタッフによる肉声読み上げ）
- デフォルトでは、機械的な誤読を防ぐため音声は自動再生されません。
- 画面上の「📖 問題の読み上げ原稿」や「🗣️ 問いかけの言葉」を押すと、ふりがな付きのスタッフ用読み原稿カードが画面に表示されます。
- スタッフの方が参加者の表情を見ながら、温かい声で直接語りかける運用を推奨します。

### AivisSpeech による音声一括生成手順
お手元の環境にインストールされている AivisSpeech を使って、全音声をまとめて作成できます。
1. **AivisSpeech を起動します**  
   （`C:\Users\owners\AppData\Local\Programs\AivisSpeech\AivisSpeech.exe`）
2. **スクリプトを実行します**  
   ターミナルまたはPowerShellで以下を実行：
   ```powershell
   cd showa-memory-quiz
   python generate_audio_aivisspeech.py
   ```
3. `showa-memory-quiz/audio/` 内に全30問分の問題文・回想問いかけ・終了メッセージ（全61ファイル）のWAV音声が自動生成されます。
4. 生成後は、アプリのボタンを押すだけで高品質なナレーション音声が再生されるようになります。

---

## 🖼 全30問の画像生成用プロンプト・推奨ファイル名カタログ

現在、高知の代表的な名所・名物・昭和文化を中心に **7問の実画像** を配置済みです。  
残りの未作成問題（23問）については、画像生成API（gemini-3.1-flash-image）のクォータ上限エラーに伴い、正確に未作成と明記しております。画像を後から追加する際は、下表の「推奨ファイル名」で `showa-memory-quiz/images/` フォルダ内に保存してください。配置すると自動的に回答画面に表示されます（画像がない問題では画面は一切崩れません）。

| 問 | 題材 | 状態 | 推奨ファイル名 | 必要な画像の内容 | 画像生成用プロンプト |
|:---:|:---|:---:|:---|:---|:---|
| 1 | はりまや橋 | **実画像あり** | `q01_harimayabashi.jpg` | 朱塗りの太鼓橋と柳、昭和レトロな街並み | Showa retro style watercolor illustration of Harimayabashi bridge in Kochi Japan, vermilion curved bridge with willows, nostalgic 1960s atmosphere, warm colors, daylight |
| 2 | 高知城 | **実画像あり** | `q02_kochijo.jpg` | 青空に映える木造の天守閣と追手門 | A nostalgic retro watercolor illustration of Kochi Castle (Kochi-jo) keep and Otemon gate in Japan, traditional Japanese castle architecture, blue sky, blooming cherry blossoms, gentle warm tones, 1960s Showa style |
| 3 | 日曜市 | **実画像あり** | `q03_nichiyoichi.jpg` | 追手筋に白いテントが連なる市と、いも天・人々 | Nostalgic Showa era open-air street market in Kochi Japan, Nichiyo-ichi Sunday market, white sunshades along street with castle in background, lively elderly people and vendors selling vegetables and fried sweet potato tempura, warm watercolor art |
| 4 | よさこい祭り | **実画像あり** | `q04_yosakoi.jpg` | ハッピを着て鳴子を持って踊る笑顔の人々 | Retro 1960s Showa illustration of Kochi Yosakoi festival dancers, vibrant traditional happi coats, holding wooden naruko clappers, energetic smiling people dancing on street, festive summer mood, nostalgic warm color palette |
| 5 | 桂浜 | **実画像あり** | `q05_katsurahama.jpg` | 白砂青松の海岸、太平洋と坂本龍馬像 | Scenic retro watercolor illustration of Katsurahama beach in Kochi Japan, majestic bronze statue of Sakamoto Ryoma gazing at the Pacific ocean, pine trees, sandy beach with rolling waves, nostalgic Showa era travel postcard aesthetic |
| 6 | 美空ひばり | **実画像あり** | `showa-kayo-singer.png` | 昭和歌謡のステージをイメージしたAIイラスト | Showa retro stage singer singing with vintage microphone, theater curtains, elegant dress, warm spotlight, 1950s aesthetic |
| 7 | 坂本龍馬 | 未配置 | `q07_ryoma.png` | 懐に手を入れて遠くを見つめる若き龍馬の肖像 | Portrait of Sakamoto Ryoma in warm retro ink and watercolor illustration style, traditional Japanese samurai hakama with western leather boots, hand inside kimono robe, charismatic gentle smile, nostalgic sepia and soft colors |
| 8 | 四万十川 | 未配置 | `q08_shimantogawa.png` | 清流とコンクリートの沈下橋、渡る自転車 | Peaceful nostalgic Japanese countryside landscape of Shimanto River in Kochi, low-water chinkabashi submersible bridge crossing clear river, lush green mountains, someone walking with a bicycle, warm summer breeze, Showa watercolor painting |
| 9 | 皿鉢料理 | 未配置 | `q09_sawachi.png` | 大皿に盛られたカツオのタタキやお寿司のごちそう | Sumptuous traditional Kochi Sawachi ryori banquet platter, huge decorative ceramic plate heaped with seared bonito katsuo tataki, sushi rolls, sea bream, and festive appetizers, warm tatami room setting, retro Showa gourmet illustration |
| 10 | ぼうしパン | **実画像あり** | `q10_boushipan.jpg` | 麦わら帽子の形をした甘いカステラのフチつきパン | Cute retro bakery illustration of Kochi's famous Boushi-pan hat bread, golden-brown sweet bun shaped like a straw hat with a crispy castella rim, old-fashioned Japanese bakery showcase, warm cozy nostalgic atmosphere |
| 11 | とさでん交通 | 未配置 | `q11_tosaden.png` | 緑とクリーム色のレトロな路面電車 | Classic vintage streetcar tram of Tosaden running on Kochi city streets, green and cream vintage tramcar, nostalgic Showa era townscape with shop signs, passengers waiting at platform, gentle retro watercolor art |
| 12 | 阿波おどり | 未配置 | `q12_awaodori.png` | 編笠の女踊りと提灯明かりの下で踊る人々 | Festive illustration of Tokushima Awa Odori dancers in Showa era, female dancers wearing woven amigasa hats and yukata dancing gracefully, paper lanterns glowing at night, vibrant energetic festival mood, retro Japanese woodblock inspired watercolor |
| 13 | 讃岐うどん | 未配置 | `q13_sanukiudon.png` | 湯気の立つコシの強いうどんとネギ・生姜 | Mouthwatering nostalgic illustration of a bowl of Sanuki udon noodles in Kagawa, thick chewy white noodles in clear golden dashi broth, green onions and grated ginger, rustic ceramic bowl on wooden table, warm comforting Showa vibe |
| 14 | 道後温泉 | 未配置 | `q14_dogoonsen.png` | 木造三層楼の本館と振鷺閣、浴衣で歩く人々 | Nostalgic retro illustration of historic Dogo Onsen Honkan bathhouse in Ehime Matsuyama, multi-story wooden traditional bathhouse architecture, Shinrokaku tower on roof, people in yukata strolling with towels, dusk lighting, warm Showa postcard style |
| 15 | 土佐文旦 | 未配置 | `q15_buntan.png` | 縁側に置かれた黄色い大玉の文旦とむいた果肉 | Still life retro watercolor of ripe Tosa Buntan citrus fruit in Kochi, large yellow pomelo fruit in bamboo basket, some peeled showing translucent juicy segments, sitting on engawa veranda in spring sunlight, nostalgic warmth |
| 16 | 三種の神器 | 未配置 | `q16_reizo-ko.png` | 昭和30年代の白い1ドア電気冷蔵庫と家族 | Vintage 1950s Showa kitchen with a round-edged white electric refrigerator, silver latch handle, happy family opening it to take out chilled watermelon, nostalgic Japanese dining room, warm retro illustration |
| 17 | ラムネ | 未配置 | `q17_ramune.png` | 氷水に浮かぶビー玉入りのガラス瓶ラムネ | Refreshing Showa summer illustration of glass Codd-neck Ramune bottle with marble inside, floating in galvanized tub filled with clear cold water and ice blocks, water droplets on bottle, wooden veranda background, nostalgic summer heat |
| 18 | けんけんぱ | 未配置 | `q18_kenkenpa.png` | 地面に石でマスを描いて跳ぶ子どもたち | Nostalgic 1960s scene of Japanese children playing hopscotch (ken-ken-pa) on dirt lane, white chalk circles drawn on ground, children wearing retro clothes hopping happily, neighborhood alleys with wooden houses, gentle sunset glow |
| 19 | 仮面ライダー | 未配置 | `q19_kamenrider.png` | 赤いマフラーをなびかせてバイクに乗るヒーロー | Retro 1970s Japanese tokusatsu hero with grasshopper mask and red scarf fluttering in the wind, riding a futuristic motorcycle on coastal road, dramatic hero pose, vintage Showa manga and TV art style |
| 20 | あげパン | 未配置 | `q20_agepan.png` | アルマイト皿に載った砂糖たっぷりの揚げパン | Classic nostalgic Japanese school lunch from Showa era, golden fried bread (age-pan) coated with sugar on an aluminum tray, triangle milk carton, wooden school desk in sunlit classroom, warm nostalgic memories |
| 21 | 湯たんぽ | 未配置 | `q21_yutanpo.png` | 波打つトタン製の湯たんぽとお湯を注ぐヤカン | Cozy retro Showa winter scene of an oval corrugated galvanized metal hot water bottle (yutanpo), pouring steaming water from vintage kettle, wrapping in soft cloth bag, placed inside heavy futon quilts, warm tatami room |
| 22 | 駄菓子屋 | 未配置 | `q22_dagashiya.png` | 地球瓶にお菓子が並び10円玉を持つ子どもたち | Charming nostalgic Showa era Japanese candy store (dagashiya), glass jars filled with colorful treats, hanging lottery prizes, vintage advertisements on wooden walls, elderly shopkeeper smiling at children with 10-yen coins, warm golden hour lighting |
| 23 | レコード | 未配置 | `q23_record.png` | ステレオのターンテーブルで針が落ちる黒いLP盤 | Vintage Showa stereo turntable playing a black vinyl LP record, delicate needle on vinyl grooves, warm wooden audio cabinet, cozy living room with soft lighting, timeless nostalgic musical atmosphere |
| 24 | 紙芝居 | 未配置 | `q24_kamishibai.png` | 自転車の荷台の舞台で語るおじさんと子どもたち | Heartwarming 1950s Showa illustration of a traveling paper theater (kamishibai) storyteller on a bicycle, wooden stage box mounted on bike rack, enthusiastic children gathered around eating candy syrup, nostalgic neighborhood vacant lot |
| 25 | オート三輪 | 未配置 | `q25_autosanrin.png` | 荷物を積んで狭い路地を走る3輪トラック | Vintage three-wheeled pickup truck (auto-sanrin midget) driving down a Showa era shopping street, carrying wooden crates and vegetables, round headlights, old wooden merchant houses with retro signs, warm cheerful nostalgic watercolor |
| 26 | 黒電話 | 未配置 | `q26_kurodenwa.png` | レースの敷物に載った重厚なダイヤル式黒電話 | Nostalgic heavy rotary dial black telephone (kuro-denwa) on a polished wooden stand, white lace doily underneath, coiled cord, thick telephone directory book nearby, cozy hallway of a traditional Showa Japanese home |
| 27 | 蚊帳 | 未配置 | `q27_kaya.png` | 和室に吊るされた緑の網と蚊取り線香の煙 | Peaceful summer night in Showa Japan, pale green mesh mosquito net (kaya) hung in tatami room, futons laid out inside, coil incense burning outside emitting gentle curl of fragrant smoke, paper screen sliding doors open to night breeze |
| 28 | フラフープ | 未配置 | `q28_hulahoop.png` | 公園で腰で輪を回して楽しむ人々 | Lively 1958 Showa scene of a girl spinning a colorful plastic hula hoop around her waist in a park, friends and mothers clapping and laughing, retro dresses and hairstyles, sunny cheerful retro Japanese illustration |
| 29 | 東京タワー | 未配置 | `q29_tokyotower.png` | 青空にそびえ立つ昭和33年完成当時の赤い塔 | Iconic red and white Tokyo Tower rising proudly into crisp blue sky in 1958, low-rise Showa period wooden and tiled houses below, streetcar passing in foreground, bright hopeful atmosphere, nostalgic retro postcard style |
| 30 | 鳴門の渦潮 | 未配置 | `q30_naruto.png` | 海原に激しく渦巻く大渦と観潮船 | Dramatic panoramic illustration of the giant Naruto whirlpools in Shikoku, swirling white foam and deep blue sea currents, a sightseeing cruise ship navigating nearby, distant green coastline, classic Showa travel poster art style |
