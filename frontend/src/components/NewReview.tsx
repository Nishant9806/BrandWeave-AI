import { useState, type FormEvent } from 'react'

interface NewReviewProps {
  onBack: () => void
  onSubmit: (data: {
    title: string
    content_type: string
    content: string
  }) => void | Promise<void>
}

function NewReview({ onBack, onSubmit }: NewReviewProps) {
  const [title, setTitle] = useState('')
  const [contentType, setContentType] = useState('SOCIAL_POST')
  const [content, setContent] = useState('')

  const [errors, setErrors] = useState({
    title: '',
    content: '',
  })

  const [isSubmitting, setIsSubmitting] = useState(false)
  const [submitError, setSubmitError] = useState('')

  const wordCount = content.trim()
    ? content.trim().split(/\s+/).length
    : 0

  const validateForm = () => {
    const newErrors = {
      title: '',
      content: '',
    }

    if (!title.trim()) {
      newErrors.title = 'Please enter a content title.'
    }

    if (!content.trim()) {
      newErrors.content = 'Please enter the content you want to review.'
    }

    setErrors(newErrors)

    return !newErrors.title && !newErrors.content
  }

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault()

    if (isSubmitting) return

    setSubmitError('')

    if (!validateForm()) return

    setIsSubmitting(true)

    try {
      await onSubmit({
        title: title.trim(),
        content_type: contentType,
        content: content.trim(),
      })
    } catch (error) {
      setSubmitError(
        error instanceof Error
          ? error.message
          : 'Something went wrong. Please try again.'
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="review-page">

      <div className="review-heading">
        <div>
          <span className="eyebrow">CONTENT GOVERNANCE</span>
          <h1>New Content Review</h1>
          <p>
            Submit your content to check whether it follows
            TechNova's brand guidelines.
          </p>
        </div>
      </div>

      <form onSubmit={handleSubmit}>

        <div className="review-form-panel">

          <div className="form-section-heading">
            <h3>Content Details</h3>
            <p>Provide basic information about your submission.</p>
          </div>

          <div className="form-group">
            <label htmlFor="title">Content Title</label>

            <input
              id="title"
              type="text"
              placeholder="e.g. SmartWatch Pro Launch Campaign"
              value={title}
              onChange={(event) => {
                setTitle(event.target.value)
                setErrors((previous) => ({
                  ...previous,
                  title: '',
                }))
              }}
              disabled={isSubmitting}
            />

            {errors.title && (
              <span className="field-error">{errors.title}</span>
            )}
          </div>

          <div className="form-group">
            <label htmlFor="contentType">Content Type</label>

            <select
              id="contentType"
              value={contentType}
              onChange={(event) => setContentType(event.target.value)}
              disabled={isSubmitting}
            >
              <option value="SOCIAL_POST">Social Media Post</option>
              <option value="ADVERTISEMENT">Advertisement</option>
              <option value="WEBSITE_COPY">Website Copy</option>
              <option value="EMAIL">Marketing Email</option>
              <option value="BLOG">Blog Article</option>
            </select>
          </div>

        </div>

        <div className="review-form-panel editor-panel">

          <div className="form-section-heading">
            <h3>Content Editor</h3>
            <p>
              Paste or write the marketing content you want to review.
            </p>
          </div>

          <div className="form-group">
            <label htmlFor="content">Your Content</label>

            <textarea
              id="content"
              placeholder="Start writing your marketing content here..."
              value={content}
              onChange={(event) => {
                setContent(event.target.value)
                setErrors((previous) => ({
                  ...previous,
                  content: '',
                }))
              }}
              rows={12}
              disabled={isSubmitting}
            />

            {errors.content && (
              <span className="field-error">{errors.content}</span>
            )}

            <div className="editor-footer">
              <span>{wordCount} words</span>
              <span>{content.length} characters</span>
            </div>
          </div>

        </div>

        <div className="review-info">
          <span className="info-icon">ⓘ</span>
          <p>
            Your content will be evaluated against approved brand facts,
            terminology and marketing guidelines.
          </p>
        </div>

        {submitError && (
          <div className="submit-error" role="alert">
            {submitError}
          </div>
        )}

        <div className="review-actions">

          <button
            type="button"
            className="back-button"
            onClick={onBack}
            disabled={isSubmitting}
          >
            Cancel
          </button>

          <button
            type="submit"
            className="primary-button"
            disabled={isSubmitting || !title.trim() || !content.trim()}
          >
            {isSubmitting ? 'Submitting...' : 'Run Brand Review →'}
          </button>

        </div>

      </form>

    </div>
  )
}

export default NewReview