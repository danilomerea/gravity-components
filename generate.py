#!/usr/bin/env python3
"""Gravity Component Pages Generator — run: python3 generate.py"""

import os, html

CDN = 'https://gravity.group-cdn.one/v5.38.6'
DOCS = 'https://gravity.group.one'
OUT = os.path.dirname(os.path.abspath(__file__))

def ic(name, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<gv-icon aria-hidden="true"{c} src="{CDN}/icons/{name}.svg"></gv-icon>'

def tile(name):
    return f'<gv-tile aria-hidden="true" src="{CDN}/tiles/{name}.svg"></gv-tile>'

def logo(name):
    return f'<gv-logo src="{CDN}/logos/{name}.svg"></gv-logo>'

CAT_BADGE = {'component':'gv-badge-info','form':'gv-badge-generic','ai':'gv-badge-aida'}
CAT_LABEL = {'component':'Component','form':'Form','ai':'AI'}

# ── Component definitions ─────────────────────────────────────────────
# (name, slug, css_class, docs_path, category, description, icons_list)
COMPONENTS = [
    ('Accordion','accordion','.gv-accordion','/components/accordion','component',
     'Collapsible content sections for organising grouped information compactly.',
     ['expand_more','expand_less','chevron_right']),
    ('App Rail','app-rail','.gv-app-rail','/components/app-rail','component',
     'Vertical navigation rail used in multi-product or app-shell layouts.',
     ['dashboard','storefront','language','view_comfy','settings']),
    ('Badge','badge','.gv-badge','/components/badges','component',
     'Status indicators, labels, and category tags for displaying contextual metadata.',
     []),
    ('Breadcrumbs','breadcrumbs','.gv-breadcrumbs','/components/breadcrumbs','component',
     'Navigation trail showing the user\'s current location within a hierarchy.',
     ['chevron_right','arrow_back','home']),
    ('Button','button','.gv-button','/components/buttons','component',
     'Interactive action triggers in multiple variants, sizes, and states.',
     ['arrow_forward','add','auto_awesome','download','delete','close']),
    ('Card','card','.gv-card','/components/card','component',
     'Container for grouped content with optional tile, title, actions, and footer.',
     ['arrow_forward','more_horiz']),
    ('Chat','chat','.gv-chat','/components/chat','component',
     'AI conversation thread displaying outgoing and incoming message bubbles.',
     []),
    ('Checkbox','checkbox','.gv-checkbox','/form-components/checkbox','form',
     'Standard checkbox input in checked, unchecked, disabled, and mixed states.',
     []),
    ('Chip','chip','.gv-chip','/components/chip','component',
     'Toggle filters, radio-style selectors, and read-only label chips.',
     ['close','check']),
    ('Comparison Table','comparison-table','.gv-table-comparison','/components/comparison-table','component',
     'Side-by-side feature comparison across product tiers with recommended highlight.',
     ['check_circle','remove','star']),
    ('Content Container','content-container','.gv-content-container','/components/content-container','component',
     'Styled surface box with border, radius, and optional padding modifiers.',
     ['info']),
    ('Conversational AI','conversational-ai','.gv-chat + .gv-input-ai','/ai/conversational','ai',
     'Full AI chat interface combining a message thread with an AI-specific input field.',
     ['arrow_forward','auto_awesome']),
    ('Data Table','data-table','.gv-data-table','/components/data-table','component',
     'Sortable, selectable table for displaying structured records with row actions.',
     ['more_horiz','check_circle','warning','filter_list']),
    ('Divider','divider','.gv-divider','/components/divider','component',
     'Horizontal separator line with optional label or action button variant.',
     ['add']),
    ('Donut Chart','donut-chart','.gv-donut-chart','/components/donut-chart','component',
     'Circular progress meter for displaying resource usage or completion percentage.',
     []),
    ('Footer','footer','.gv-footer','/components/footer','component',
     'Page footer with copyright, links, and optional brand logo.',
     []),
    ('Header','header','.gv-main-header','/components/header','component',
     'Top navigation bar with logo, nav links, and optional user actions.',
     ['notifications','account_circle','settings','search']),
    ('Input AI','input-ai','.gv-input-ai','/form-components/input-ai','form',
     'AI-specific textarea with send button and generated-content disclaimer.',
     ['arrow_forward','auto_awesome','mic']),
    ('Input Autocomplete','input-autocomplete','.gv-autocomplete','/form-components/input-autocomplete','form',
     'Text field with typeahead dropdown for selecting from a list of options.',
     ['expand_more','search','close']),
    ('Input Character Counter','input-character-counter','.gv-char-counter','/form-components/input-character-counter','form',
     'Input or textarea with a live character counter showing remaining characters.',
     []),
    ('Input Date','input-date','.gv-input-date','/form-components/input-date','form',
     'Date and time picker inputs with calendar and clock icon addons.',
     ['date_range','schedule','event','today']),
    ('Input General','input-general','.gv-input','/form-components/input-general','form',
     'Standard text input in default, error, disabled, and addon prefix/suffix variants.',
     ['search','visibility','close','link']),
    ('Input Number','input-number','.gv-input-number','/form-components/input-number','form',
     'Stepper input for incrementing and decrementing numeric values.',
     ['add','remove']),
    ('Input Search','input-search','.gv-input-search','/form-components/input-search','form',
     'Search field with integrated search button and clear option.',
     ['search','close','filter_list']),
    ('Input Select','input-select','.gv-input-select','/form-components/input-select','form',
     'Native select dropdown with custom styling and chevron icon.',
     ['expand_more']),
    ('Input Textarea','input-textarea','.gv-input-textarea','/form-components/input-textarea','form',
     'Multi-line text input with resizable area for longer form content.',
     []),
    ('Legend','legend','.gv-legend','/components/legend','component',
     'Status key with labelled icons for interpreting data visualisations.',
     ['check_circle','warning','dangerous','remove']),
    ('List','list','.gv-list-items','/components/list','component',
     'Styled unordered lists with check or bullet variants for feature displays.',
     ['check_circle']),
    ('List Table','list-table','.gv-list-table','/components/list-table','component',
     'Lightweight row-based list with column headers, ideal for settings and logs.',
     ['more_horiz','check_circle','warning']),
    ('Loader','loader','gv-loader','/components/loader','component',
     'Animated spinner for indicating loading states and async operations.',
     []),
    ('Modal','modal','.gv-modal','/components/modal','component',
     'Dialog overlay for confirmations, forms, and focused user interactions.',
     ['close','warning','check_circle','info']),
    ('Navigation','navigation','.gv-global-nav','/components/navigation','component',
     'Icon-only vertical sidebar for app-level navigation between modules.',
     ['view_comfy','storefront','language','mail','contact_emergency','settings']),
    ('Notice','notice','.gv-notice','/components/notice','component',
     'Inline alert banners for info, success, warning, alert, upgrade, and system states.',
     ['info','check_circle','warning','error']),
    ('Option Group','option-group','.gv-option-group','/components/option-group','form',
     'Fieldset grouping of checkboxes or radio buttons with a shared label.',
     []),
    ('Overlay','overlay','.gv-overlay','/components/overlay','component',
     'Semi-transparent backdrop used to dim page content behind modals or drawers.',
     []),
    ('Page Header','page-header','.gv-page-header','/components/subheader','component',
     'Section header with title, subtitle, action buttons, and status stats line.',
     ['add','vitals','check_circle','download','filter_list']),
    ('Product Table','product-table','.gv-table-col','/components/product-table','component',
     'Pricing column presenting a single plan with price, CTA, and feature list.',
     ['check_circle','star','arrow_forward']),
    ('Quantity Select','quantity-select','.gv-input-quantity-select','/form-components/quantity-select','form',
     'Visual tile-based selector for choosing a quantity or configuration option.',
     []),
    ('Radio','radio','.gv-radio','/form-components/radio','form',
     'Radio button input for mutually exclusive option selection.',
     []),
    ('Resource','resource','.gv-resource','/components/resource','component',
     'Progress bar showing current vs total resource usage with alert states.',
     []),
    ('Sidedrawer','sidedrawer','.gv-sidedrawer','/components/sidedrawer','component',
     'Off-canvas panel sliding from the right, used for user menus and settings.',
     ['close','account_circle','logout','settings','notifications']),
    ('Skeleton','skeleton','.gv-skeleton','/components/skeleton','component',
     'Placeholder loading blocks mimicking content shape before data loads.',
     []),
    ('Stepper','stepper','.gv-stepper','/components/stepper','component',
     'Step-by-step progress indicator for multi-stage flows like checkout or setup.',
     ['check']),
    ('Sticky','sticky','.gv-sticky-bar','/components/sticky','component',
     'Fixed bar that appears after scroll to promote a key action or product.',
     ['close']),
    ('System Wide Banner','system-wide-banner','.gv-system-wide','/components/system-wide-banner','component',
     'Full-width dismissible notification banner for system-wide alerts.',
     ['error','warning','info','close']),
    ('Tabs','tabs','.gv-section-tablist','/components/tabs','component',
     'Horizontal tab bar for switching between related content panels.',
     []),
    ('Toggle','toggle','.gv-toggle','/form-components/toggle','form',
     'Switch control for binary on/off settings.',
     []),
    ('Tooltip','tooltip','.gv-tooltip','/components/tooltip','component',
     'Contextual label appearing on hover or focus to explain an element.',
     ['info','help_outline','more_horiz']),
]

# ── Preview HTML for index cards (compact) ────────────────────────────
PREVIEW = {
'accordion': f'''<div class="gv-accordion" style="width:100%;max-width:240px;">
  <div class="gv-acc-item"><h3 class="gv-acc-header"><button class="gv-acc-trigger gv-expanded" aria-expanded="true" aria-controls="pi-acc1" id="pi-acc1t"><span class="gv-acc-title">Open item</span></button></h3>
  <div id="pi-acc1" role="region" aria-labelledby="pi-acc1t" class="gv-acc-body"><div class="gv-acc-content"><p>Expanded content here.</p></div></div></div>
  <div class="gv-acc-item"><h3 class="gv-acc-header"><button class="gv-acc-trigger" aria-expanded="false" aria-controls="pi-acc2" id="pi-acc2t"><span class="gv-acc-title">Closed item</span></button></h3>
  <div id="pi-acc2" role="region" aria-labelledby="pi-acc2t" class="gv-acc-body gv-hidden"><div class="gv-acc-content"><p>Hidden.</p></div></div></div>
</div>''',

'app-rail': f'''<nav class="gv-app-rail" aria-label="App navigation">
  <ul class="gv-nav-list">
    <li><a href="#" class="gv-item gv-active" aria-current="true"><span class="gv-item-icon">{ic('dashboard')}</span><span>Dashboard</span></a></li>
    <li><a href="#" class="gv-item"><span class="gv-item-icon">{ic('storefront')}</span><span>Store</span></a></li>
    <li><a href="#" class="gv-item"><span class="gv-item-icon">{ic('language')}</span><span>Domains</span></a></li>
  </ul>
</nav>''',

'badge': f'''<div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center;">
  <div class="gv-badge gv-badge-generic">Generic</div>
  <div class="gv-badge gv-badge-alert">Alert</div>
  <div class="gv-badge gv-badge-warning">Warning</div>
  <div class="gv-badge gv-badge-info">Info</div>
  <div class="gv-badge gv-badge-success">Success</div>
  <div class="gv-badge gv-badge-discount">Save 20%</div>
</div>''',

'breadcrumbs': f'''<nav aria-label="Breadcrumb"><ol class="gv-breadcrumbs">
  <li><a href="#">Account</a>{ic('chevron_right')}</li>
  <li><a href="#">Hosting</a>{ic('chevron_right')}</li>
  <li><span aria-current="page">Settings</span></li>
</ol></nav>''',

'button': f'''<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;">
  <button type="button" class="gv-button gv-button-primary gv-mode-condensed">Primary</button>
  <button type="button" class="gv-button gv-button-secondary gv-mode-condensed">Secondary</button>
  <button type="button" class="gv-button gv-button-cta gv-mode-condensed">CTA</button>
  <button type="button" class="gv-button gv-button-destructive gv-mode-condensed">Destructive</button>
  <button type="button" class="gv-button gv-button-aida gv-mode-condensed">{ic('auto_awesome')}<span>Aida</span></button>
</div>''',

'card': f'''<div class="gv-card" style="max-width:200px;">
  <div class="gv-card-tile">{tile('dashboard')}</div>
  <div class="gv-card-content"><h3 class="gv-card-title">Card title</h3><p>Short description.</p></div>
  <div class="gv-card-footer"><button type="button" class="gv-button gv-button-primary gv-mode-condensed"><span>Action</span>{ic('arrow_forward')}</button></div>
</div>''',

'chat': f'''<section class="gv-chat" style="width:100%;max-width:260px;">
  <ul class="gv-chat-list">
    <li class="gv-chat-message gv-chat-outgoing"><div class="gv-meta"><span class="gv-meta-user">You</span></div><p class="gv-chat-message-body">Build me a landing page.</p></li>
    <li class="gv-chat-message gv-chat-incoming"><div class="gv-meta"><span class="gv-meta-user">Aida</span></div><p class="gv-chat-message-body">On it! Give me a moment…</p></li>
  </ul>
</section>''',

'checkbox': f'''<div style="display:flex;flex-direction:column;gap:10px;align-items:flex-start;">
  <label style="display:flex;gap:8px;align-items:center;"><input type="checkbox" class="gv-checkbox" /> Unchecked</label>
  <label style="display:flex;gap:8px;align-items:center;"><input type="checkbox" class="gv-checkbox" checked /> Checked</label>
  <label style="display:flex;gap:8px;align-items:center;"><input type="checkbox" class="gv-checkbox" disabled /> Disabled</label>
</div>''',

'chip': f'''<div style="display:flex;flex-direction:column;gap:10px;align-items:flex-start;">
  <div style="display:flex;gap:6px;flex-wrap:wrap;">
    <button type="button" class="gv-chip">Inactive</button>
    <button type="button" class="gv-chip gv-chip-active">Active</button>
    <button type="button" class="gv-chip">Filter</button>
  </div>
  <div style="display:flex;gap:6px;">
    <button type="button" class="gv-chip gv-chip-radio gv-chip-active">Monthly</button>
    <button type="button" class="gv-chip gv-chip-radio">Annual</button>
  </div>
</div>''',

'comparison-table': f'''<div class="gv-table-comparison gv-table-features" style="width:100%;font-size:12px;">
  <div class="gv-table" role="table">
    <header class="gv-table-header" role="rowgroup"><div class="gv-table-slider"><div class="gv-rows"><div class="gv-table-row" role="row">
      <div class="gv-row-header gv-sr-only" role="rowheader"><span>Plan</span></div>
      <div class="gv-row-cells">
        <div class="gv-row-cell" role="columnheader"><div class="gv-header-text"><h3 class="gv-title" style="font-size:12px;">Starter</h3></div></div>
        <div class="gv-row-cell" role="columnheader"><span class="gv-recommended-label">Recommended</span><div class="gv-header-text"><h3 class="gv-title" style="font-size:12px;">Business</h3></div></div>
      </div>
    </div></div></div></header>
    <div class="gv-table-body"><section class="gv-table-section" role="rowgroup"><div class="gv-rows">
      <div class="gv-table-row" role="row">
        <div class="gv-row-header" role="rowheader"><span class="gv-row-title">SSL</span></div>
        <div class="gv-row-cells">
          <div class="gv-row-cell" role="cell">{ic('check_circle','gv-available')}</div>
          <div class="gv-row-cell" role="cell">{ic('check_circle','gv-available')}</div>
        </div>
      </div>
    </div></section></div>
  </div>
</div>''',

'content-container': f'''<div class="gv-content-container gv-p-lg gv-stack-space-sm" style="width:100%;max-width:260px;">
  <h3 class="gv-heading-xs">Content container</h3>
  <p class="gv-text-sm">Provides background, border, radius and shadow.</p>
  <div class="gv-notice gv-notice-addon gv-notice-info">{ic('info','gv-notice-icon')}<p class="gv-notice-content">Info notice inside</p></div>
</div>''',

'conversational-ai': f'''<div style="width:100%;max-width:260px;display:flex;flex-direction:column;gap:0;">
  <section class="gv-chat"><ul class="gv-chat-list">
    <li class="gv-chat-message gv-chat-outgoing"><div class="gv-meta"><span class="gv-meta-user">You</span></div><p class="gv-chat-message-body">Build me a landing page.</p></li>
    <li class="gv-chat-message gv-chat-incoming"><div class="gv-meta"><span class="gv-meta-user">Aida</span></div><p class="gv-chat-message-body">Sure! What's the main goal?</p></li>
  </ul></section>
  <div class="gv-form-option gv-input-ai"><div class="gv-input gv-input-textarea"><textarea placeholder="Reply…" rows="1"></textarea>
    <div class="gv-input-toolbar gv-mode-condensed" role="toolbar"><div class="gv-toolbar-end"><button type="button" class="gv-button gv-button-icon gv-button-primary" aria-label="Send">{ic('arrow_forward')}</button></div></div>
  </div></div>
</div>''',

'data-table': f'''<div class="gv-data-table" style="width:100%;font-size:12px;">
  <table>
    <thead><tr><th scope="col"><input type="checkbox" class="gv-checkbox gv-mode-condensed"/></th><th>Domain</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td><input type="checkbox" class="gv-checkbox gv-mode-condensed"/></td><td>example.com</td><td><div class="gv-badge gv-badge-success">Active</div></td></tr>
      <tr><td><input type="checkbox" class="gv-checkbox gv-mode-condensed"/></td><td>myshop.one</td><td><div class="gv-badge gv-badge-warning">Expiring</div></td></tr>
    </tbody>
  </table>
</div>''',

'divider': f'''<div style="display:flex;flex-direction:column;gap:16px;width:100%;padding:0 8px;">
  <div class="gv-divider"></div>
  <div style="display:flex;align-items:center;gap:12px;"><span class="gv-text-sm">Left</span><div class="gv-divider" style="flex:1;"></div><span class="gv-text-sm">Right</span></div>
  <div class="gv-divider-button"><div class="gv-divider" aria-hidden="true"></div><button type="button" class="gv-button gv-button-secondary gv-mode-condensed">{ic('add')}<span>Add</span></button><div class="gv-divider" aria-hidden="true"></div></div>
</div>''',

'donut-chart': f'''<div style="display:flex;gap:16px;align-items:center;">
  <div class="gv-donut-chart"><div class="gv-progress-circle" data-progress-percent="0" role="meter" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"><gv-indicator src="{CDN}/indicators/progress-circle.svg" aria-hidden="true"></gv-indicator><span>—</span></div></div>
  <div class="gv-donut-chart"><div class="gv-progress-circle gv-state-success" data-progress-percent="40" role="meter" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"><gv-indicator src="{CDN}/indicators/progress-circle.svg" aria-hidden="true"></gv-indicator><span>40</span></div></div>
  <div class="gv-donut-chart"><div class="gv-progress-circle gv-state-success" data-progress-percent="90" role="meter" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"><gv-indicator src="{CDN}/indicators/progress-circle.svg" aria-hidden="true"></gv-indicator><span>90</span></div></div>
</div>''',

'footer': f'''<footer class="gv-footer" style="width:100%;position:relative;">
  <div class="gv-footer-bar"><div class="gv-footer-content">
    <ul class="gv-footer-links"><li><a href="#">Terms</a></li><li><a href="#">Privacy</a></li><li><a href="#">Cookies</a></li></ul>
    <div class="gv-footer-copyright">© 2026 group.one</div>
  </div></div>
</footer>''',

'header': f'''<header class="gv-main-header" style="position:relative;width:100%;">
  <div class="gv-header-nav">
    <div class="gv-nav-left"><a class="gv-logo" href="#" aria-label="Home">{logo('group-one')}</a></div>
    <nav class="gv-nav-links"><ul><li class="gv-active"><a href="#">Home</a></li><li><a href="#">Domains</a></li><li><a href="#">Hosting</a></li></ul></nav>
  </div>
</header>''',

'input-ai': f'''<div class="gv-form-option gv-input-ai" style="width:100%;max-width:280px;">
  <div class="gv-input gv-input-textarea"><textarea placeholder="Ask Aida anything…" rows="2"></textarea>
    <div class="gv-input-toolbar gv-mode-condensed" role="toolbar"><div class="gv-toolbar-end"><button type="button" class="gv-button gv-button-icon gv-button-primary" aria-label="Send">{ic('arrow_forward')}</button></div></div>
  </div>
  <span class="gv-input-message gv-message-info">AI-generated replies may not always be accurate.</span>
</div>''',

'input-autocomplete': f'''<div class="gv-form-option gv-autocomplete" style="width:100%;max-width:240px;">
  <label class="gv-label" for="idx-ac">Domain extension</label>
  <div class="gv-input gv-with-addon">
    <input id="idx-ac" type="text" placeholder=".com, .net, .one…" />
    <button type="button" class="gv-addon" aria-label="Open">{ic('expand_more')}</button>
  </div>
</div>''',

'input-character-counter': f'''<div class="gv-form-option" style="width:100%;max-width:240px;">
  <label class="gv-label" for="idx-cc">Meta description</label>
  <div class="gv-char-counter-input"><input type="text" id="idx-cc" class="gv-input" placeholder="Describe your page…" maxlength="160"/></div>
  <div class="gv-char-counter-info"><div class="gv-char-counter"><span class="gv-char-total">0</span><span>/</span><span class="gv-char-max">160</span></div></div>
</div>''',

'input-date': f'''<div style="display:flex;flex-direction:column;gap:10px;width:100%;max-width:200px;">
  <div class="gv-input gv-input-date gv-with-addon"><input type="date"/><div class="gv-addon">{ic('date_range')}</div></div>
  <div class="gv-input gv-input-date gv-with-addon"><input type="time"/><div class="gv-addon">{ic('schedule')}</div></div>
</div>''',

'input-general': f'''<div style="display:flex;flex-direction:column;gap:10px;width:100%;max-width:240px;">
  <input type="text" class="gv-input" placeholder="Default input"/>
  <input type="text" class="gv-input gv-error" value="Error state"/>
  <div class="gv-input gv-with-addon"><input type="text" placeholder="With prefix"/><div class="gv-prefix">https://</div></div>
</div>''',

'input-number': f'''<div class="gv-input gv-input-number">
  <button type="button" class="gv-subtract" aria-label="Decrease">{ic('remove')}</button>
  <input type="number" value="3"/>
  <button type="button" class="gv-add" aria-label="Increase">{ic('add')}</button>
</div>''',

'input-search': f'''<div class="gv-input gv-input-search" style="width:100%;max-width:240px;">
  <input type="search" placeholder="Search domains…"/>
  <button type="button" class="gv-addon" aria-label="Search">{ic('search')}</button>
</div>''',

'input-select': f'''<div style="display:flex;flex-direction:column;gap:10px;width:100%;max-width:220px;">
  <div class="gv-input gv-input-select"><select><option>Choose a plan</option><option>Starter</option><option>Business</option></select>{ic('expand_more')}</div>
</div>''',

'input-textarea': f'''<div class="gv-input gv-input-textarea" style="width:100%;max-width:260px;">
  <textarea placeholder="Enter your message here…" rows="3"></textarea>
</div>''',

'legend': f'''<div class="gv-legend" style="width:100%;max-width:240px;">
  <ul class="gv-legend-bar">
    <li>{ic('remove','gv-legend-normal')}<span>Normal</span></li>
    <li>{ic('dangerous','gv-legend-poor')}<span>Poor</span></li>
    <li>{ic('warning','gv-legend-improve')}<span>Improve</span></li>
    <li>{ic('check_circle','gv-legend-good')}<span>Good</span></li>
  </ul>
</div>''',

'list': f'''<div style="display:flex;gap:24px;align-items:flex-start;">
  <ul class="gv-list-items gv-list-check gv-mode-condensed"><li>Free SSL</li><li>Daily backups</li><li>99.9% uptime</li></ul>
  <ul class="gv-list-items gv-list-bullet gv-mode-condensed"><li>10 GB storage</li><li>5 websites</li><li>SSH access</li></ul>
</div>''',

'list-table': f'''<div class="gv-list-table" style="width:100%;font-size:12px;">
  <div class="gv-list-row gv-list-header"><span>Name</span><span>Type</span><span>Status</span></div>
  <div class="gv-list-row"><span>example.com</span><span>.com</span><span><div class="gv-badge gv-badge-success">Active</div></span></div>
  <div class="gv-list-row"><span>mysite.one</span><span>.one</span><span><div class="gv-badge gv-badge-warning">Expiring</div></span></div>
</div>''',

'loader': f'''<div style="display:flex;gap:24px;align-items:center;">
  <gv-loader src="{CDN}/loaders/spinner.svg"></gv-loader>
  <div class="gv-loader-container"><gv-loader src="{CDN}/loaders/spinner.svg"></gv-loader><p style="font-size:12px;">Loading…</p></div>
</div>''',

'modal': f'''<div class="gv-modal-content" style="position:relative;max-width:240px;width:100%;" role="dialog" aria-labelledby="pi-mdemo" aria-modal="true">
  <button type="button" class="gv-modal-close" aria-label="Close">{ic('close')}</button>
  <div class="gv-modal-body"><h2 id="pi-mdemo" class="gv-modal-title">Confirm action</h2><p>Are you sure you want to continue?</p></div>
  <div class="gv-button-group"><button type="button" class="gv-button gv-button-cancel gv-mode-condensed">Cancel</button><button type="button" class="gv-button gv-button-primary gv-mode-condensed">Confirm</button></div>
</div>''',

'navigation': f'''<nav class="gv-global-nav" aria-label="App nav">
  <ul class="gv-nav-list">
    <li><button type="button" class="gv-nav-item gv-active" aria-label="Dashboard" aria-pressed="true">{ic('view_comfy')}</button></li>
    <li><button type="button" class="gv-nav-item" aria-label="Storefront">{ic('storefront')}</button></li>
    <li><button type="button" class="gv-nav-item" aria-label="Domains">{ic('language')}</button></li>
    <li><button type="button" class="gv-nav-item" aria-label="Mail">{ic('mail')}</button></li>
  </ul>
</nav>''',

'notice': f'''<div style="display:flex;flex-direction:column;gap:6px;width:100%;padding:0 8px;">
  <div class="gv-notice gv-notice-info gv-mode-condensed">{ic('info','gv-notice-icon')}<p class="gv-notice-content">Info notice</p></div>
  <div class="gv-notice gv-notice-success gv-mode-condensed">{ic('check_circle','gv-notice-icon')}<p class="gv-notice-content">Success</p></div>
  <div class="gv-notice gv-notice-warning gv-mode-condensed">{ic('warning','gv-notice-icon')}<p class="gv-notice-content">Warning</p></div>
  <div class="gv-notice gv-notice-alert gv-mode-condensed">{ic('error','gv-notice-icon')}<p class="gv-notice-content">Alert</p></div>
</div>''',

'option-group': f'''<div class="gv-option-group gv-mode-condensed" style="width:100%;max-width:220px;">
  <fieldset class="gv-options">
    <div class="gv-label gv-option-group-label"><legend>Features</legend></div>
    <div class="gv-form-option gv-option-group-types">
      <label class="gv-option-inline"><input type="checkbox" class="gv-checkbox" checked/><span class="gv-label">Free SSL</span></label>
      <label class="gv-option-inline"><input type="checkbox" class="gv-checkbox"/><span class="gv-label">Daily backups</span></label>
      <label class="gv-option-inline"><input type="checkbox" class="gv-checkbox" checked/><span class="gv-label">CDN</span></label>
    </div>
  </fieldset>
</div>''',

'overlay': f'''<div style="position:relative;min-height:100px;width:100%;overflow:hidden;border-radius:8px;">
  <div style="padding:12px;position:relative;z-index:2;"><p class="gv-text-sm" style="color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.5);">Content behind overlay</p></div>
  <div class="gv-overlay gv-state-open" style="position:absolute;inset:0;opacity:.6;"></div>
</div>''',

'page-header': f'''<div class="gv-page-header gv-header" style="width:100%;">
  <div class="gv-header-content">
    <div class="gv-content"><h1 class="gv-title" style="font-size:18px;">Domains</h1><h2 class="gv-subtitle" style="font-size:13px;">Manage your domains</h2></div>
    <div class="gv-button-group"><button type="button" class="gv-button gv-button-primary gv-mode-condensed">{ic('add')}<span>Register</span></button></div>
  </div>
  <div class="gv-header-status"><div class="gv-status">{ic('vitals')}<div class="gv-text"><span class="gv-title">Active</span><span class="gv-separator">:</span><span class="gv-value">12</span></div></div></div>
</div>''',

'product-table': f'''<div class="gv-table-col" style="font-size:12px;max-width:180px;">
  <div class="gv-header-text"><h3 class="gv-title" style="font-size:14px;">Business</h3><p class="gv-subtitle" style="font-size:11px;">For growing businesses</p></div>
  <div class="gv-order-details" style="margin-top:8px;"><div class="gv-order-product-button">
    <div class="gv-price-container"><div class="gv-price-main"><div class="gv-price"><span class="gv-price-text">€ 9,-</span><span class="gv-period">/mo</span></div></div></div>
    <button type="button" class="gv-button gv-button-cta gv-mode-condensed">Select</button>
  </div></div>
  <div class="gv-section-key-features" style="margin-top:8px;"><ul class="gv-features-list">
    <li class="gv-feature-item gv-key-feature">{ic('check_circle')}<div class="gv-content"><span class="gv-text">50 GB SSD</span></div></li>
    <li class="gv-feature-item gv-key-feature">{ic('check_circle')}<div class="gv-content"><span class="gv-text">5 websites</span></div></li>
  </ul></div>
</div>''',

'quantity-select': f'''<div class="gv-input-quantity-select" style="width:100%;max-width:220px;">
  <div class="gv-header"><span class="gv-title">CPU cores</span></div>
  <div class="gv-input-quantity-items">
    <div class="gv-input-quantity-item"><label><input type="radio" name="pi-qty" value="2" checked/><span class="gv-content"><span class="gv-amount">2</span></span></label></div>
    <div class="gv-input-quantity-item"><label><input type="radio" name="pi-qty" value="4"/><span class="gv-content"><span class="gv-amount">4</span></span></label></div>
    <div class="gv-input-quantity-item"><label><input type="radio" name="pi-qty" value="8"/><span class="gv-content"><span class="gv-amount">8</span></span></label></div>
  </div>
</div>''',

'radio': f'''<div style="display:flex;flex-direction:column;gap:10px;align-items:flex-start;">
  <label style="display:flex;gap:8px;align-items:center;"><input type="radio" name="pi-r" class="gv-radio" checked/> Monthly billing</label>
  <label style="display:flex;gap:8px;align-items:center;"><input type="radio" name="pi-r" class="gv-radio"/> Annual (save 20%)</label>
  <label style="display:flex;gap:8px;align-items:center;"><input type="radio" name="pi-r" class="gv-radio" disabled/> Disabled option</label>
</div>''',

'resource': f'''<div style="display:flex;flex-direction:column;gap:12px;width:100%;max-width:240px;padding:0 4px;">
  <div class="gv-resource"><div class="gv-progress" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"><div class="gv-bar" style="width:40%"></div></div><div class="gv-content"><span class="gv-amount">240 GB</span><span class="gv-description">of 600 GB used</span></div></div>
  <div class="gv-resource"><div class="gv-progress" role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100"><div class="gv-bar gv-alert" style="width:85%"></div></div><div class="gv-content"><span class="gv-amount">8.5 GB</span><span class="gv-description">of 10 GB (alert)</span></div></div>
</div>''',

'sidedrawer': f'''<div style="position:relative;min-height:160px;width:100%;overflow:hidden;">
  <p class="gv-text-sm gv-text-secondary" style="padding:12px;">← Page behind drawer</p>
  <div class="gv-sidedrawer gv-state-open" style="position:absolute;top:0;right:0;bottom:0;z-index:10;">
    <div class="gv-side-content gv-pos-right">
      <button type="button" class="gv-btn-close" aria-label="Close">{ic('close')}</button>
      <div class="gv-side-account"><div class="gv-account-info"><span class="gv-name">Danilo Merea</span><span class="gv-sub">danilo@group.one</span></div></div>
      <div class="gv-side-menu"><nav class="gv-side-nav"><ul>
        <li><a href="#" class="gv-nav-item gv-active">{ic('account_circle')}<span>My info</span></a></li>
        <li><a href="#" class="gv-nav-item">{ic('logout')}<span>Logout</span></a></li>
      </ul></nav></div>
    </div>
  </div>
</div>''',

'skeleton': f'''<div style="display:flex;flex-direction:column;gap:8px;width:100%;max-width:240px;">
  <div class="gv-skeleton" style="height:18px;width:55%;"></div>
  <div class="gv-skeleton" style="height:13px;"></div>
  <div class="gv-skeleton" style="height:13px;width:85%;"></div>
  <div class="gv-skeleton" style="height:13px;width:70%;"></div>
  <div class="gv-skeleton gv-radius-0" style="height:56px;margin-top:4px;"></div>
</div>''',

'stepper': f'''<nav class="gv-stepper" aria-label="Checkout" style="position:relative;width:100%;max-width:280px;">
  <ol>
    <li class="gv-step gv-step-done"><a href="#" class="gv-step-content"><span class="gv-sr-only">Step 1 done</span><div class="gv-step-type" aria-hidden="true">{ic('check')}<span class="gv-step-nr">1</span></div><div class="gv-step-label" aria-hidden="true">Domain</div></a><div class="gv-step-line" aria-hidden="true"></div></li>
    <li class="gv-step gv-step-current"><div class="gv-step-content" aria-current="step"><span class="gv-sr-only">Step 2 current</span><div class="gv-step-type" aria-hidden="true">{ic('check')}<span class="gv-step-nr">2</span></div><div class="gv-step-label" aria-hidden="true">Extras</div></div><div class="gv-step-line" aria-hidden="true"></div></li>
    <li class="gv-step gv-step-last"><div class="gv-step-content"><span class="gv-sr-only">Step 3</span><div class="gv-step-type" aria-hidden="true">{ic('check')}<span class="gv-step-nr">3</span></div><div class="gv-step-label" aria-hidden="true">Payment</div></div></li>
  </ol>
</nav>''',

'sticky': f'''<div style="display:flex;flex-direction:column;gap:0;width:100%;">
  <div class="gv-sticky-content gv-state-open" style="position:relative;display:flex;align-items:center;padding:10px 16px;gap:12px;background:var(--color-surface-bright);">
    <span class="gv-text-sm gv-text-bold">example.com</span>
    <div class="gv-badge gv-badge-discount">€ 9,-/mo</div>
    <div style="margin-left:auto;"><button type="button" class="gv-button gv-button-cta gv-mode-condensed">Order now</button></div>
  </div>
  <p class="gv-text-sm gv-text-secondary" style="padding:8px 16px;font-size:11px;">↑ appears after scroll</p>
</div>''',

'system-wide-banner': f'''<div style="display:flex;flex-direction:column;gap:4px;width:100%;">
  <div class="gv-notice gv-system-wide">{ic('error','gv-notice-icon')}<p class="gv-notice-content">Scheduled maintenance tonight at 23:00.</p><button type="button" class="gv-notice-close" aria-label="Close">{ic('close')}</button></div>
  <div class="gv-notice gv-system-wide gv-notice-warning">{ic('warning','gv-notice-icon')}<p class="gv-notice-content">Your SSL expires in 3 days.</p><button type="button" class="gv-notice-close" aria-label="Close">{ic('close')}</button></div>
</div>''',

'tabs': f'''<div style="display:flex;flex-direction:column;align-items:flex-start;width:100%;max-width:280px;">
  <div class="gv-scroll-row" style="width:100%;"><div class="gv-section-controls gv-section-tablist" role="tablist" aria-label="Plans">
    <button role="tab" class="gv-tab gv-control gv-tab-active" aria-selected="true" aria-controls="pi-tp1"><span class="gv-tab-content">Starter</span></button>
    <button role="tab" class="gv-tab gv-control" aria-selected="false" aria-controls="pi-tp2"><span class="gv-tab-content">Business</span></button>
    <button role="tab" class="gv-tab gv-control" aria-selected="false" aria-controls="pi-tp3"><span class="gv-tab-content">Enterprise</span></button>
  </div></div>
  <div id="pi-tp1" role="tabpanel" class="gv-tab-panel gv-panel-active" style="padding:12px 0;"><p class="gv-text-sm">10 GB · 1 website · Free SSL</p></div>
  <div id="pi-tp2" role="tabpanel" class="gv-tab-panel" style="padding:12px 0;"><p class="gv-text-sm">50 GB · 5 websites · Priority support</p></div>
  <div id="pi-tp3" role="tabpanel" class="gv-tab-panel" style="padding:12px 0;"><p class="gv-text-sm">Unlimited · Dedicated SLA</p></div>
</div>''',

'toggle': f'''<div style="display:flex;flex-direction:column;gap:12px;align-items:flex-start;">
  <label style="display:flex;gap:10px;align-items:center;"><div class="gv-toggle"><input type="checkbox" id="pi-tg1"/><div class="gv-toggle-slider"></div></div> Off</label>
  <label style="display:flex;gap:10px;align-items:center;"><div class="gv-toggle"><input type="checkbox" id="pi-tg2" checked/><div class="gv-toggle-slider"></div></div> On</label>
  <label style="display:flex;gap:10px;align-items:center;"><div class="gv-toggle"><input type="checkbox" id="pi-tg3" disabled/><div class="gv-toggle-slider"></div></div> Disabled</label>
</div>''',

'tooltip': f'''<div style="display:flex;gap:32px;justify-content:center;padding-top:32px;">
  <div class="gv-tooltip-container gv-tooltip-top-center"><button class="gv-tooltip-button" aria-label="Info" aria-describedby="pi-tt1">{ic('info')}</button><div id="pi-tt1" class="gv-tooltip gv-arrow-bottom-center" role="tooltip"><p>Top center</p></div></div>
  <div class="gv-tooltip-container gv-tooltip-top-left"><button class="gv-tooltip-button gv-text-dotted" aria-describedby="pi-tt2"><span>Hover me</span></button><div id="pi-tt2" class="gv-tooltip gv-arrow-bottom-left" role="tooltip"><p>Dotted trigger</p></div></div>
</div>''',
}

# ── Shared JS ─────────────────────────────────────────────────────────
SHARED_JS = '''
<script>
document.querySelectorAll('.gv-acc-trigger').forEach(t => {
  t.addEventListener('click', () => {
    const open = t.getAttribute('aria-expanded') === 'true';
    t.closest('.gv-accordion')?.querySelectorAll('.gv-acc-trigger').forEach(x => {
      x.classList.remove('gv-expanded'); x.setAttribute('aria-expanded','false');
      const b = document.getElementById(x.getAttribute('aria-controls'));
      if (b) b.classList.add('gv-hidden');
    });
    if (!open) {
      t.classList.add('gv-expanded'); t.setAttribute('aria-expanded','true');
      const b = document.getElementById(t.getAttribute('aria-controls'));
      if (b) b.classList.remove('gv-hidden');
    }
  });
});
document.querySelectorAll('[role="tablist"]').forEach(tl => {
  tl.querySelectorAll('[role="tab"]').forEach(tab => {
    tab.addEventListener('click', () => {
      tl.querySelectorAll('[role="tab"]').forEach(x => { x.classList.remove('gv-tab-active'); x.setAttribute('aria-selected','false'); });
      tab.classList.add('gv-tab-active'); tab.setAttribute('aria-selected','true');
      const panel = document.getElementById(tab.getAttribute('aria-controls'));
      tl.closest('[class]')?.querySelectorAll('.gv-tab-panel').forEach(p => p.classList.remove('gv-panel-active'));
      if (panel) panel.classList.add('gv-panel-active');
    });
  });
});
document.querySelectorAll('.gv-chip:not(.gv-chip-radio)').forEach(c => c.addEventListener('click', () => c.classList.toggle('gv-chip-active')));
document.querySelectorAll('.gv-chip-radio').forEach(c => {
  c.addEventListener('click', () => {
    c.closest('div')?.querySelectorAll('.gv-chip-radio').forEach(x => x.classList.remove('gv-chip-active'));
    c.classList.add('gv-chip-active');
  });
});
document.querySelectorAll('.gv-char-counter-input input, .gv-char-counter-input textarea').forEach(input => {
  const counter = input.closest('.gv-form-option')?.querySelector('.gv-char-total');
  if (counter) input.addEventListener('input', () => counter.textContent = input.value.length);
});
// sidebar scroll-spy
const navLinks = document.querySelectorAll('.gv-side-nav a.gv-nav-item');
if (navLinks.length) {
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        navLinks.forEach(l => l.classList.remove('gv-active'));
        const a = document.querySelector(`.gv-side-nav a[href="#${e.target.id}"]`);
        if (a) a.classList.add('gv-active');
      }
    });
  }, { rootMargin: '-72px 0px -55% 0px' });
  document.querySelectorAll('section[id], div[id]').forEach(s => obs.observe(s));
}
// index filter chips
const filterBtns = document.querySelectorAll('[data-filter]');
const indexCards = document.querySelectorAll('[data-cat]');
filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('gv-chip-active'));
    btn.classList.add('gv-chip-active');
    const f = btn.dataset.filter;
    indexCards.forEach(c => { c.style.display = (!f || f === 'all' || c.dataset.cat === f) ? '' : 'none'; });
    document.querySelectorAll('.cat-heading').forEach(h => {
      if (!f || f === 'all') { h.style.display = ''; return; }
      h.style.display = h.dataset.cat === f ? '' : 'none';
    });
  });
});
// index search
const searchInput = document.getElementById('index-search');
if (searchInput) {
  searchInput.addEventListener('input', () => {
    const q = searchInput.value.toLowerCase();
    indexCards.forEach(c => {
      const name = c.querySelector('.card-name')?.textContent.toLowerCase() || '';
      c.style.display = name.includes(q) ? '' : 'none';
    });
  });
}
</script>'''

# ── Page templates ────────────────────────────────────────────────────
def head(title, depth='..'):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} — Gravity Components</title>
  <link rel="stylesheet" href="{CDN}/css/brands/group-one.min.css"/>
  <script type="module" src="{CDN}/index.umd.js"></script>
  <link rel="stylesheet" href="{depth}/src/styles.css"/>
  <link rel="stylesheet" href="{depth}/src/comp-page.css"/>
