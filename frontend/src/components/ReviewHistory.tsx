const reviewHistory = [
  {
    id: 'REV-001',
    title: 'SmartWatch Pro Instagram Advertisement',
    type: 'SOCIAL_POST',
    date: '14 Nov 2026',
    status: 'NEEDS_CHANGES',
    findings: 3,
  },
  {
    id: 'REV-002',
    title: 'SmartWatch Pro Product Launch Campaign',
    type: 'ADVERTISEMENT',
    date: '13 Nov 2026',
    status: 'APPROVED',
    findings: 0,
  },
  {
    id: 'REV-003',
    title: 'Website Product Description',
    type: 'WEBSITE_COPY',
    date: '12 Nov 2026',
    status: 'NEEDS_CHANGES',
    findings: 2,
  },
]

function ReviewHistory() {
  return (
    <div className="review-history-page">
      <div className="page-heading">
        <div>
          <h1>Review History</h1>
          <p>View previously submitted content and its review status.</p>
        </div>
      </div>

      <div className="history-table-wrapper">
        <table className="history-table">
          <thead>
            <tr>
              <th>Review ID</th>
              <th>Content</th>
              <th>Type</th>
              <th>Date</th>
              <th>Findings</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {reviewHistory.map((review) => (
              <tr key={review.id}>
                <td>{review.id}</td>
                <td>{review.title}</td>
                <td>{review.type.replace('_', ' ')}</td>
                <td>{review.date}</td>
                <td>{review.findings}</td>
                <td>
                  <span className={`history-status ${review.status.toLowerCase()}`}>
                    {review.status.replace('_', ' ')}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <p className="demo-note">
        These are illustrative records for the frontend demo. Actual review
        history will come from the backend.
      </p>
    </div>
  )
}

export default ReviewHistory