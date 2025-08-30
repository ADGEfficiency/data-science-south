/**
 * Home page view toggle functionality
 * Switches between competency-based, year-based, and type-based content grouping
 */

document.addEventListener('DOMContentLoaded', function() {
  // Get DOM elements
  const competencyViewBtn = document.getElementById('competency-view-btn');
  const yearViewBtn = document.getElementById('year-view-btn');
  const typeViewBtn = document.getElementById('type-view-btn');
  const competencyView = document.getElementById('competency-view');
  const yearView = document.getElementById('year-view');
  const typeView = document.getElementById('type-view');
  const toggleAllBtn = document.getElementById('toggle-all-btn');
  
  // Check if all required elements exist
  if (!competencyViewBtn || !yearViewBtn || !typeViewBtn || !competencyView || !yearView || !typeView || !toggleAllBtn) {
    console.warn('Home toggle: Required elements not found');
    return;
  }
  
  // Load user's preferred view from localStorage
  const savedView = localStorage.getItem('home-view-preference') || 'competency';
  
  // Initialize collapsible sections functionality
  initializeCollapsibleSections();
  
  // Set initial view based on saved preference
  if (savedView === 'year') {
    showYearView();
  } else if (savedView === 'type') {
    showTypeView();
  } else {
    showCompetencyView();
  }
  
  // Update toggle button text initially
  updateToggleButtonText();
  
  // Show content area now that everything is set up correctly
  document.getElementById('content-area').classList.remove('opacity-0');
  
  // Add event listeners
  competencyViewBtn.addEventListener('click', function(e) {
    e.preventDefault();
    const shouldExpandAll = isCurrentStateExpanded();
    showCompetencyView();
    localStorage.setItem('home-view-preference', 'competency');
    if (shouldExpandAll) {
      expandAllSections();
    } else {
      collapseAllSections();
    }
    updateToggleButtonText();
  });
  
  yearViewBtn.addEventListener('click', function(e) {
    e.preventDefault();
    const shouldExpandAll = isCurrentStateExpanded();
    showYearView();
    localStorage.setItem('home-view-preference', 'year');
    if (shouldExpandAll) {
      expandAllSections();
    } else {
      collapseAllSections();
    }
    updateToggleButtonText();
  });
  
  typeViewBtn.addEventListener('click', function(e) {
    e.preventDefault();
    const shouldExpandAll = isCurrentStateExpanded();
    showTypeView();
    localStorage.setItem('home-view-preference', 'type');
    if (shouldExpandAll) {
      expandAllSections();
    } else {
      collapseAllSections();
    }
    updateToggleButtonText();
  });
  
  // Toggle all button
  toggleAllBtn.addEventListener('click', function(e) {
    e.preventDefault();
    if (isCurrentStateExpanded()) {
      collapseAllSections();
    } else {
      expandAllSections();
    }
    updateToggleButtonText();
  });
  
  /**
   * Show the competency-based view
   */
  function showCompetencyView() {
    // Update button states
    competencyViewBtn.classList.remove('bg-gray-100', 'text-gray-700');
    competencyViewBtn.classList.add('bg-gray-800', 'text-white', 'active');
    
    yearViewBtn.classList.remove('bg-gray-800', 'text-white', 'active');
    yearViewBtn.classList.add('bg-gray-100', 'text-gray-700');
    
    typeViewBtn.classList.remove('bg-gray-800', 'text-white', 'active');
    typeViewBtn.classList.add('bg-gray-100', 'text-gray-700');
    
    // Update view visibility
    competencyView.classList.remove('hidden');
    yearView.classList.add('hidden');
    typeView.classList.add('hidden');
  }
  
  /**
   * Show the year-based view
   */
  function showYearView() {
    // Update button states
    yearViewBtn.classList.remove('bg-gray-100', 'text-gray-700');
    yearViewBtn.classList.add('bg-gray-800', 'text-white', 'active');
    
    competencyViewBtn.classList.remove('bg-gray-800', 'text-white', 'active');
    competencyViewBtn.classList.add('bg-gray-100', 'text-gray-700');
    
    typeViewBtn.classList.remove('bg-gray-800', 'text-white', 'active');
    typeViewBtn.classList.add('bg-gray-100', 'text-gray-700');
    
    // Update view visibility
    yearView.classList.remove('hidden');
    competencyView.classList.add('hidden');
    typeView.classList.add('hidden');
  }
  
  /**
   * Show the type-based view
   */
  function showTypeView() {
    // Update button states
    typeViewBtn.classList.remove('bg-gray-100', 'text-gray-700');
    typeViewBtn.classList.add('bg-gray-800', 'text-white', 'active');
    
    competencyViewBtn.classList.remove('bg-gray-800', 'text-white', 'active');
    competencyViewBtn.classList.add('bg-gray-100', 'text-gray-700');
    
    yearViewBtn.classList.remove('bg-gray-800', 'text-white', 'active');
    yearViewBtn.classList.add('bg-gray-100', 'text-gray-700');
    
    // Update view visibility
    typeView.classList.remove('hidden');
    competencyView.classList.add('hidden');
    yearView.classList.add('hidden');
  }
  
  /**
   * Initialize collapsible sections functionality
   */
  function initializeCollapsibleSections() {
    // Add event listeners to all section headers
    document.addEventListener('click', function(e) {
      if (e.target.closest('.section-header')) {
        const header = e.target.closest('.section-header');
        const section = header.closest('.collapsible-section');
        toggleSection(section);
      }
    });
  }
  
  /**
   * Toggle a single section
   */
  function toggleSection(section) {
    const content = section.querySelector('.section-content');
    const isCollapsed = content.classList.contains('collapsed');
    
    if (isCollapsed) {
      content.classList.remove('collapsed');
      section.classList.remove('collapsed');
    } else {
      content.classList.add('collapsed');
      section.classList.add('collapsed');
    }
    
    // Save state to localStorage
    const sectionId = section.querySelector('.section-header').getAttribute('data-section');
    const currentView = getCurrentView();
    const storageKey = `section-${currentView}-${sectionId}`;
    localStorage.setItem(storageKey, isCollapsed ? 'expanded' : 'collapsed');
    
    // Update toggle button text after individual section toggle
    updateToggleButtonText();
  }
  
  /**
   * Expand all visible sections
   */
  function expandAllSections() {
    const visibleSections = getVisibleSections();
    visibleSections.forEach(section => {
      const content = section.querySelector('.section-content');
      
      content.classList.remove('collapsed');
      section.classList.remove('collapsed');
      
      // Save state
      const sectionId = section.querySelector('.section-header').getAttribute('data-section');
      const currentView = getCurrentView();
      const storageKey = `section-${currentView}-${sectionId}`;
      localStorage.setItem(storageKey, 'expanded');
    });
    updateToggleButtonText();
  }
  
  /**
   * Collapse all visible sections
   */
  function collapseAllSections() {
    const visibleSections = getVisibleSections();
    visibleSections.forEach(section => {
      const content = section.querySelector('.section-content');
      
      content.classList.add('collapsed');
      section.classList.add('collapsed');
      
      // Save state
      const sectionId = section.querySelector('.section-header').getAttribute('data-section');
      const currentView = getCurrentView();
      const storageKey = `section-${currentView}-${sectionId}`;
      localStorage.setItem(storageKey, 'collapsed');
    });
    updateToggleButtonText();
  }
  
  /**
   * Get all sections in the currently visible view
   */
  function getVisibleSections() {
    const currentView = getCurrentView();
    let viewContainer;
    
    if (currentView === 'competency') {
      viewContainer = competencyView;
    } else if (currentView === 'year') {
      viewContainer = yearView;
    } else {
      viewContainer = typeView;
    }
    
    return viewContainer.querySelectorAll('.collapsible-section');
  }
  
  /**
   * Get the current active view
   */
  function getCurrentView() {
    if (!competencyView.classList.contains('hidden')) return 'competency';
    if (!yearView.classList.contains('hidden')) return 'year';
    if (!typeView.classList.contains('hidden')) return 'type';
    return 'competency'; // default
  }
  
  /**
   * Check if current state should be considered "expanded" (any section is expanded)
   */
  function isCurrentStateExpanded() {
    const visibleSections = getVisibleSections();
    
    // If any section is expanded, consider the overall state as expanded
    for (let section of visibleSections) {
      const content = section.querySelector('.section-content');
      const isCollapsed = content.classList.contains('collapsed');
      if (!isCollapsed) {
        return true; // Found at least one expanded section
      }
    }
    
    return false; // All sections are collapsed
  }
  
  /**
   * Update the toggle button text based on current state
   */
  function updateToggleButtonText() {
    if (isCurrentStateExpanded()) {
      toggleAllBtn.textContent = 'Collapse All';
    } else {
      toggleAllBtn.textContent = 'Expand All';
    }
  }
});