</head>'''

def nav_header(depth='..'):
    return f'''  <a href="#main-content" class="gv-skip-link">Skip to main content</a>
  <header class="gv-main-header">
    <div class="gv-header-nav">
      <div class="gv-nav-left">
        <a href="{depth}/index.html" class="gv-logo" aria-label="Gravity Components">
          <gv-logo src="{CDN}/logos/group-one.svg"></gv-logo>
        </a>
      </div>
      <nav class="gv-nav-links"><ul>
        <li class="gv-active"><a href="{depth}/index.html">Components</a></li>
        <li><a href="{depth}/icons.html">Icons</a></li>
        <li><a href="{DOCS}" target="_blank">Gravity Docs ↗</a></li>
      </ul></nav>
      <div class="gv-nav-menu">
        <div class="gv-badge gv-badge-info">v5.38.6</div>
      </div>
    </div>
  </header>'''

def icons_section(icon_names):
    if not icon_names:
        return ''
    tiles = '\n'.join(f'''    <div class="icon-tile">
      <gv-icon aria-hidden="true" src="{CDN}/icons/{n}.svg"></gv-icon>
      <span class="icon-name">{n}</span>
    </div>''' for n in icon_names)
    return f'''<div class="icons-section" id="cdn-icons">
  <h2>CDN Icons used</h2>
  <p class="section-sub">Copy the src path to use in your own components.</p>
  <div class="icons-grid">
{tiles}
  </div>
