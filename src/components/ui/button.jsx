import React from 'react';

export const Button = ({ children, onClick, className }) => {
  return (
    <button
      onClick={onClick}
      className={`border border-solid border-slate-500 text-white px-4 py-2 rounded-xl ${className}`}
    >
      {children}
    </button>
  );
};
