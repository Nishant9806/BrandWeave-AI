import NewReview from './components/NewReview'
import { useState } from 'react'
import './App.css'
import ReviewResults from './components/ReviewResults'
import BrandVault from './components/BrandVault'
import ReviewHistory from './components/ReviewHistory'
import Approvals from './components/Approvals'
import Settings from './components/Settings'
const navigation = [
  { name: 'Overview', icon: '▦' },
  { name: 'Brand Vault', icon: '◈' },
  { name: 'New Review', icon: '＋' },
  { name: 'Review History', icon: '◷' },
  { name: 'Approvals', icon: '✓' },
]

function App() {
  const [activePage, setActivePage] = useState('Overview')
  const [submittedContent, setSubmittedContent] = useState({
  title: '',
  content_type: '',
  content: '',
})
  return (
    <div className="app-container">

      {/* Sidebar */}
      <aside className="sidebar">

        <div className="brand">
          <div className="brand-logo">B</div>
          <div>
            <h2>BrandWeave</h2>
            <span>AI BRAND GOVERNANCE</span>
          </div>
        </div>

        <div className="workspace">
          <span className="workspace-label">WORKSPACE</span>
          <div className="workspace-card">
            <div className="workspace-icon">T</div>
            <div>
              <strong>TechNova</strong>
              <small>Brand Workspace</small>
            </div>
            <span className="workspace-arrow">⌄</span>
          </div>
        </div>

        <nav className="navigation">
          <span className="nav-label">MENU</span>

          {navigation.map((item) => (
            <button
              key={item.name}
              className={`nav-item ${
                activePage === item.name ? 'active' : ''
              }`}
              onClick={() => setActivePage(item.name)}
            >
              <span className="nav-icon">{item.icon}</span>
              {item.name}
            </button>
          ))}
        </nav>

        <div className="sidebar-bottom">
          <button
  className={`nav-item ${activePage === 'Settings' ? 'active' : ''}`}
  onClick={() => setActivePage('Settings')}
>
            <span className="nav-icon">⚙</span>
            Settings
          </button>

          <div className="profile">
            <div className="avatar">NS</div>
            <div>
              <strong>Nishant Srivastava</strong>
              <small>Administrator</small>
            </div>
            <span className="profile-menu">•••</span>
          </div>
        </div>

      </aside>

      {/* Main Content */}
      <main className="main-content">

        <header className="topbar">
          <div>
            <span className="breadcrumb">Workspace / {activePage}</span>
          </div>

          <div className="topbar-right">
            <span className="environment">DEMO ENVIRONMENT</span>
            <button className="notification">♧</button>
          </div>
        </header>

        <section className="page-content">

          {activePage === 'Overview' ? (
            <>
              <div className="welcome-section">
                <div>
                  <span className="eyebrow">BRAND INTELLIGENCE CENTER</span>
                  <h1>Good evening, Nishant.</h1>
                  <p>
                    Here's what's happening with your brand governance today.
                  </p>
                </div>

                <button
                  className="primary-button"
                  onClick={() => setActivePage('New Review')}
                >
                  + New Content Review
                </button>
              </div>

              {/* Statistics */}
              <div className="stats-grid">

                <div className="stat-card">
                  <span>Total Submissions</span>
                  <h2>24</h2>
                  <small>All submitted content</small>
                  <div className="stat-icon purple">▤</div>
                </div>

                <div className="stat-card">
                  <span>Approved Content</span>
                  <h2>16</h2>
                  <small>Successfully approved</small>
                  <div className="stat-icon green">✓</div>
                </div>

                <div className="stat-card">
                  <span>Pending Reviews</span>
                  <h2>5</h2>
                  <small>Awaiting review or approval</small>
                  <div className="stat-icon orange">◷</div>
                </div>

                <div className="stat-card">
                  <span>Brand Violations</span>
                  <h2>12</h2>
                  <small>Detected across submissions</small>
                  <div className="stat-icon red">⚑</div>
                </div>

              </div>

              {/* Main dashboard panels */}
              <div className="dashboard-grid">

                <div className="panel activity-panel">
                  <div className="panel-heading">
                    <div>
                      <h3>Recent Submissions</h3>
                      <p>Latest content submitted for brand review</p>
                    </div>
                    <button className="text-button">View all →</button>
                  </div>

                  <div className="submission-list">

                    <div className="submission-row">
                      <div className="document-icon">文</div>
                      <div className="submission-info">
                        <strong>SmartWatch Pro Campaign</strong>
                        <small>Social Media Post · 14 Nov 2026</small>
                      </div>
                      <span className="status approved">Approved</span>
                    </div>

                    <div className="submission-row">
                      <div className="document-icon">文</div>
                      <div className="submission-info">
                        <strong>Product Launch Advertisement</strong>
                        <small>Advertisement · 14 Nov 2026</small>
                      </div>
                      <span className="status review">Under Review</span>
                    </div>

                    <div className="submission-row">
                      <div className="document-icon">文</div>
                      <div className="submission-info">
                        <strong>Winter Sale Campaign</strong>
                        <small>Marketing Copy · 13 Nov 2026</small>
                      </div>
                      <span className="status changes">Changes Required</span>
                    </div>

                    <div className="submission-row">
                      <div className="document-icon">文</div>
                      <div className="submission-info">
                        <strong>SmartWatch Product Description</strong>
                        <small>Website Copy · 12 Nov 2026</small>
                      </div>
                      <span className="status approved">Approved</span>
                    </div>

                  </div>
                </div>

                <div className="panel compliance-panel">
                  <div className="panel-heading">
                    <div>
                      <h3>Brand Compliance</h3>
                      <p>Overall governance overview</p>
                    </div>
                  </div>

                  <div className="compliance-score">
                    <div className="score-circle">
                      <div>
                        <strong>87%</strong>
                        <small>Compliant</small>
                      </div>
                    </div>
                  </div>

                  <div className="compliance-legend">
                    <div>
                      <span className="legend-dot compliant-dot"></span>
                      Compliant content
                      <strong>87%</strong>
                    </div>
                    <div>
                      <span className="legend-dot violation-dot"></span>
                      Needs attention
                      <strong>13%</strong>
                    </div>
                  </div>

                  <p className="demo-note">
                    Illustrative demo statistics
                  </p>
                </div>

              </div>

              {/* Bottom panel */}
              <div className="panel quick-actions">
                <div>
                  <h3>Keep your brand consistent.</h3>
                  <p>
                    Review content, verify brand claims and maintain
                    consistent messaging across every channel.
                  </p>
                </div>

                <button
                  className="secondary-button"
                  onClick={() => setActivePage('Brand Vault')}
                >
                  Explore Brand Vault →
                </button>
              </div>

            </>
          ) : activePage === 'Brand Vault' ? (

            <BrandVault />

          ) : activePage === 'New Review' ? (

            <NewReview
              onBack={() => setActivePage('Overview')}
              onSubmit={(data) => {
              setSubmittedContent(data)
              setActivePage('Review Results')
              }}
             />
          ) : activePage === 'Review History' ? (
            <ReviewHistory 
            />
          ) : activePage === 'Approvals' ? (
            <Approvals />
          ) : activePage === 'Settings' ? (
            <Settings />
          ) : activePage === 'Review Results' ? (

            <ReviewResults
              title={submittedContent.title}
              onBack={() => setActivePage('New Review')}
            />

          ) : (

            <div className="placeholder-page">
              <span className="eyebrow">BRANDWEAVE WORKSPACE</span>
              <h1>{activePage}</h1>
              <p>
                This section is being developed.
              </p>
              <button
                className="primary-button"
                onClick={() => setActivePage('Overview')}
              >
                Back to Overview
              </button>
            </div>

          )}

        </section>

      </main>
    </div>
  )
}

export default App