</div>'''

def code_block(code_str):
    escaped = html.escape(code_str)
    return f'''<div class="code-block">
  <details>
    <summary>Show HTML</summary>
    <pre><code>{escaped}</code></pre>
  </details>
</div>'''

# ── Generate INDEX ────────────────────────────────────────────────────
def gen_index():
    cats = [('component','Components'), ('form','Form Components'), ('ai','AI Components')]
    sections = ''
    for cat_key, cat_label in cats:
        comps_in_cat = [(n,s,cls,dp,cat,desc,icons) for n,s,cls,dp,cat,desc,icons in COMPONENTS if cat == cat_key]
        if not comps_in_cat:
            continue
        cards = ''
        for name, slug, cls, dp, cat, desc, icons in comps_in_cat:
            preview_html = PREVIEW.get(slug, f'<span class="gv-text-secondary gv-text-sm">{name}</span>')
            cards += f'''      <a class="index-card" href="components/{slug}.html" data-cat="{cat}">
        <div class="card-preview">{preview_html}</div>
        <div class="card-meta">
          <span class="card-name">{name}</span>
          <span class="card-arrow">→</span>
        </div>
      </a>
'''
        sections += f'''
    <p class="cat-heading" id="cat-{cat_key}" data-cat="{cat_key}">{cat_label}</p>
    <div class="comp-grid" style="margin-bottom:8px;">
{cards}    </div>
'''

    total = len(COMPONENTS)
    return f'''{head('Overview', '.')}
