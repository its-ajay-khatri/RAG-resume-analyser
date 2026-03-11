import UploadResume from "./components/UploadResume"
import ResultViewer from "./components/resultViewer"
import { useState } from "react"
import './App.css';

function App() {
  const [result, setResult] = useState("")

  return (
     <div className="app">

      <div className="left-panel">
        <UploadResume setResult={setResult} />
      </div>

      <div className="right-panel">
        <ResultViewer result={result} />
      </div>

    </div>
  )
}

export default App