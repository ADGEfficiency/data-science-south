document.addEventListener('DOMContentLoaded', function () {
  // Add copy buttons to all code blocks
  const codeBlocks = document.querySelectorAll('pre code')

  codeBlocks.forEach(function (codeBlock) {
    const pre = codeBlock.parentElement
    const figure = pre.parentElement

    // Create copy button
    const copyButton = document.createElement('button')
    copyButton.className = 'copy-code-btn'
    copyButton.innerHTML = `
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                <path d="m5 15-4-4 4-4"></path>
            </svg>
        `
    copyButton.setAttribute('aria-label', 'Copy code to clipboard')

    // Add click handler
    copyButton.addEventListener('click', function () {
      let code = codeBlock.textContent

      // Remove $ and following whitespace if code starts with $
      if (code.startsWith('$ ')) {
        code = code.substring(2)
      }

      navigator.clipboard
        .writeText(code)
        .then(function () {
          // Show success state
          copyButton.innerHTML = `
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polyline points="20,6 9,17 4,12"></polyline>
                    </svg>
                    Copied!
                `
          copyButton.classList.add('copied')

          // Reset after 2 seconds
          setTimeout(function () {
            copyButton.innerHTML = `
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="m5 15-4-4 4-4"></path>
                        </svg>
                    `
            copyButton.classList.remove('copied')
          }, 2000)
        })
        .catch(function (err) {
          console.error('Failed to copy code: ', err)
          copyButton.innerHTML = 'Failed'
          setTimeout(function () {
            copyButton.innerHTML = `
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="m5 15-4-4 4-4"></path>
                        </svg>
                    `
          }, 2000)
        })
    })

    // Insert the button into the figure (before the pre element)
    figure.insertBefore(copyButton, pre)
  })
})
