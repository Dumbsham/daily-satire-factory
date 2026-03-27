'use client';

import { motion } from 'framer-motion';
import { Sparkles } from 'lucide-react';
// 1. Notice we removed SignedIn/SignedOut and added useUser
import { SignInButton, UserButton, useUser } from '@clerk/nextjs';

export default function Navbar() {
  // 2. We ask Clerk directly: "Is the data loaded? Are they signed in?"
  const { isLoaded, isSignedIn } = useUser();

  return (
    <motion.nav 
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      className="sticky top-0 z-50 w-full backdrop-blur-md bg-neutral-950/80 border-b border-neutral-800"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-20">
          
          {/* LOGO SECTION */}
          <div className="flex items-center gap-2 cursor-pointer">
            <motion.div 
              whileHover={{ rotate: 20, scale: 1.1 }}
              className="bg-gradient-to-tr from-orange-500 to-red-500 p-2 rounded-xl"
            >
              <Sparkles className="text-white" size={24} />
            </motion.div>
            <span className="text-white font-extrabold text-2xl tracking-tight">
              DailySatire<span className="text-orange-500">.ai</span>
            </span>
          </div>

          {/* CLERK AUTH BUTTONS */}
          <div className="flex items-center gap-4">
            
            {/* Show nothing while loading to prevent ugly flickering */}
            {isLoaded && !isSignedIn && (
              <SignInButton mode="modal">
                <button className="bg-white text-black px-5 py-2.5 rounded-full font-bold shadow-[0_0_20px_rgba(255,255,255,0.2)] hover:shadow-[0_0_30px_rgba(255,255,255,0.4)] transition-shadow">
                  Sign In
                </button>
              </SignInButton>
            )}
            
            {isLoaded && isSignedIn && (
              <div className="flex items-center gap-4">
                <button className="text-neutral-400 hover:text-white font-medium transition-colors">
                  My Gallery
                </button>
                <UserButton appearance={{ elements: { avatarBox: "w-10 h-10" } }} />
              </div>
            )}
            
          </div>

        </div>
      </div>
    </motion.nav>
  );
}