<body class="gv-activated gv-pt-nav gv-full-page">
{nav_header('.')}
  <main id="main-content" class="gv-surface-dim gv-flex gv-flex-1">
    <div class="gv-flex gv-flex-1 gv-mx-auto gv-w-max-container">

      <!-- Sidebar -->
      <div class="page-sidebar gv-sidebar gv-max-tab-hidden" style="min-width:200px;padding:24px 0;">
        <div class="gv-side-menu">
          <div class="gv-side-label">Categories</div>
          <nav class="gv-side-nav"><ul>
            <li><a href="#cat-component" class="gv-nav-item"><gv-icon aria-hidden="true" src="{CDN}/icons/dashboard.svg"></gv-icon><span>Components</span></a></li>
            <li><a href="#cat-form" class="gv-nav-item"><gv-icon aria-hidden="true" src="{CDN}/icons/edit_note.svg"></gv-icon><span>Form</span></a></li>
            <li><a href="#cat-ai" class="gv-nav-item"><gv-icon aria-hidden="true" src="{CDN}/icons/auto_awesome.svg"></gv-icon><span>AI</span></a></li>
          </ul></nav>
        </div>
      </div>

      <!-- Content -->
      <div class="gv-flex-1 gv-p-fluid" style="min-width:0;padding-top:32px;padding-bottom:64px;">

        <div class="index-hero">
          <h1 class="gv-heading-xxl">Gravity Component Overview</h1>
          <p class="gv-text-lg gv-text-secondary">All {total} components — live previews, CDN v5.38.6. Click any card to open the full component page.</p>
        </div>

        <div class="index-search-bar">
          <div class="gv-input gv-input-search" style="max-width:280px;">
            <input type="search" id="index-search" placeholder="Search components…"/>
            <button type="button" class="gv-addon" aria-label="Search"><gv-icon aria-hidden="true" src="{CDN}/icons/search.svg"></gv-icon></button>
          </div>
          <div class="index-filters">
            <button type="button" class="gv-chip gv-chip-radio gv-chip-active" data-filter="all">All</button>
            <button type="button" class="gv-chip gv-chip-radio" data-filter="component">Components</button>
            <button type="button" class="gv-chip gv-chip-radio" data-filter="form">Form</button>
            <button type="button" class="gv-chip gv-chip-radio" data-filter="ai">AI</button>
          </div>
        </div>
{sections}
      </div>
    </div>
  </main>
{SHARED_JS}
</body>
</html>'''

# ── Generate COMPONENT PAGE ───────────────────────────────────────────
def gen_component_page(idx, comp_data):
    name, slug, cls, dp, cat, desc, icon_names = comp_data
    docs_url = DOCS + dp
    badge_cls = CAT_BADGE[cat]
    cat_label = CAT_LABEL[cat]

    # prev / next
    prev_comp = COMPONENTS[idx - 1] if idx > 0 else None
    next_comp = COMPONENTS[idx + 1] if idx < len(COMPONENTS) - 1 else None
    prev_link = f'<a href="{prev_comp[1]}.html">{ic("arrow_back")} {prev_comp[0]}</a>' if prev_comp else '<span></span>'
    next_link = f'<a href="{next_comp[1]}.html" class="next">{next_comp[0]} {ic("arrow_forward")}</a>' if next_comp else '<span></span>'

    # sidebar links
    sidebar_items = f'''<li><a href="#demo-main" class="gv-nav-item">{ic('play_circle')}<span>Demo</span></a></li>
            <li><a href="#demo-variants" class="gv-nav-item">{ic('grid_view')}<span>Variants</span></a></li>'''
    if icon_names:
        icon_img = ic('image')
        sidebar_items += f'\n            <li><a href="#cdn-icons" class="gv-nav-item">{icon_img}<span>CDN Icons</span></a></li>'

    preview_html = PREVIEW.get(slug, f'<span class="gv-text-secondary">{name}</span>')
    icons_html = icons_section(icon_names)
    code_snippet = code_block(preview_html)

    return f'''{head(name)}
