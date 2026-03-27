'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, PenTool, Palette, Printer, Image as ImageIcon, Loader2 } from 'lucide-react';
import { useUser } from '@clerk/nextjs';
// Our roster of AI Agents
const AGENTS = [
  { id: 0, name: 'The Scout', icon: Search, action: 'Scouring Indian news for headlines...' },
  { id: 1, name: 'The Editor', icon: PenTool, action: 'Writing a biting Hinglish satire...' },
  { id: 2, name: 'The Illustrator', icon: Palette, action: 'Painting the caricature... (takes a moment)' },
  { id: 3, name: 'The Publisher', icon: Printer, action: 'Stamping the punchline on the canvas...' },
];

export default function ComicGenerator() {
  const { user, isSignedIn, isLoaded } = useUser();
  const [isGenerating, setIsGenerating] = useState(false);
  const [currentAgent, setCurrentAgent] = useState(0);
  const [comicUrl, setComicUrl] = useState<string | null>(null);

  // The visual fake progress timer
  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (isGenerating) {
      interval = setInterval(() => {
        setCurrentAgent((prev) => {
          if (prev < 2) return prev + 1; // Hang on the Illustrator until the API actually finishes
          return prev;
        });
      }, 4000);
    }
    return () => clearInterval(interval);
  }, [isGenerating]);

  const generateComic = async () => {
    setIsGenerating(true);
    setCurrentAgent(0);
    setComicUrl(null);

    try {
      // Call your Python FastAPI backend
     const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';
      
      const response = await fetch(`${apiUrl}/generate-comic`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: user?.id || "anonymous" }),
      });

      if (response.status === 429) {
        throw new Error("You've reached your limit of 5 comics for today! Come back tomorrow.");
      }
      if (!response.ok) throw new Error('Failed to generate comic');

      // Move to the final "Publisher" agent step
      setCurrentAgent(3);
      
      const blob = await response.blob();
      const imageUrl = URL.createObjectURL(blob);
      
      // Give the Publisher 1 second to "stamp" before showing the image
      setTimeout(() => {
        setComicUrl(imageUrl);
        setIsGenerating(false);
      }, 1000);

    } catch (error: any) {
      console.error(error);
      // Show the actual error message (e.g., the rate limit warning) or a fallback
      alert(error.message || "Oops! The factory broke down. Make sure your Python server is running!");
      setIsGenerating(false);
    }
  };

  return (
    <div className="w-full max-w-3xl mx-auto flex flex-col items-center">
      
{/* THE START BUTTON */}
      {!isGenerating && !comicUrl && isLoaded && (
        <>
          {isSignedIn ? (
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={generateComic}
              className="bg-gradient-to-r from-orange-500 to-red-600 text-white px-8 py-4 rounded-full font-bold text-xl shadow-[0_0_40px_rgba(234,88,12,0.4)] hover:shadow-[0_0_60px_rgba(234,88,12,0.6)] transition-all flex items-center gap-3"
            >
              <PenTool size={24} />
              Generate Today's Cartoon
            </motion.button>
          ) : (
            <div className="bg-neutral-900 border border-neutral-800 p-6 rounded-2xl text-center max-w-md w-full shadow-xl">
              <h3 className="text-xl font-bold text-white mb-2">Join the Factory</h3>
              <p className="text-neutral-400 mb-0">
                Please sign in using the button in the top right corner to start generating AI satire!
              </p>
            </div>
          )}
        </>
      )}

      {/* THE ANIMATED AGENT TRACKER */}
      {isGenerating && (
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="w-full bg-neutral-900 border border-neutral-800 rounded-2xl p-6 shadow-2xl"
        >
          <div className="flex items-center justify-between mb-6 border-b border-neutral-800 pb-4">
            <h3 className="text-xl font-bold text-white flex items-center gap-2">
              <Loader2 className="animate-spin text-orange-500" />
              Factory Status
            </h3>
            <span className="text-neutral-500 text-sm">Step {currentAgent + 1} of 4</span>
          </div>
          
          <div className="flex flex-col gap-4">
            {AGENTS.map((agent, index) => {
              const isActive = currentAgent === index;
              const isDone = currentAgent > index;
              const Icon = agent.icon;

              return (
                <div key={agent.id} className={`flex items-center gap-4 p-4 rounded-xl transition-all duration-500 ${isActive ? 'bg-neutral-800 border border-neutral-700 shadow-inner' : 'opacity-40'}`}>
                  <div className={`p-3 rounded-full ${isActive ? 'bg-orange-500/20 text-orange-400' : isDone ? 'bg-green-500/20 text-green-400' : 'bg-neutral-800 text-neutral-500'}`}>
                    <Icon size={24} className={isActive ? 'animate-bounce' : ''} />
                  </div>
                  <div className="flex-1">
                    <h4 className={`font-bold text-lg ${isActive ? 'text-white' : 'text-neutral-400'}`}>{agent.name}</h4>
                    <p className="text-sm text-neutral-400">{isDone ? 'Task Complete!' : isActive ? agent.action : 'Waiting in queue...'}</p>
                  </div>
                  {isDone && <span className="text-green-500 font-bold">✓</span>}
                </div>
              );
            })}
          </div>
        </motion.div>
      )}

      {/* THE FINAL REVEAL */}
      <AnimatePresence>
        {comicUrl && !isGenerating && (
          <motion.div 
            initial={{ opacity: 0, scale: 0.8, rotate: -2 }}
            animate={{ opacity: 1, scale: 1, rotate: 1 }}
            className="w-full bg-white p-4 rounded-xl shadow-2xl"
          >
            <img src={comicUrl} alt="AI Generated Comic" className="w-full h-auto rounded-lg border border-neutral-200" />
            
            <div className="mt-6 flex justify-between items-center px-2">
              <button 
                onClick={() => setComicUrl(null)} 
                className="text-neutral-500 hover:text-black font-semibold transition-colors"
              >
                ← Create Another
              </button>
              
              <a 
                href={comicUrl} 
                download="daily_satire.png"
                className="bg-black text-white px-6 py-3 rounded-lg font-bold hover:bg-neutral-800 transition-colors flex items-center gap-2 shadow-lg"
              >
                <ImageIcon size={20} /> Download
              </a>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

    </div>
  );
}