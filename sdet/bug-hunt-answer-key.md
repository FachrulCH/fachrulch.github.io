# Bug Hunt Challenge - Answer Key

> **Total: 25 bugs | Max Score: 55 points**

## Scoring

| Difficulty | Points | Count |
|------------|--------|-------|
| Easy       | 1 pt   | 9     |
| Medium     | 2 pt   | 7     |
| Hard       | 3 pt   | 5     |
| Expert     | 5 pt   | 4     |

---

## Easy Bugs (1 point each)

### Bug #1 — Invisible Discount Badge
- **Location:** Product card "Wireless Headphones"
- **What:** The "20% OFF" badge has the same text color and background color (`#fffde7`), making it completely invisible.
- **How to find:** Visual inspection or inspect element → `.discount-badge` CSS class
- **Keywords:** `invisible`, `contrast`, `color`, `badge`, `discount`

### Bug #7 — Negative Product Price
- **Location:** Product card "Laptop Stand"
- **What:** Price shows `$-29.99` — a negative price makes no sense.
- **How to find:** Visual inspection
- **Keywords:** `negative`, `price`, `-29`

### Bug #9 — Six Stars Out of Five
- **Location:** Product card "Mechanical Keyboard"
- **What:** Rating shows 6 filled stars (★★★★★★) instead of max 5.
- **How to find:** Count the stars visually
- **Keywords:** `6`, `star`, `rating`, `five`

### Bug #14 — Invalid Email Format
- **Location:** Team Members table, row "Alice Chen"
- **What:** Email shows `alice.chen@@company..com` — double `@` and double `.`
- **How to find:** Visual inspection of table data
- **Keywords:** `email`, `@@`, `format`, `invalid`

### Bug #15 — Empty Name Cell
- **Location:** Team Members table, 3rd row (DevOps Engineer)
- **What:** The Name column is completely empty.
- **How to find:** Visual inspection of table
- **Keywords:** `empty`, `name`, `missing`, `blank`

### Bug #19 — Lorem Ipsum Placeholder
- **Location:** FAQ section → "What payment methods are accepted?"
- **What:** The answer contains lorem ipsum placeholder text instead of real content.
- **How to find:** Open the accordion and read the content
- **Keywords:** `lorem`, `ipsum`, `placeholder`

### Bug #22 — Password Field Shows Plain Text
- **Location:** Login Form → Password input
- **What:** The password field uses `type="text"` instead of `type="password"`, making the password visible.
- **How to find:** Type in the password field and notice it's not masked, or inspect the element
- **Keywords:** `password`, `text`, `plain`, `visible`, `type`

### Bug #25 — Outdated Copyright Year
- **Location:** Page footer
- **What:** Copyright says `© 2019` which is outdated.
- **How to find:** Scroll to footer
- **Keywords:** `copyright`, `2019`, `year`, `footer`

### Bug #4 — Buttons Call Undefined Functions
- **Location:** "Mark all read" button (Navigation) and "Delete All Data" button (Actions)
- **What:** `onclick="markAllRead()"` and `onclick="deleteAllData()"` reference functions that don't exist. Clicking them throws `ReferenceError` in console.
- **How to find:** Click the buttons and check console, or inspect the onclick handlers
- **Keywords:** `undefined`, `function`, `markAllRead`, `deleteAllData`

---

## Medium Bugs (2 points each)

### Bug #3 — Duplicate HTML ID
- **Location:** Navigation link `<a id="nav-profile">` and Profile heading `<h3 id="nav-profile">`
- **What:** Two elements share the same ID `nav-profile`, violating HTML spec. `document.getElementById('nav-profile')` will only return the first one.
- **How to find:** Inspect element or search DOM for duplicate IDs
- **Keywords:** `duplicate`, `id`, `nav-profile`

### Bug #5 — Bio Text Truncated Without Expand
- **Location:** User Profile → bio paragraph
- **What:** `.bio-text` has `max-height: 40px; overflow: hidden` — the text is cut off mid-sentence with no "read more" or scroll mechanism.
- **How to find:** Notice text seems incomplete, inspect the element's CSS
- **Keywords:** `overflow`, `hidden`, `cut`, `truncat`, `bio`

### Bug #10 — NaN Counter
- **Location:** User Profile → Stats → Commits counter
- **What:** Shows `NaN`. The code calls `parseInt('not-a-number')` which returns `NaN`, then the counter animation multiplies/adds with `NaN`.
- **How to find:** Visual inspection or console check
- **Keywords:** `nan`, `number`, `commit`, `counter`

