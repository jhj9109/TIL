import React, { useState } from "react";
import AppRouter from "components/Router";
import fbase from "fbase"

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  return (
    <>
	    <AppRouter isLoggedIn={isLoggedIn}/>
      <footer>
        &copy; {new Date().getFullYear()} Jwitter
      </footer>
    </>

  );
}

export default App;