import React from 'react';
import { Button } from '@/components/ui/button';
import { ArrowRight, Download } from 'lucide-react';

export const Home: React.FC = () => {
  const handleGetStarted = () => {
    // Navigate to about section or handle click
    const aboutSection = document.getElementById('about');
    if (aboutSection) {
      aboutSection.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleDownloadCV = () => {
    // Handle CV download
    console.log('Download CV clicked');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Hero Section */}
      <div className="flex items-center justify-center min-h-screen px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl mx-auto text-center">
          {/* Main Heading */}
          <h1 className="text-4xl sm:text-5xl md:text-6xl font-bold text-gray-900 mb-6">
            Hello, I'm{' '}
            <span className="text-blue-600 bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              Your Name
            </span>
          </h1>
          
          {/* Subtitle */}
          <p className="text-xl sm:text-2xl text-gray-600 mb-8 max-w-2xl mx-auto">
            A passionate <strong>Frontend Developer</strong> creating beautiful and functional web experiences
          </p>
          
          {/* Description */}
          <p className="text-lg text-gray-700 mb-12 max-w-3xl mx-auto leading-relaxed">
            I specialize in modern web technologies including React, TypeScript, and Tailwind CSS. 
            I love building user-friendly interfaces that combine great design with seamless functionality.
          </p>
          
          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <Button
              size="lg"
              onClick={handleGetStarted}
              className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 text-lg"
            >
              Get Started
              <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
            
            <Button
              variant="outline"
              size="lg"
              onClick={handleDownloadCV}
              className="border-blue-600 text-blue-600 hover:bg-blue-50 px-8 py-3 text-lg"
            >
              <Download className="mr-2 h-5 w-5" />
              Download CV
            </Button>
          </div>
          
          {/* Skills Badge */}
          <div className="mt-16">
            <p className="text-sm text-gray-500 mb-4">Technologies I work with</p>
            <div className="flex flex-wrap justify-center gap-3">
              {['React', 'TypeScript', 'Tailwind CSS', 'Node.js', 'Next.js', 'Vite'].map((skill) => (
                <span
                  key={skill}
                  className="px-4 py-2 bg-white/60 backdrop-blur-sm rounded-full text-sm font-medium text-gray-700 border border-white/20"
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>
      
      {/* About Section (placeholder) */}
      <div id="about" className="py-20 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl font-bold text-gray-900 mb-6">About Me</h2>
          <p className="text-lg text-gray-700 leading-relaxed">
            This is a sample about section. You can customize this with your own content, 
            experience, and background information.
          </p>
        </div>
      </div>
    </div>
  );
};