### Bug #13 — Wrong Search Input Type
- **Location:** Team Members section → Search box
- **What:** The search input has `type="date"` instead of `type="text"`, showing a date picker instead of a text search box.
- **How to find:** Try to type in the search box and notice it's a date picker, or inspect the element
- **Keywords:** `date`, `search`, `input`, `type`

### Bug #16 — Status Text/Style Mismatch
- **Location:** Team Members table → Diana Ross row
- **What:** The status text says "Active" but uses the `status-inactive` CSS class (red styling), creating a visual contradiction.
- **How to find:** Notice the red "Active" badge, inspect the element's class
- **Keywords:** `status`, `active`, `inactive`, `mismatch`, `style`

### Bug #17 — Progress Bar Mismatch
- **Location:** Project Dashboard → Sprint Progress bar
- **What:** The bar text shows `85%` but the actual CSS width is `45%` — the visual doesn't match the number.
- **How to find:** Notice the bar looks less than half full but says 85%, inspect the `style` attribute
- **Keywords:** `progress`, `85`, `45`, `width`, `mismatch`

### Bug #18 — Unix Epoch Tooltip Date
- **Location:** Project Dashboard → "Last updated: 2 hours ago" tooltip
- **What:** Hovering shows `January 1, 1970 00:00:00 UTC` — the Unix epoch, indicating an uninitialized timestamp.
- **How to find:** Hover over "2 hours ago" text
- **Keywords:** `epoch`, `1970`, `date`, `tooltip`, `timestamp`

### Bug #21 — Autocomplete Disabled on Email
- **Location:** Login Form → Email input
- **What:** `autocomplete="off"` prevents password managers from autofilling, bad for UX and security.
- **How to find:** Inspect the email input attributes
- **Keywords:** `autocomplete`, `off`, `email`

---

## Hard Bugs (3 points each)

### Bug #6 — Product Image 404
- **Location:** Product card "Wireless Headphones" image
- **What:** The `<img>` src points to `https://httpstat.us/404`, which returns a 404. The `onerror` handler hides it gracefully, but the Network tab shows the failed request.
- **How to find:** Open DevTools → Network tab → look for failed requests (red entries)
- **Keywords:** `404`, `image`, `network`, `failed`, `broken`

### Bug #8 — Z-Index Layering Issue
- **Location:** Modal overlay vs floating notification
- **What:** The floating notification has `z-index: 999` while the modal overlay has `z-index: 100`. When both are visible, the notification appears on top of the modal, breaking the expected modal behavior.
- **How to find:** Click "Open Modal" then quickly click "Show Notification" — notification appears above the modal overlay
- **Keywords:** `z-index`, `modal`, `notification`, `overlay`

### Bug #11 — External CSS 404
- **Location:** `<head>` section
- **What:** `<link rel="stylesheet" href="https://cdn.example.com/nonexistent-theme-v3.2.1.css">` points to a non-existent CSS file, generating a 404 in the Network tab.
- **How to find:** DevTools → Network tab → filter by CSS → see failed request
- **Keywords:** `404`, `css`, `stylesheet`, `network`, `cdn`

### Bug #12 — Favicon 404
- **Location:** `<head>` section
- **What:** `<link rel="icon" href="/favicon-bug-hunt-x9z.ico">` points to a non-existent favicon, generating a 404.
- **How to find:** DevTools → Network tab → look for failed .ico request
- **Keywords:** `favicon`, `404`, `network`, `ico`

### Bug #20 — Insecure Form Action (HTTP)
- **Location:** Login Form `<form>` tag
- **What:** `action="http://api.example.com/login"` uses HTTP instead of HTTPS, meaning credentials would be sent in plain text.
- **How to find:** Inspect the `<form>` element's `action` attribute
- **Keywords:** `http`, `https`, `insecure`, `form`, `action`

---

## Expert Bugs (5 points each)

### Bug #23 — Hidden Debug Panel with Secrets
- **Location:** Hidden `<div id="debug-panel">` near the bottom of the page (has `display:none`)
- **What:** Contains sensitive information in the DOM:
  - API Key: `sk-test-4f8b2c1a9e3d7f6b5a0c8d2e1f4a7b3c`
  - DB Host: `prod-db.internal.company.com:5432`
  - Admin JWT token
  - Environment: `production`
- **How to find:** Inspect element → search DOM for "debug" or "api" or "token", or use Elements panel to browse hidden elements
- **Keywords:** `debug`, `hidden`, `api key`, `token`, `sensitive`, `credential`

### Bug #24 — Credentials in HTML Comment
- **Location:** HTML comment block near the footer
- **What:** Contains staging credentials in a `<!-- TODO -->` comment:
  - Username: `admin`
  - Password: `P@ssw0rd123!`
  - API endpoint: `https://staging-api.internal.company.com/v2`
