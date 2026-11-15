const pendingApprovals = [
  {
    id: 'APR-001',
    title: 'SmartWatch Pro Instagram Campaign',
    submittedBy: 'Content Creator',
    date: '14 Nov 2026',
    findings: 2,
    status: 'PENDING',
  },
  {
    id: 'APR-002',
    title: 'Product Launch Advertisement',
    submittedBy: 'Marketing Team',
    date: '13 Nov 2026',
    findings: 0,
    status: 'PENDING',
  },
]

function Approvals() {
  const handleDecision = (title: string, decision: string) => {
    alert(`"${title}" marked as ${decision}. Demo action only.`)
  }

  return (
    <div className="approvals-page">
      <div className="page-heading">
        <div>
          <h1>Approvals</h1>
          <p>Review content and make final publishing decisions.</p>
        </div>
      </div>

      <div className="approval-list">
        {pendingApprovals.map((item) => (
          <div className="approval-card" key={item.id}>
            <div>
              <h3>{item.title}</h3>
              <p>Submitted by: {item.submittedBy}</p>
              <p>Submission date: {item.date}</p>
              <p>Findings: {item.findings}</p>
              <span className="approval-pending">{item.status}</span>
            </div>

            <div className="approval-actions">
              <button
                onClick={() => handleDecision(item.title, 'APPROVED')}
              >
                Approve
              </button>

              <button
                className="request-changes-button"
                onClick={() => handleDecision(item.title, 'CHANGES REQUESTED')}
              >
                Request Changes
              </button>
            </div>
          </div>
        ))}
      </div>

      <p className="demo-note">
        These are illustrative approval records. Actual approval decisions
        will be saved through the backend.
      </p>
    </div>
  )
}

export default Approvals