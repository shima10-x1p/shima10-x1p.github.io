import React from 'react';

export const Input = ({ type, placeholder, value, onChange, className }) => {
  return (
    <input
      type={type}
      placeholder={placeholder}
      value={value}
      onChange={onChange}
      className={`border p-2 rounded-xl ${className} text-gray-500 bg-slate-800 border-slate-500 w-full`}
    />
  );
};
