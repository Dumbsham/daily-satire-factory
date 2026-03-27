import ComicGenerator from "@/components/ui/ComicGenerator";
import Antigravity from '@/components/Antigravity';

export default function Home() {
  return (
    // 1. The main wrapper needs to take up the full screen height
    <div className="relative min-h-[calc(100vh-80px)] w-full overflow-hidden">
      
      {/* 2. THE BACKGROUND LAYER: Pinned to the back (z-0) */}
      <div className="absolute inset-0 z-0 opacity-60">
        <Antigravity
          count={300}
          magnetRadius={6}
          ringRadius={7}
          waveSpeed={0.4}
          waveAmplitude={1}
          particleSize={1.5}
          lerpSpeed={0.05}
          color="#ea580c" /* Pro-tip: Changed from purple to orange to match your fiery gradient! */
          autoAnimate
          particleVariance={1}
          rotationSpeed={0}
          depthFactor={1}
          pulseSpeed={3}
          particleShape="capsule"
          fieldStrength={10}
        />
      </div>

      {/* 3. THE FOREGROUND LAYER: Brought to the front (z-10) */}
      <div className="relative z-10 flex flex-col items-center justify-center min-h-[calc(100vh-80px)] px-4 py-12 pointer-events-none">
        
        {/* pointer-events-auto allows us to click the text and buttons, while letting 
            mouse movements pass through the empty space to play with the Antigravity background */}
        
        <div className="text-center mb-16 space-y-4 pointer-events-auto">
          <h1 className="text-5xl md:text-7xl font-extrabold text-white tracking-tight">
            The Daily <span className="text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-red-500">Satirist</span>
          </h1>
          <p className="text-neutral-400 text-lg md:text-xl max-w-2xl mx-auto backdrop-blur-sm bg-neutral-950/40 p-3 rounded-2xl">
            An autonomous multi-agent AI factory that turns live Indian political news into single-panel Hinglish comic strips.
          </p>
        </div>
        
        <div className="w-full pointer-events-auto">
          <ComicGenerator />
        </div>

      </div>
    </div>
  );
}