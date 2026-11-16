import type {
  HealthResponse,
  ContentSubmissionRequest,
  ContentSubmissionResponse,
  ReviewResponse,
  Finding,
  CorrectionRequest,
  CorrectionResponse,
  DecisionRequest,
  DecisionResponse,
  AnalyticsResponse,
} from '../types/api'

// ==========================================
// BASE API CONFIGURATION
// ==========================================

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'

// ==========================================
// REUSABLE API REQUEST FUNCTION
// ==========================================

interface ApiOptions {
  method?: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'
  body?: unknown
}

export async function apiRequest<T>(
  endpoint: string,
  options: ApiOptions = {}
): Promise<T> {
  const { method = 'GET', body } = options

  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      ...(body !== undefined
        ? { body: JSON.stringify(body) }
        : {}),
    })

    if (!response.ok) {
      let errorMessage = `Request failed with status ${response.status}`

      try {
        const errorData = await response.json()
        errorMessage = errorData.detail || errorMessage
      } catch {
        // Keep default error message.
      }

      throw new Error(errorMessage)
    }

    return await response.json() as T
  } catch (error) {
    if (error instanceof TypeError) {
      throw new Error(
        'Unable to connect to the server. Please check whether the backend is running.'
      )
    }

    throw error
  }
}

// ==========================================
// HEALTH CHECK
// ==========================================

export const checkHealth = () =>
  apiRequest<HealthResponse>('/api/health')

// ==========================================
// BRAND VAULT
// ==========================================

export const getBrand = () =>
  apiRequest('/api/brand')

export const getBrandFacts = () =>
  apiRequest('/api/brand/facts')

export const getBrandTerms = () =>
  apiRequest('/api/brand/terms')

// ==========================================
// CONTENT
// ==========================================

export const createContent = (
  data: ContentSubmissionRequest
) =>
  apiRequest<ContentSubmissionResponse>('/api/content', {
    method: 'POST',
    body: data,
  })

export const getContent = () =>
  apiRequest('/api/content')

export const getContentById = (id: string) =>
  apiRequest(`/api/content/${encodeURIComponent(id)}`)

// ==========================================
// REVIEW
// ==========================================

export const runReview = (submissionId: string) =>
  apiRequest<ReviewResponse>(
    `/api/content/${encodeURIComponent(submissionId)}/review`,
    { method: 'POST' }
  )

export const getFindings = (submissionId: string) =>
  apiRequest<Finding[]>(
    `/api/content/${encodeURIComponent(submissionId)}/findings`
  )

// ==========================================
// CORRECTIONS
// ==========================================

export const applyCorrections = (
  submissionId: string,
  data: CorrectionRequest
) =>
  apiRequest<CorrectionResponse>(
    `/api/content/${encodeURIComponent(submissionId)}/corrections`,
    {
      method: 'POST',
      body: data,
    }
  )

// ==========================================
// APPROVALS
// ==========================================

export const submitDecision = (
  submissionId: string,
  data: DecisionRequest
) =>
  apiRequest<DecisionResponse>(
    `/api/content/${encodeURIComponent(submissionId)}/decision`,
    {
      method: 'POST',
      body: data,
    }
  )

// ==========================================
// HISTORY
// ==========================================

export const getContentHistory = (submissionId: string) =>
  apiRequest(
    `/api/content/${encodeURIComponent(submissionId)}/history`
  )

// ==========================================
// ANALYTICS
// ==========================================

export const getAnalytics = () =>
  apiRequest<AnalyticsResponse>('/api/insights/overview')