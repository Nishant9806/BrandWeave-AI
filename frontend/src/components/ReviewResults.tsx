import { useState } from 'react'

interface Finding {
  finding_id: string
  category: string
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
  original_text: string
  explanation: string
  suggested_fix: string
  source_type: string
  source_id: string
  status: 'OPEN' | 'ACCEPTED' | 'REJECTED'
  source: 'RULE_ENGINE' | 'AI_ENGINE'
}

const sampleFindings: Finding[] = [
  {
    finding_id: 'finding_001',
    category: 'FACTUAL_ERROR',
    severity: 'HIGH',
    original_text: '48-hour battery life',
    explanation: 'The approved battery life is 24 hours.',
    suggested_fix: '24-hour battery life',
    source_type: 'BRAND_FACT',
    source_id: 'battery_life',
    status: 'OPEN',
    source: 'RULE_ENGINE',
  },
  {
    finding_id: 'finding_002',
    category: 'FACTUAL_ERROR',
    severity: 'HIGH',
    original_text: '₹1,999',
    explanation: 'The approved product price is ₹1,499.',
    suggested_fix: '₹1,499',
    source_type: 'BRAND_FACT',
    source_id: 'price',
    status: 'OPEN',
    source: 'RULE_ENGINE',
  },
  {
    finding_id: 'finding_003',
    category: 'TERMINOLOGY',
    severity: 'MEDIUM',
    original_text: 'Smart Watch Professional',
    explanation: 'Use the officially approved product name.',
    suggested_fix: 'SmartWatch Pro',
    source_type: 'BRAND_TERM',
    source_id: 'Smart Watch Professional',
    status: 'OPEN',
    source: 'RULE_ENGINE',
  },
  {
    finding_id: 'finding_004',
    category: 'UNSUPPORTED_CLAIM',
    severity: 'HIGH',
    original_text: "India's No. 1 smartwatch",
    explanation: 'This superiority claim requires supporting evidence.',
    suggested_fix: 'Remove the claim or provide verifiable evidence.',
    source_type: 'AI_ANALYSIS',
    source_id: 'ai_analysis_001',
    status: 'OPEN',
    source: 'AI_ENGINE',
  },
  {
    finding_id: 'finding_005',
    category: 'UNSUPPORTED_CLAIM',
    severity: 'HIGH',
    original_text: 'Guaranteed to transform your life',
    explanation: 'This guaranteed-benefit claim is not supported by approved brand evidence.',
    suggested_fix: 'Remove or substantiate the claim.',
    source_type: 'AI_ANALYSIS',
    source_id: 'ai_analysis_002',
    status: 'OPEN',
    source: 'AI_ENGINE',
  },
]

interface ReviewResultsProps {
  onBack: () => void
  title: string
}

function ReviewResults({ onBack, title }: ReviewResultsProps) {
  const [findings, setFindings] = useState(sampleFindings)

  const handleDecision = (
    findingId: string,
    decision: 'ACCEPTED' | 'REJECTED'
  ) => {
    setFindings((previous) =>
      previous.map((finding) =>
        finding.finding_id === findingId
          ? { ...finding, status: decision }
          : finding
      )
    )
  }

  const openFindings = findings.filter(
    (finding) => finding.status === 'OPEN'
  )

  const acceptedFindings = findings.filter(
    (finding) => finding.status === 'ACCEPTED'
  )

  const rejectedFindings = findings.filter(
    (finding) => finding.status === 'REJECTED'
  )

  const countSeverity = (severity: Finding['severity']) =>
    findings.filter((finding) => finding.severity === severity).length

  return (
    <div className="review-results-page">

      <div className="results-heading">
        <div>
          <span className="eyebrow">BRAND COMPLIANCE REPORT</span>
          <h1>Review Results</h1>
          <p>{title} · Version 1</p>
        </div>

        <button onClick={onBack}>Back to Submission</button>
      </div>

      <section className="results-summary">

        <div>
          <h3>Review Summary</h3>
          <p>Illustrative review data</p>
        </div>

        <div className="summary-stat">
          <strong>{findings.length}</strong>
          <span>Total Findings</span>
        </div>

        <div className="summary-stat">
          <strong>{countSeverity('CRITICAL')}</strong>
          <span>Critical</span>
        </div>

        <div className="summary-stat">
          <strong>{countSeverity('HIGH')}</strong>
          <span>High</span>
        </div>

        <div className="summary-stat">
          <strong>{countSeverity('MEDIUM')}</strong>
          <span>Medium</span>
        </div>

        <div className="summary-stat">
          <strong>{countSeverity('LOW')}</strong>
          <span>Low</span>
        </div>

      </section>

      <section className="findings-section">

        <div className="findings-heading">
          <div>
            <h2>Detected Findings</h2>
            <p>Review each issue and decide how to address it.</p>
          </div>

          <span>{openFindings.length} Open</span>
        </div>

        {findings.map((finding) => (

          <article className="finding-card" key={finding.finding_id}>

            <div className="finding-header">
              <strong>{finding.category.replaceAll('_', ' ')}</strong>

              <span className={`severity ${finding.severity.toLowerCase()}`}>
                {finding.severity}
              </span>
            </div>

            <div className="finding-body">

              <div>
                <label>Original Text</label>
                <p>{finding.original_text}</p>
              </div>

              <div>
                <label>Explanation</label>
                <p>{finding.explanation}</p>
              </div>

              <div>
                <label>Suggested Correction</label>
                <p>{finding.suggested_fix}</p>
              </div>

              <div>
                <label>Evidence Source</label>
                <p>
                  {finding.source_type} · {finding.source_id}
                </p>
              </div>

              <div>
                <label>Detection Method</label>
                <p>{finding.source === 'RULE_ENGINE' ? 'Deterministic Rule Engine' : 'AI Analysis'}</p>
              </div>

            </div>

            <div className="finding-footer">

              <strong>Status: {finding.status}</strong>

              {finding.status === 'OPEN' && (
                <div>
                  <button
                    onClick={() =>
                      handleDecision(finding.finding_id, 'ACCEPTED')
                    }
                  >
                    Accept Correction
                  </button>

                  <button
                    onClick={() =>
                      handleDecision(finding.finding_id, 'REJECTED')
                    }
                  >
                    Reject
                  </button>
                </div>
              )}

            </div>

          </article>

        ))}

      </section>

      <section className="correction-summary">
        <h3>Correction Decisions</h3>
        <p>Accepted corrections: {acceptedFindings.length}</p>
        <p>Rejected corrections: {rejectedFindings.length}</p>
        <p>Remaining open findings: {openFindings.length}</p>

        <p>
          Accepting a correction does not resolve the finding.
          A new content version and review are required.
        </p>

        <button
          disabled={acceptedFindings.length === 0}
          onClick={() =>
            alert('Correction application will be connected to the backend.')
          }
        >
          Apply Accepted Corrections
        </button>
      </section>

    </div>
  )
}

export default ReviewResults