<body class="gv-activated gv-pt-nav gv-full-page">
{nav_header()}
  <main id="main-content" class="gv-surface-dim gv-flex gv-flex-1">
    <div class="gv-flex gv-flex-1 gv-mx-auto gv-w-max-container">

      <!-- Sidebar -->
      <div class="page-sidebar gv-sidebar gv-max-tab-hidden" style="min-width:200px;padding:24px 0;">
        <div class="gv-side-menu">
          <div class="gv-side-label">On this page</div>
          <nav class="gv-side-nav"><ul>
            {sidebar_items}
          </ul></nav>
        </div>
      </div>

      <!-- Content -->
      <div class="gv-flex-1 gv-p-fluid" style="min-width:0;padding-top:32px;padding-bottom:64px;">

        <!-- Breadcrumb -->
        <div class="comp-breadcrumb">
          <a href="../index.html">{ic('arrow_back')} All components</a>
          <span class="sep">/</span>
          <span>{name}</span>
        </div>

        <!-- Hero -->
        <div class="comp-page-hero">
          <h1>{name}</h1>
          <div class="hero-meta">
            <div class="gv-badge {badge_cls}">{cat_label}</div>
            <code class="gv-text-sm" style="background:var(--color-surface-dim);padding:2px 8px;border-radius:4px;font-size:12px;">{cls}</code>
            <a href="{docs_url}" target="_blank" class="gv-button gv-button-secondary gv-mode-condensed" style="font-size:12px;">Docs ↗</a>
          </div>
          <p class="comp-desc">{desc}</p>
        </div>

        <!-- Main demo -->
        <div class="demo-section" id="demo-main">
          <h2>Demo</h2>
          <div class="demo-box demo-tall">
            {preview_html}
          </div>
          {code_snippet}
        </div>

        <!-- Variants -->
        <div class="demo-section" id="demo-variants">
          <h2>Variants</h2>
          <div class="variants-grid">
            {_variants(slug, name, cls)}
          </div>
        </div>

        <!-- CDN Icons -->
        {icons_html}

        <!-- Prev / Next -->
        <div class="comp-prev-next">
          {prev_link}
          {next_link}
        </div>

      </div>
    </div>
  </main>
{SHARED_JS}
</body>
</html>'''

def _variants(slug, name, cls):
    """Return 3 variant cards for a component."""
    V = VARIANTS.get(slug)
    if not V:
        # generic fallback
        return f'''<div class="variant-card">
  <div class="variant-preview">{PREVIEW.get(slug,'')}</div>
  <div class="variant-label">Default</div>
