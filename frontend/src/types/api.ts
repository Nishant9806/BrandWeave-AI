// ==========================================
// COMMON TYPES
// ==========================================

export type ContentType =
  | 'SOCIAL_POST'
  | 'ADVERTISEMENT'
  | 'WEBSITE_COPY'
  | 'EMAIL'
  | 'BLOG'

export type FindingCategory =
  | 'FACTUAL_ERROR'
  | 'TERMINOLOGY'
  | 'TONE'
  | 'UNSUPPORTED_CLAIM'
  | 'ACCESSIBILITY'

export type FindingSeverity =
  | 'LOW'
  | 'MEDIUM'
  | 'HIGH'
  | 'CRITICAL'

export type FindingStatus =
  | 'OPEN'
  | 'ACCEPTED'
  | 'REJECTED'
  | 'RESOLVED'
  | 'DISPUTED'

export type DecisionType =
  | 'APPROVED'
  | 'REJECTED'
  | 'CHANGES_REQUESTED'

// ==========================================
// HEALTH CHECK
// ==========================================

export interface HealthResponse {
  status: string
  service: string
}

// ==========================================
// CONTENT SUBMISSION
// ==========================================

export interface ContentSubmissionRequest {
  title: string
  content_type: ContentType
  content: string
}

export interface ContentSubmissionResponse {
  submission_id: string
  version: number
  status: string
}

// ==========================================
// FINDINGS
// ==========================================

export interface Finding {
  finding_id: string
  review_id: string
  category: FindingCategory
  severity: FindingSeverity
  confidence: number
  original_text: string
  explanation: string
  suggested_fix: string
  source_type: string
  source_id: string
  status: FindingStatus
}

// ==========================================
// REVIEW
// ==========================================

export interface ReviewResponse {
  submission_id: string
  version_id: string
  review_id: string
  status: 'COMPLETED' | 'FAILED'
  total_findings: number
  findings: Finding[]
}

// ==========================================
// CORRECTIONS
// ==========================================

export interface CorrectionItem {
  finding_id: string
  replacement_text: string
}

export interface CorrectionRequest {
  version_id: string
  corrections: CorrectionItem[]
}

export interface CorrectionResponse {
  submission_id: string
  new_version_id: string
  version_number: number
  status: string
  message: string
}

// ==========================================
// APPROVAL DECISION
// ==========================================

export interface DecisionRequest {
  version_id: string
  decision: DecisionType
  comment: string
}

export interface DecisionResponse {
  submission_id: string
  version_id: string
  decision: DecisionType
  message: string
}

// ==========================================
// ANALYTICS
// ==========================================

export interface AnalyticsResponse {
  total_submissions: number
  approved: number
  pending: number
  changes_requested: number
  total_findings: number
}

// ==========================================
// API ERROR
// ==========================================

export interface ApiError {
  detail: string
}