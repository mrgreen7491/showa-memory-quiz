"""
AivisSpeech 音声一括生成スクリプト (Ver.2.1)
==============================================
このスクリプトは、ローカルで起動している AivisSpeech (デフォルト: http://127.0.0.1:10101) を利用して、
「昭和の思い出広場」全30問の問題文、回想問いかけ、および終了メッセージのWAV音声ファイルを一括生成します。

【使用手順】
1. AivisSpeech アプリケーション (C:\\Users\\owners\\AppData\\Local\\Programs\\AivisSpeech\\AivisSpeech.exe) を起動します。
2. ターミナルまたはPowerShellで以下を実行します：
   python generate_audio_aivisspeech.py
3. showa-memory-quiz/audio/ フォルダ内に高品質なWAV音声ファイルが自動保存されます。
4. 音声ファイルが保存されると、ブラウザアプリ側で自動的にその音声が再生されるようになります。
"""

import json
import os
import sys
import urllib.parse
import urllib.request

AIVIS_URL = "http://127.0.0.1:10101"
SPEAKER_ID = 888753760  # AivisSpeech のデフォルトスピーカー (Anneli 等)。未指定時は利用可能な最初のスピーカーを使用

def check_engine_online():
    """AivisSpeech エンジンが稼働中か確認"""
    try:
        req = urllib.request.Request(f"{AIVIS_URL}/version")
        with urllib.request.urlopen(req, timeout=3) as res:
            version = res.read().decode('utf-8')
            print(f"✔ AivisSpeech エンジン接続成功 (バージョン: {version})")
            return True
    except Exception as e:
        print("❌ AivisSpeech エンジンに接続できませんでした。")
        print("   AivisSpeech アプリケーションを起動してから再実行してください。")
        print(f"   詳細: {e}")
        return False

def get_default_speaker():
    """利用可能なスピーカーIDを取得"""
    try:
        req = urllib.request.Request(f"{AIVIS_URL}/speakers")
        with urllib.request.urlopen(req, timeout=3) as res:
            speakers = json.loads(res.read().decode('utf-8'))
            if speakers and len(speakers) > 0:
                first_style = speakers[0]["styles"][0]["id"]
                name = speakers[0]["name"]
                print(f"✔ 使用スピーカー: {name} (スタイルID: {first_style})")
                return first_style
    except Exception:
        pass
    return 0

def synthesize_text(text, speaker_id, output_path):
    """テキストから音声WAVを生成して保存"""
    try:
        # 1. audio_query 生成
        params = urllib.parse.urlencode({"text": text, "speaker": speaker_id})
        query_url = f"{AIVIS_URL}/audio_query?{params}"
        query_req = urllib.request.Request(query_url, method="POST")
        with urllib.request.urlopen(query_req, timeout=10) as res:
            query_data = res.read()

        # 高齢者向けに少しゆっくりめ(0.9)に調整
        query_json = json.loads(query_data.decode('utf-8'))
        query_json["speedScale"] = 0.90
        modified_query = json.dumps(query_json).encode('utf-8')

        # 2. synthesis 合成
        synth_params = urllib.parse.urlencode({"speaker": speaker_id})
        synth_url = f"{AIVIS_URL}/synthesis?{synth_params}"
        synth_req = urllib.request.Request(
            synth_url,
            data=modified_query,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(synth_req, timeout=30) as res:
            wav_data = res.read()

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(wav_data)
        return True
    except Exception as e:
        print(f"  ⚠ 合成エラー: {e}")
        return False

def main():
    print("=== AivisSpeech 音声一括生成ツール ===")
    if not check_engine_online():
        sys.exit(1)

    speaker_id = get_default_speaker()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "quiz_data.json")

    if not os.path.exists(json_path):
        print(f"❌ {json_path} が見つかりません。")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        quiz_data = json.load(f)

    audio_dir = os.path.join(script_dir, "audio")
    os.makedirs(audio_dir, exist_ok=True)

    total_files = len(quiz_data) * 2 + 1
    generated_count = 0

    print(f"\n合計 {total_files} 個の音声ファイルを生成します...")

    # 各問の音声生成
    for item in quiz_data:
        q_id = item["id"]
        # 問題文
        q_file = os.path.join(script_dir, item["audioFiles"]["question"])
        q_script = item["audioScripts"]["questionScript"]
        print(f"[{q_id:02d}/30] 問題文を生成中... -> {os.path.basename(q_file)}")
        if synthesize_text(q_script, speaker_id, q_file):
            generated_count += 1

        # 回想問いかけ
        r_file = os.path.join(script_dir, item["audioFiles"]["reminiscence"])
        r_script = item["audioScripts"]["reminiscenceScript"]
        print(f"[{q_id:02d}/30] 回想問いかけを生成中... -> {os.path.basename(r_file)}")
        if synthesize_text(r_script, speaker_id, r_file):
            generated_count += 1

    # 終了メッセージ
    ending_file = os.path.join(audio_dir, "ending_message.wav")
    ending_script = "昭和の旅、おつかれさまでした。たくさんの懐かしい思い出に出会えましたね。ご参加いただき、心からありがとうございました。高知や四国の懐かしい風景、昭和の暮らしやごちそう、家族やお友達と過ごした温かい記憶がたくさんよみがえってきましたね。今日お話しいただいた一つひとつの思い出や笑顔は、かけがえのない大切な宝物です。ここで一息、温かいお茶でも召し上がりながら、皆さんと今日の余韻をお楽しみください。"
    print(f"[終了] 終了メッセージを生成中... -> {os.path.basename(ending_file)}")
    if synthesize_text(ending_script, speaker_id, ending_file):
        generated_count += 1

    print(f"\n✔ 生成完了: {generated_count} / {total_files} ファイル")
    print(f"保存先: {audio_dir}")

if __name__ == "__main__":
    main()