</div>'''
    cards = ''
    for label, html_content, extra_cls in V:
        cards += f'''<div class="variant-card">
  <div class="variant-preview {extra_cls}">{html_content}</div>
  <div class="variant-label">{label}</div>
</div>
'''
    return cards

# ── Variant HTML per component ─────────────────────────────────────────
# Each entry: list of (label, html, extra_preview_classes)
VARIANTS = {
'accordion': [
    ('Two items, one open', f'''<div class="gv-accordion" style="width:100%;max-width:240px;">
  <div class="gv-acc-item"><h3 class="gv-acc-header"><button class="gv-acc-trigger gv-expanded" aria-expanded="true" aria-controls="v-a1" id="v-a1t"><span class="gv-acc-title">What is included?</span></button></h3>
  <div id="v-a1" class="gv-acc-body"><div class="gv-acc-content"><p>Free SSL, CDN, and backups.</p></div></div></div>
  <div class="gv-acc-item"><h3 class="gv-acc-header"><button class="gv-acc-trigger" aria-expanded="false" aria-controls="v-a2" id="v-a2t"><span class="gv-acc-title">Can I upgrade?</span></button></h3>
  <div id="v-a2" class="gv-acc-body gv-hidden"><div class="gv-acc-content"><p>Yes, at any time.</p></div></div></div>
