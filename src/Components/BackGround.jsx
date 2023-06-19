import { useEffect } from 'react';

const Background = ({ image }) => {
  useEffect(() => {
    document.body.style.backgroundImage = `url(${image})`;
    document.body.style.backgroundSize = 'cover';
    document.body.style.backgroundPosition = 'center center';
    document.body.style.backgroundRepeat = 'no-repeat';

    return () => {
      // Clean up the background image when the component is unmounted
      document.body.style.backgroundImage = 'none';
    };
  }, [image]);

  return null; // The background component doesn't render anything in the UI
};

export default Background;
