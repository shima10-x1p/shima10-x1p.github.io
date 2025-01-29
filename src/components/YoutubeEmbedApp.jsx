import React, { useState } from "react";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { Card, CardContent } from "./ui/card";

const YouTubeEmbedApp = () => {
  const [youtubeUrl, setYoutubeUrl] = useState("");
  const [embedUrl, setEmbedUrl] = useState("");
  const [start, setStart] = useState({ hours: "", minutes: "", seconds: "" });
  const [end, setEnd] = useState({ hours: "", minutes: "", seconds: "" });

  const formatTime = (time) => {
    const { hours, minutes, seconds } = time;
    let totalSeconds = 0;
    if (hours) totalSeconds += parseInt(hours, 10) * 3600;
    if (minutes) totalSeconds += parseInt(minutes, 10) * 60;
    if (seconds) totalSeconds += parseInt(seconds, 10);
    return totalSeconds > 0 ? totalSeconds : "";
  };

  const convertToEmbedUrl = (url) => {
    const regex = /(?:https?:\/\/)?(?:www\.)?youtu(?:\.be|be\.com)\/(?:watch\?v=|embed\/|v\/|live\/)?([^&\n?#]+)(?:[?&].*)?/;
    const match = url.match(regex);
    if (!match) return "";
    let embedUrl = `https://www.youtube.com/embed/${match[1]}`;
    const params = [];
    const startTime = formatTime(start);
    const endTime = formatTime(end);
    if (startTime) params.push(`start=${startTime}`);
    if (endTime) params.push(`end=${endTime}`);
    if (params.length > 0) embedUrl += `?${params.join("&")}`;
    return embedUrl;
  };

  const handleConvert = () => {
    const embed = convertToEmbedUrl(youtubeUrl);
    setEmbedUrl(embed);
  };

  return (
    <div className="flex flex-col items-center py-4 border border-slate-800 rounded-xl my-5 px-3">
      <div className="flex flex-col items-center gap-4 w-full">
        <div className="flex flex-col">
          <Input
            type="text"
            placeholder="YouTubeのURL"
            value={youtubeUrl}
            onChange={(e) => setYoutubeUrl(e.target.value)}
            className="my-4 w-80"
          />
          <div className="flex flex-col gap-4 mb-4">
            <div>
              <h2 className="text-lg mb-2 text-gray-500">開始時間</h2>
              <div className="flex gap-2">
                <Input
                  type="number"
                  placeholder="時"
                  value={start.hours}
                  onChange={(e) => setStart({ ...start, hours: e.target.value })}
                  className="w-24"
                />
                <Input
                  type="number"
                  placeholder="分"
                  value={start.minutes}
                  onChange={(e) => setStart({ ...start, minutes: e.target.value })}
                  className="w-24"
                />
                <Input
                  type="number"
                  placeholder="秒"
                  value={start.seconds}
                  onChange={(e) => setStart({ ...start, seconds: e.target.value })}
                  className="w-24"
                />
              </div>
            </div>
            <div>
              <h2 className="text-lg mb-2 text-gray-500">終了時間</h2>
              <div className="flex gap-2">
                <Input
                  type="number"
                  placeholder="時"
                  value={end.hours}
                  onChange={(e) => setEnd({ ...end, hours: e.target.value })}
                  className="w-24"
                />
                <Input
                  type="number"
                  placeholder="分"
                  value={end.minutes}
                  onChange={(e) => setEnd({ ...end, minutes: e.target.value })}
                  className="w-24"
                />
                <Input
                  type="number"
                  placeholder="秒"
                  value={end.seconds}
                  onChange={(e) => setEnd({ ...end, seconds: e.target.value })}
                  className="w-24"
                />
              </div>
            </div>
          </div>
          <Button onClick={handleConvert} className="mb-4">埋め込みURL作成</Button>
        </div>
        {embedUrl && (
          <div className="flex flex-col items-center w-full">
            <Card className="w-full max-w-2xl">
              <CardContent>
                <iframe
                  src={embedUrl}
                  title="YouTube Video"
                  className="w-full aspect-video"
                  frameBorder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                ></iframe>
              </CardContent>
            </Card>
            <h2 className="text-lg font-medium mb-2 text-gray-500">埋め込みURL</h2>
            <Input
              type="text"
              value={embedUrl}
              readOnly
              className="mb-4 w-96"
            />
          </div>
        )}
      </div>
    </div>
  );
};

export default YouTubeEmbedApp;