</div>''', ''),
    ('Three items collapsed', f'''<div class="gv-accordion" style="width:100%;max-width:240px;">
  {''.join(f"""<div class="gv-acc-item"><h3 class="gv-acc-header"><button class="gv-acc-trigger" aria-expanded="false" aria-controls="v-a{i}b" id="v-a{i}t"><span class="gv-acc-title">Question {i}</span></button></h3><div id="v-a{i}b" class="gv-acc-body gv-hidden"><div class="gv-acc-content"><p>Answer {i}.</p></div></div></div>""" for i in range(3,6))}
</div>''', ''),
    ('Condensed mode', f'''<div class="gv-accordion gv-mode-condensed" style="width:100%;max-width:240px;">
  <div class="gv-acc-item"><h3 class="gv-acc-header"><button class="gv-acc-trigger gv-expanded" aria-expanded="true" aria-controls="v-ac1" id="v-ac1t"><span class="gv-acc-title">Condensed open</span></button></h3>
  <div id="v-ac1" class="gv-acc-body"><div class="gv-acc-content"><p>Compact spacing.</p></div></div></div>
  <div class="gv-acc-item"><h3 class="gv-acc-header"><button class="gv-acc-trigger" aria-expanded="false" aria-controls="v-ac2" id="v-ac2t"><span class="gv-acc-title">Condensed closed</span></button></h3>
  <div id="v-ac2" class="gv-acc-body gv-hidden"><div class="gv-acc-content"><p>Hidden.</p></div></div></div>
</div>''', ''),
],
'badge': [
    ('Status variants', f'''<div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center;">
  <div class="gv-badge gv-badge-generic">Generic</div>
  <div class="gv-badge gv-badge-info">Info</div>
  <div class="gv-badge gv-badge-success">Success</div>
  <div class="gv-badge gv-badge-warning">Warning</div>
  <div class="gv-badge gv-badge-alert">Alert</div>
  <div class="gv-badge gv-badge-discount">-20%</div>
</div>''', ''),
    ('Aida AI badge', f'''<div style="display:flex;flex-direction:column;gap:8px;align-items:center;">
  <div class="gv-badge gv-badge-aida"><gv-logo src="{CDN}/logos/aida.svg" fit="auto" aria-hidden="true"></gv-logo><span class="gv-sr-only">Aida</span><span>AI</span></div>
  <span class="gv-text-sm gv-text-secondary">Aida badge with logo</span>
</div>''', ''),
    ('In context', f'''<div style="display:flex;flex-direction:column;gap:10px;align-items:flex-start;">
  <div style="display:flex;align-items:center;gap:8px;"><span class="gv-text-sm">Domain:</span><div class="gv-badge gv-badge-success">Active</div></div>
  <div style="display:flex;align-items:center;gap:8px;"><span class="gv-text-sm">SSL:</span><div class="gv-badge gv-badge-warning">Expiring</div></div>
  <div style="display:flex;align-items:center;gap:8px;"><span class="gv-text-sm">Backup:</span><div class="gv-badge gv-badge-alert">Failed</div></div>
</div>''', ''),
],
'button': [
    ('All variants', f'''<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;">
  <button type="button" class="gv-button gv-button-primary">Primary</button>
  <button type="button" class="gv-button gv-button-secondary">Secondary</button>
  <button type="button" class="gv-button gv-button-cta">CTA</button>
  <button type="button" class="gv-button gv-button-cancel">Cancel</button>
  <button type="button" class="gv-button gv-button-destructive">Destructive</button>
  <button type="button" class="gv-button gv-button-upgrade">Upgrade</button>
</div>''', ''),
    ('With icons', f'''<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;">
  <button type="button" class="gv-button gv-button-primary gv-mode-condensed">{ic('add')}<span>Register domain</span></button>
  <button type="button" class="gv-button gv-button-secondary gv-mode-condensed">{ic('download')}<span>Export</span></button>
  <button type="button" class="gv-button gv-button-aida gv-mode-condensed">{ic('auto_awesome')}<span>Ask Aida</span></button>
  <button type="button" class="gv-button gv-button-icon gv-button-secondary" aria-label="Delete">{ic('delete')}</button>
</div>''', ''),
    ('Button group', f'''<div style="display:flex;flex-direction:column;gap:12px;align-items:center;">
  <div class="gv-button-group">
    <button type="button" class="gv-button gv-button-cancel gv-mode-condensed">Back</button>
    <button type="button" class="gv-button gv-button-primary gv-mode-condensed">Continue</button>
  </div>
  <div class="gv-button-group">
    <button type="button" class="gv-button gv-button-secondary gv-mode-condensed" disabled>Disabled</button>
    <button type="button" class="gv-button gv-button-primary gv-mode-condensed">Enabled</button>
  </div>
</div>''', ''),
],
'card': [
    ('With tile + action', f'''<div class="gv-card" style="max-width:220px;">
  <div class="gv-card-tile">{tile('wordpress')}</div>
  <div class="gv-card-content"><h3 class="gv-card-title">WordPress</h3><p>One-click install with automatic updates.</p></div>
  <div class="gv-card-footer"><button type="button" class="gv-button gv-button-primary gv-mode-condensed"><span>Install</span>{ic('arrow_forward')}</button></div>
</div>''', ''),
    ('Notice inside card', f'''<div class="gv-card" style="max-width:220px;">
  <div class="gv-card-content">
    <h3 class="gv-card-title">Storage usage</h3>
    <div class="gv-notice gv-notice-warning gv-notice-addon gv-mode-condensed">{ic('warning','gv-notice-icon')}<p class="gv-notice-content">85% used</p></div>
    <p class="gv-text-sm" style="margin-top:8px;">8.5 GB of 10 GB used.</p>
  </div>
</div>''', ''),
    ('Multiple cards', f'''<div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center;">
  {''.join(f"""<div class="gv-card" style="max-width:120px;"><div class="gv-card-tile">{tile('dashboard')}</div><div class="gv-card-content"><h3 class="gv-card-title" style="font-size:12px;">Plan {i}</h3></div></div>""" for i in range(1,4))}
</div>''', ''),
],
'notice': [
    ('All severities', f'''<div style="display:flex;flex-direction:column;gap:8px;width:100%;">
  <div class="gv-notice gv-notice-info">{ic('info','gv-notice-icon')}<p class="gv-notice-content"><strong>Info:</strong> Your domain was registered successfully.</p></div>
  <div class="gv-notice gv-notice-success">{ic('check_circle','gv-notice-icon')}<p class="gv-notice-content"><strong>Success:</strong> SSL installed.</p></div>
  <div class="gv-notice gv-notice-warning">{ic('warning','gv-notice-icon')}<p class="gv-notice-content"><strong>Warning:</strong> SSL expires in 7 days.</p></div>
  <div class="gv-notice gv-notice-alert">{ic('error','gv-notice-icon')}<p class="gv-notice-content"><strong>Alert:</strong> Payment failed.</p></div>
</div>''', 'v-col'),
    ('With action', f'''<div style="display:flex;flex-direction:column;gap:8px;width:100%;">
  <div class="gv-notice gv-notice-upgrade">{ic('gv-custom-upgrade','gv-notice-icon')}<p class="gv-notice-content">Upgrade to Business for more storage.</p><button type="button" class="gv-button gv-button-upgrade gv-mode-condensed">Upgrade</button></div>
  <div class="gv-notice gv-notice-system">{ic('error','gv-notice-icon')}<p class="gv-notice-content">System maintenance scheduled.</p><button type="button" class="gv-button gv-button-cancel gv-mode-condensed">Details</button></div>
</div>''', 'v-col'),
    ('Addon (compact) variant', f'''<div class="gv-content-container gv-p-md" style="width:100%;max-width:280px;">
  <p class="gv-text-sm">Some page content</p>
  <div class="gv-notice gv-notice-addon gv-notice-info" style="margin-top:8px;">{ic('info','gv-notice-icon')}<p class="gv-notice-content">This is an addon notice inside a container.</p></div>
