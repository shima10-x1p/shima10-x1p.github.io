import React from 'react';

export const Card = ({ children, className }) => {
  return (
    <div className={`shadow-md p-4 rounded ${className}`}>
      {children}
    </div>
  );
};

export const CardContent = ({ children }) => {
  return <div className="p-2">{children}</div>;
};
