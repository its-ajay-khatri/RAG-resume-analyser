import axios from "axios"
import { useState } from "react"

function UploadResume({ setResult }) {

  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleUpload = async () => {

    if (!file) return

    const formData = new FormData()
    formData.append("file", file)

    setLoading(true)

    const res = await axios.post(
      `${import.meta.env.VITE_API_URL}/analyze-resume`,
      formData
    )

    setResult(res.data.result)

    setLoading(false)
  }

  return (
    <div className="upload-card">

      <label className="drop-area">

        <input
          type="file"
          accept=".pdf,.png,.jpg,.jpeg"
          onChange={(e) => setFile(e.target.files[0])}
          hidden
        />

        <div>

          <h3>Upload Resume</h3>
          <p>Supports PDF, PNG, JPG</p>

          {file && (
            <p className="file-name">
              {file.name}
            </p>
          )}

        </div>

      </label>

      <button
        className={loading ? "analyze-btn-disabled" : "analyze-btn"}
        onClick={handleUpload}
        disabled={loading}
      >
        {loading ? "Analyzing Resume..." : "Analyze Resume"}
      </button>

    </div>
  )
}

export default UploadResume