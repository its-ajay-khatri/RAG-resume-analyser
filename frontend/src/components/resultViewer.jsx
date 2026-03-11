import ReactMarkdown from "react-markdown"

function ResultViewer({ result }) {

  return (
    <div className="result-card">

      <h2>Resume Analysis</h2>

      {!result ? (
        <p>Upload a resume to see analysis here.</p>
      ) : (
        <ReactMarkdown>
            {result}
        </ReactMarkdown>
      )}

    </div>
  )
}

export default ResultViewer