</div>''', ''),
],
'modal': [
    ('Confirmation dialog', f'''<div class="gv-modal-content" style="position:relative;max-width:280px;width:100%;" role="dialog" aria-labelledby="v-m1">
  <button type="button" class="gv-modal-close" aria-label="Close">{ic('close')}</button>
  <div class="gv-modal-body"><h2 id="v-m1" class="gv-modal-title">Delete domain?</h2><p>This action cannot be undone. All associated records will be removed.</p></div>
  <div class="gv-button-group"><button type="button" class="gv-button gv-button-cancel gv-mode-condensed">Cancel</button><button type="button" class="gv-button gv-button-destructive gv-mode-condensed">Delete</button></div>
</div>''', ''),
    ('With icon header', f'''<div class="gv-modal-content" style="position:relative;max-width:280px;width:100%;" role="dialog" aria-labelledby="v-m2">
  <button type="button" class="gv-modal-close" aria-label="Close">{ic('close')}</button>
  <div class="gv-modal-body">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">{ic('check_circle')}<h2 id="v-m2" class="gv-modal-title" style="margin:0;">Domain registered!</h2></div>
    <p>example.com has been registered for 1 year.</p>
  </div>
  <div class="gv-button-group"><button type="button" class="gv-button gv-button-primary gv-mode-condensed">Go to dashboard</button></div>
</div>''', ''),
    ('Form modal', f'''<div class="gv-modal-content" style="position:relative;max-width:280px;width:100%;" role="dialog" aria-labelledby="v-m3">
  <button type="button" class="gv-modal-close" aria-label="Close">{ic('close')}</button>
  <div class="gv-modal-body"><h2 id="v-m3" class="gv-modal-title">Add DNS record</h2>
    <div class="gv-form-option" style="margin-top:12px;"><label class="gv-label">Record type</label>
      <div class="gv-input gv-input-select"><select><option>A</option><option>CNAME</option><option>MX</option></select>{ic('expand_more')}</div>
    </div>
    <div class="gv-form-option" style="margin-top:8px;"><label class="gv-label">Value</label><input type="text" class="gv-input" placeholder="e.g. 1.2.3.4"/></div>
  </div>
  <div class="gv-button-group"><button type="button" class="gv-button gv-button-cancel gv-mode-condensed">Cancel</button><button type="button" class="gv-button gv-button-primary gv-mode-condensed">Save</button></div>
</div>''', ''),
],
'tabs': [
    ('Standard', f'''<div style="display:flex;flex-direction:column;align-items:flex-start;width:100%;max-width:300px;">
  <div class="gv-scroll-row" style="width:100%;"><div class="gv-section-controls gv-section-tablist" role="tablist" aria-label="Settings">
    <button role="tab" class="gv-tab gv-control gv-tab-active" aria-selected="true" aria-controls="v-t1"><span class="gv-tab-content">General</span></button>
    <button role="tab" class="gv-tab gv-control" aria-selected="false" aria-controls="v-t2"><span class="gv-tab-content">Security</span></button>
    <button role="tab" class="gv-tab gv-control" aria-selected="false" aria-controls="v-t3"><span class="gv-tab-content">DNS</span></button>
  </div></div>
  <div id="v-t1" role="tabpanel" class="gv-tab-panel gv-panel-active" style="padding:12px 0;"><p class="gv-text-sm">General settings.</p></div>
  <div id="v-t2" role="tabpanel" class="gv-tab-panel" style="padding:12px 0;"><p class="gv-text-sm">Security settings.</p></div>
  <div id="v-t3" role="tabpanel" class="gv-tab-panel" style="padding:12px 0;"><p class="gv-text-sm">DNS records.</p></div>
</div>''', ''),
    ('5 tabs', f'''<div class="gv-scroll-row" style="width:100%;"><div class="gv-section-controls gv-section-tablist" role="tablist" aria-label="Tabs">
  {''.join(f"""<button role="tab" class="gv-tab gv-control{' gv-tab-active' if i==0 else ''}" aria-selected="{'true' if i==0 else 'false'}"><span class="gv-tab-content">Tab {i+1}</span></button>""" for i in range(5))}
</div></div>''', ''),
    ('With badges', f'''<div class="gv-scroll-row" style="width:100%;"><div class="gv-section-controls gv-section-tablist" role="tablist" aria-label="Queue">
  <button role="tab" class="gv-tab gv-control gv-tab-active" aria-selected="true"><span class="gv-tab-content">Active <div class="gv-badge gv-badge-success" style="margin-left:4px;">12</div></span></button>
  <button role="tab" class="gv-tab gv-control" aria-selected="false"><span class="gv-tab-content">Pending <div class="gv-badge gv-badge-warning" style="margin-left:4px;">3</div></span></button>
  <button role="tab" class="gv-tab gv-control" aria-selected="false"><span class="gv-tab-content">Expired</span></button>
</div></div>''', ''),
],
'input-general': [
    ('States', f'''<div style="display:flex;flex-direction:column;gap:10px;width:100%;">
  <input type="text" class="gv-input" placeholder="Default"/>
  <input type="text" class="gv-input gv-error" value="Error state"/>
  <input type="text" class="gv-input" value="Disabled" disabled/>
  <div class="gv-notice gv-notice-alert gv-mode-condensed" style="font-size:12px;">{ic('error','gv-notice-icon')}<p class="gv-notice-content">This field is required</p></div>
</div>''', 'v-col'),
    ('With addons', f'''<div style="display:flex;flex-direction:column;gap:10px;width:100%;">
  <div class="gv-input gv-with-addon"><div class="gv-prefix">https://</div><input type="text" placeholder="yourdomain.com"/></div>
  <div class="gv-input gv-with-addon"><input type="text" placeholder="Subdomain"/><div class="gv-suffix">.group.one</div></div>
  <div class="gv-input gv-with-addon"><input type="text" placeholder="Search…"/><button type="button" class="gv-addon" aria-label="Search">{ic('search')}</button></div>
</div>''', 'v-col'),
    ('Labeled form field', f'''<div class="gv-form-option" style="width:100%;">
  <label class="gv-label" for="v-ig1">Domain name</label>
  <input type="text" id="v-ig1" class="gv-input" placeholder="e.g. mystore"/>
  <span class="gv-input-message">Minimum 2 characters. Letters, numbers and hyphens only.</span>
</div>''', 'v-col'),
],
'chip': [
    ('Filter chips', f'''<div style="display:flex;flex-direction:column;gap:12px;">
  <p class="gv-text-sm gv-text-secondary">Multi-select</p>
  <div style="display:flex;gap:6px;flex-wrap:wrap;">
    <button type="button" class="gv-chip gv-chip-active">PHP 8.2</button>
    <button type="button" class="gv-chip gv-chip-active">MySQL</button>
    <button type="button" class="gv-chip">PostgreSQL</button>
    <button type="button" class="gv-chip">Redis</button>
  </div>
</div>''', ''),
    ('Radio chips', f'''<div style="display:flex;flex-direction:column;gap:12px;">
  <p class="gv-text-sm gv-text-secondary">Single-select</p>
  <div style="display:flex;gap:6px;flex-wrap:wrap;">
    <button type="button" class="gv-chip gv-chip-radio gv-chip-active">Monthly</button>
    <button type="button" class="gv-chip gv-chip-radio">Quarterly</button>
    <button type="button" class="gv-chip gv-chip-radio">Annual</button>
  </div>
</div>''', ''),
    ('Label chips (read-only)', f'''<div class="gv-chip-labels">
  <div class="gv-item">PHP 8.2</div>
  <div class="gv-item">MySQL 8</div>
  <div class="gv-item">SSL</div>
  <div class="gv-item">CDN</div>
</div>''', ''),
],
}

# ── Fill missing variants with generic fallback ───────────────────────
for name, slug, cls, dp, cat, desc, icons in COMPONENTS:
    if slug not in VARIANTS:
        p = PREVIEW.get(slug, '')
        VARIANTS[slug] = [
            ('Default', p, ''),
            ('Condensed', p.replace('gv-mode-condensed', '').replace('<div class="gv', '<div class="gv').replace('<button type="button" class="gv-button gv-button', '<button type="button" class="gv-button gv-mode-condensed gv-button'), ''),
        ]

# ── Run ───────────────────────────────────────────────────────────────
def main():
    # Write index
    idx_path = os.path.join(OUT, 'index.html')
    with open(idx_path, 'w') as f:
        f.write(gen_index())
    print(f'  ✓ index.html')

    # Write component pages
    comp_dir = os.path.join(OUT, 'components')
    os.makedirs(comp_dir, exist_ok=True)
    for i, comp in enumerate(COMPONENTS):
        slug = comp[1]
        page = gen_component_page(i, comp)
        path = os.path.join(comp_dir, f'{slug}.html')
        with open(path, 'w') as f:
            f.write(page)
        print(f'  ✓ components/{slug}.html')

    print(f'\nDone — {len(COMPONENTS)} component pages + index.html')

if __name__ == '__main__':
    main()