- **How to find:** View page source (Ctrl+U) or inspect DOM and look for comment nodes
- **Keywords:** `comment`, `html`, `credential`, `password`, `staging`, `admin`

### Bug #25b — Console: Non-Standard Log Messages
- **Location:** Browser DevTools → Console tab
- **What:** Multiple suspicious console outputs appear on page load and over time:

  **Immediate (on load):**
  | Type | Message |
  |------|---------|
  | `console.log` | `[WARNING] Debug mode is enabled in production!` (red styled) |
  | `console.warn` | `Deprecation warning: userData.legacyFormat() will be removed in v4.0` |
  | `console.error` | `Failed to load user preferences: QUOTA_EXCEEDED_ERR` |
  | `console.log` | `[PERF] Page load took 4,723ms — threshold is 2,000ms` (orange styled) |
  | `console.info` | `[TELEMETRY] Session data sent to analytics.tracker.io — user did not opt in` |
  | `console.warn` | `[SECURITY] Content-Security-Policy header is missing` |
  | `console.error` | `Unhandled promise rejection: TypeError: Cannot read property "email" of undefined` |

  **Delayed:**
  | Time | Type | Message |
  |------|------|---------|
  | 2s | `console.error` | `[CONFIG] Failed to parse configuration: ...` |
  | 3s | `console.error` | `[MEMORY] Potential memory leak detected: 847 detached DOM nodes` |
  | 4s | `console.table` | Performance metrics table (all EXCEEDED) |
  | 5s | `console.warn` | `[API] Rate limit approaching: 487/500 requests` |
  | 8s | `console.log` | `[AUTH] Token expires in 30 seconds. No refresh handler registered.` |

  **On login form submit:**
  | Type | Message |
  |------|---------|
  | `console.log` | `[AUTH] Login attempt — email: ..., password: ...` (logs credentials!) |

  **On "Run Diagnostic" button click:**
  | Type | Message |
  |------|---------|
  | grouped | Browser info, WebSocket failure, localStorage 4.8/5MB, `STATUS: DEGRADED` |

- **How to find:** Open DevTools → Console tab, observe messages over time

### Bug #25c — Memory Leak
- **Location:** JavaScript `setInterval` at the bottom of the script
- **What:** Every 2 seconds, the script pushes 100 objects (each containing a detached DOM node and a string) into `leakyArray` which is never cleaned up. Over time this will consume increasing memory.
- **How to find:** DevTools → Memory tab → take heap snapshots over time and compare, or Performance monitor → observe JS heap size growing
- **Keywords:** `memory`, `leak`, `detached`, `DOM`, `interval`

---

## Bug Checklist

| # | Difficulty | Bug | Found |
|---|-----------|-----|-------|
| 1 | Easy | Invisible discount badge (same color text/bg) | ☐ |
| 2 | Easy | Settings link goes to `about:blank` | ☐ |
| 3 | Medium | Duplicate ID `nav-profile` | ☐ |
| 4 | Easy | Buttons call undefined functions | ☐ |
| 5 | Medium | Bio text cut off (overflow hidden) | ☐ |
| 6 | Hard | Product image 404 (Network tab) | ☐ |
| 7 | Easy | Negative product price (-$29.99) | ☐ |
| 8 | Hard | Z-index: notification overlaps modal | ☐ |
| 9 | Easy | 6 stars out of 5 | ☐ |
| 10 | Medium | Commits counter shows NaN | ☐ |
| 11 | Hard | External CSS 404 (Network tab) | ☐ |
| 12 | Hard | Favicon 404 (Network tab) | ☐ |
| 13 | Medium | Search input is type="date" | ☐ |
| 14 | Easy | Invalid email format (@@, ..) | ☐ |
| 15 | Easy | Empty name cell in table | ☐ |
| 16 | Medium | Status text/class mismatch | ☐ |
| 17 | Medium | Progress bar 85% text, 45% width | ☐ |
| 18 | Medium | Tooltip shows Unix epoch (1970) | ☐ |
| 19 | Easy | Lorem ipsum placeholder in FAQ | ☐ |
| 20 | Hard | Login form uses HTTP (not HTTPS) | ☐ |
| 21 | Medium | autocomplete="off" on email | ☐ |
| 22 | Easy | Password field is type="text" | ☐ |
| 23 | Expert | Hidden debug panel with API keys in DOM | ☐ |
| 24 | Expert | HTML comment contains staging credentials | ☐ |
| 25 | Easy | Copyright year 2019 (outdated) | ☐ |
| — | Expert | Console: non-standard log messages | ☐ |
| — | Expert | Memory leak (growing leakyArray) | ☐ |
