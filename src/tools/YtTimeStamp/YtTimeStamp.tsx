import { useState } from "react";
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from "../../components/ui/card";
import { Input } from "../../components/ui/input";
import { Button } from "../../components/ui/button";
import Navbar from "../../components/custom/Navbar";

export default function YtTimeStamp() {
  const [videoUrl, setVideoUrl] = useState("");
  const [hours, setHours] = useState("");
  const [minutes, setMinutes] = useState("");
  const [seconds, setSeconds] = useState("");
  const [generatedUrl, setGeneratedUrl] = useState("");

  const generateTimestampUrl = () => {
    try {
      const url = new URL(videoUrl);
      if (!url.hostname.includes("youtube.com") && !url.hostname.includes("youtu.be")) {
        alert("YouTubeのURLを入力してください。");
        return;
      }

      const totalSeconds = (parseInt(hours) || 0) * 3600 + (parseInt(minutes) || 0) * 60 + (parseInt(seconds) || 0);
      if (totalSeconds <= 0) {
        alert("有効な時間を入力してください。");
        return;
      }

      if (url.hostname.includes("youtu.be")) {
        // 短縮URLの場合
        setGeneratedUrl(`${url.href}?t=${totalSeconds}s`);
      } else {
        // 通常のURLの場合
        url.searchParams.set("t", `${totalSeconds}s`);
        setGeneratedUrl(url.href);
      }
    } catch (error) {
      alert("無効なURLです。");
    }
  };

  const copyToClipboard = async () => {
    if (!generatedUrl) return;
    try {
      await navigator.clipboard.writeText(generatedUrl);
      alert("コピーしました！");
    } catch (error) {
      alert("コピーに失敗しました。");
    }
  };

  return (
    <>
      <Navbar />
      <h1 className='text-2xl font-bold mb-5 text-center text-slate-500'>YouTubeリンクにタイムスタンプつけるやつ (GPT-4o)</h1>
      <Card className="max-w-md mx-auto">
        <CardHeader>
          <CardTitle className="text-slate-500">YouTube タイムスタンプ生成</CardTitle>
        </CardHeader>
        <CardContent>
          <Input
            type="text"
            placeholder="YouTubeのURLを入力"
            value={videoUrl}
            onChange={(e) => setVideoUrl(e.target.value)}
            className="mb-2"
          />
          <div className="flex gap-2 mb-2">
            <Input
              type="number"
              placeholder="時"
              value={hours}
              onChange={(e) => setHours(e.target.value)}
              className="w-1/3"
            />
            <Input
              type="number"
              placeholder="分"
              value={minutes}
              onChange={(e) => setMinutes(e.target.value)}
              className="w-1/3"
            />
            <Input
              type="number"
              placeholder="秒"
              value={seconds}
              onChange={(e) => setSeconds(e.target.value)}
              className="w-1/3"
            />
          </div>
          <Button
            onClick={generateTimestampUrl}
            className="w-full mb-2 text-slate-500" variant="outline"
          >
            生成
          </Button>
          {generatedUrl && (
            <div className="p-2 border rounded bg-slate-800 flex flex-col items-center">
              <p className="break-all text-sm">{generatedUrl}</p>
              <Button
                onClick={copyToClipboard}
                className="mt-2 text-slate-500"
              >
                コピー
              </Button>
            </div>
          )}
        </CardContent>
        <CardFooter>
          <p className="text-sm text-slate-500">YouTubeのURLとタイムスタンプを入力してください。</p>
        </CardFooter>
      </Card>
      <Button asChild variant="outline" size="lg" className='mt-10'>
        <a className='text-slate-500' href="/#/tools">戻る</a>
      </Button>
    </>
  );
}
