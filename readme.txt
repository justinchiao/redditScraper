<html lang="en-US" class="theme-beta theme-light"><head>
        <script async="" src="https://www.redditstatic.com/js/tags-slim.js"></script><script>
    var __SUPPORTS_TIMING_API = typeof performance === 'object' && !!performance.mark && !! performance.measure && !!performance.getEntriesByType;
    function __perfMark(name) { __SUPPORTS_TIMING_API && performance.mark(name); };
    var __firstPostLoaded = false;
    function __markFirstPostVisible() {
      if (__firstPostLoaded) { return; }
      __firstPostLoaded = true;
      __perfMark("first_post_title_image_loaded");
    }
    var __firstCommentLoaded = false;
    function __markFirstCommentVisible() {
      if (__firstCommentLoaded) { return; }
      __firstCommentLoaded = true;
      __perfMark("first_comment_loaded");
    }
  </script>
        <script>__perfMark('head_tag_start');</script>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="referrer" content="origin-when-cross-origin">
        <style>
  /* http://meyerweb.com/eric/tools/css/reset/
    v2.0 | 20110126
    License: none (public domain)
  */

  html, body, div, span, applet, object, iframe,
  h1, h2, h3, h4, h5, h6, p, blockquote, pre,
  a, abbr, acronym, address, big, button, cite, code,
  del, dfn, em, img, input, ins, kbd, q, s, samp,
  small, strike, strong, sub, sup, tt, var,
  b, u, i, center,
  dl, dt, dd, ol, ul, li,
  fieldset, form, label, legend,
  table, caption, tbody, tfoot, thead, tr, th, td,
  article, aside, canvas, details, embed,
  figure, figcaption, footer, header, hgroup,
  menu, nav, output, ruby, section, summary,
  time, mark, audio, video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
  }

  /* HTML5 display-role reset for older browsers */
  article, aside, details, figcaption, figure,
  footer, header, hgroup, menu, nav, section {
    display: block;
  }
  body {
    line-height: 1;
    font-family: BentonSans, sans-serif;
  }
  ol, ul {
    list-style: none;
  }
  blockquote, q {
    quotes: none;
  }
  blockquote:before, blockquote:after,
  q:before, q:after {
    content: '';
    content: none;
  }
  table {
    border-collapse: collapse;
    border-spacing: 0;
  }
  a {
    color: inherit;
    text-decoration: inherit;
  }

  html, body {
    width: 100%;
    margin: 0;
  }

  /* HTML5 display-role reset for older browsers */
  article, aside, details, figcaption, figure,
  footer, header, hgroup, menu, nav, section {
    display: block;
  }

  button {
    background: transparent;
    border: none;
    color: inherit;
    cursor: pointer;
    padding: initial;
  }

  body {
    min-height: calc(100vh - 48px);
    line-height: 1;
    font-family: IBMPlexSans, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
  }

  body ::-moz-selection {
    background-color: #7dbcff99;
  }

  input, textarea, [contenteditable] {
    
  font-family: Noto Sans, Arial, sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 21px;

    font-family: inherit;
  }
</style>
        <style data-href="chunkCSS/vendors~Reddit.5e0ee9d505a551167136_.css" data-chunk="Reddit" key="chunkCSS/vendors~Reddit.5e0ee9d505a551167136_.css">faceplate-expandable-section-helper {
  display: contents;
  /* [rpl] just to boost the selector */
  /*
  Target the [open] attribute on either the root element OR the details
  element to rotate the chevron. This is to handle rotating chevrons both
  before and after the faceplate-expandable-section-helper component is defined.
  
  Before the component is defined, the [open] attribute on the component will not
  toggle if the user clicks on details, but the [open] attribute will toggle on
  the details element, so we need to target details too.

  The reason we can't target only the details element is because once the web
  component is defined, we delay toggling the [open] attribute on the details
  element until AFTER the animation finishes. So if we only targeted the details
  element for the chevron rotation the chevron wouldn't rotate until after the
  collapse animation finished and we finally toggle the [open] attriubte on the
  details element.
  */
  /*
    Specific handling for nested menus. We only need to handle collapse menus inside of
    expanded menus, not expanded menus inside collapsed menus because you can't see those!
  */
}
faceplate-expandable-section-helper > details > summary {
  list-style-type: none;
}
faceplate-expandable-section-helper[rpl] > details > summary {
  /* override details.less */
  margin: 0;
}
faceplate-expandable-section-helper > details > summary [icon-name='caret-down-outline'] {
  transition: transform 0.22s ease-in-out;
}
faceplate-expandable-section-helper[open] summary [icon-name='caret-down-outline'],
faceplate-expandable-section-helper:not(:defined) > details[open] summary [icon-name='caret-down-outline'] {
  transform: rotate(180deg);
}
faceplate-expandable-section-helper:not([open]) summary [icon-name='caret-down-outline'],
faceplate-expandable-section-helper:not(:defined) > details:not([open]) summary [icon-name='caret-down-outline'] {
  transform: rotate(0deg);
}
/*
 * This is a Tailwind CSS file, it must be run through the PostCSS compiler
 * with the Tailwind plugin, not Less. The `postcss-import` plugin is also
 * needed, if you have other additions to your Tailwind entry point CSS.
 *
 * @example
 * // tailwind.css
 * @import '@reddit/faceplate/styles/tailwind-components.css'
 * @tailwind components;
 * @tailwind utilities;
 *
 * // styles.less
 * @import (less) '@reddit/faceplate/faceplate.css';
 * @import (less) './tailwind-build.css';
 */
.-translate-y-1\/2, .-translate-x-1\/2, .translate-x-0, .translate-y-md, .rotate-90, .scale-75, .scale-150, .scale-100, .-scale-x-100, .transform {
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
}
.ordinal {
  --tw-ordinal:  ;
  --tw-slashed-zero:  ;
  --tw-numeric-figure:  ;
  --tw-numeric-spacing:  ;
  --tw-numeric-fraction:  ;
}
.shadow-none, .shadow-sm, .shadow-md {
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
}
.ring {
  --tw-ring-inset:  ;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
}
.container {
  width: 100%;
}
.\!container {
  width: 100% !important;
}
@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
  .\!container {
    max-width: 1024px !important;
  }
}
/* Anchor component*/
.a {
    border: var(--line-a-focus) solid transparent;
    border-radius: 2px;
    color: var(--color-a-default);
    font-size: 1em;
    padding: 0 var(--spacer-a-px);
    margin: calc(-1 * var(--line-a-focus)) calc(-1 * (var(--spacer-a-px) + var(--line-a-focus)));
    text-decoration: none;
  }
.\!a {
    border: var(--line-a-focus) solid transparent !important;
    border-radius: 2px !important;
    color: var(--color-a-default) !important;
    font-size: 1em !important;
    padding: 0 var(--spacer-a-px) !important;
    margin: calc(-1 * var(--line-a-focus)) calc(-1 * (var(--spacer-a-px) + var(--line-a-focus))) !important;
    text-decoration: none !important;
  }
.a:hover {
    color: var(--color-a-hover);
  }
.\!a:hover {
    color: var(--color-a-hover) !important;
  }
.a:visited:not(.no-visited),
  .a.visited:not(.no-visited) {
    color: var(--color-a-visited);
  }
.\!a:visited:not(.no-visited),
  .\!a.visited:not(.no-visited) {
    color: var(--color-a-visited) !important;
  }
/* Button component */
.button {
    background: var(--button-color-background);
    border-radius: 999px;
    border: none;
    border: var(--button-border-width, 0) solid var(--button-border-color, transparent);
    box-shadow: var(--button-shadow);
    box-sizing: border-box;
    color: var(--button-color-text);
    cursor: pointer;
    display: inline-block;
    font: var(--button-font);
    height: var(--button-height);
    line-height: calc(var(--button-height) - (2 * var(--button-border-width, 0px)));
    overflow: hidden;
    padding: 0 calc(var(--button-padding) - var(--button-border-width, 0px));
    text-align: center;
    text-decoration: none;
    text-overflow: ellipsis;
    white-space: nowrap;
    --button-border-color: var(--button-border-color-default);
    --button-border-width: var(--button-border-width-default);
    --button-color-background: var(--button-color-background-default);
    --button-color-text: var(--button-color-text-default);
    /* This is :active, AKA Pressed */
    /* This is Selected */
  }
.\!button {
    background: var(--button-color-background) !important;
    border-radius: 999px !important;
    border: none !important;
    border: var(--button-border-width, 0) solid var(--button-border-color, transparent) !important;
    box-shadow: var(--button-shadow) !important;
    box-sizing: border-box !important;
    color: var(--button-color-text) !important;
    cursor: pointer !important;
    display: inline-block !important;
    font: var(--button-font) !important;
    height: var(--button-height) !important;
    line-height: calc(var(--button-height) - (2 * var(--button-border-width, 0px))) !important;
    overflow: hidden !important;
    padding: 0 calc(var(--button-padding) - var(--button-border-width, 0px)) !important;
    text-align: center !important;
    text-decoration: none !important;
    text-overflow: ellipsis !important;
    white-space: nowrap !important;
    --button-border-color: var(--button-border-color-default) !important;
    --button-border-width: var(--button-border-width-default) !important;
    --button-color-background: var(--button-color-background-default) !important;
    --button-color-text: var(--button-color-text-default) !important;
    /* This is :active, AKA Pressed */
    /* This is Selected */
  }
.button .button-icon {
    margin-right: var(--spacer-xs);
  }
.\!button .button-icon {
    margin-right: var(--spacer-xs) !important;
  }
.button .dropdown-icon {
    transform: rotate(0deg);
    transition: transform 0.2s ease-in-out;
  }
.\!button .dropdown-icon {
    transform: rotate(0deg) !important;
    transition: transform 0.2s ease-in-out !important;
  }
.button:focus,
  .button:hover,
  .button.hover {
    --button-color-overlay: var(--color-button-overlay-focus);
  }
.\!button:focus,
  .\!button:hover,
  .\!button.hover {
    --button-color-overlay: var(--color-button-overlay-focus) !important;
  }
.button:hover,
  .button.hover {
    --button-border-color: var(--button-border-color-hover);
    --button-color-background: var(--button-color-background-hover);
  }
.\!button:hover,
  .\!button.hover {
    --button-border-color: var(--button-border-color-hover) !important;
    --button-color-background: var(--button-color-background-hover) !important;
  }
.button:active,
  .button.active {
    --button-color-overlay: var(--color-button-overlay-active);
    --button-color-background: linear-gradient(var(--color-interactive-pressed), var(--color-interactive-pressed)),
      var(--button-color-background-active);
  }
.\!button:active,
  .\!button.active {
    --button-color-overlay: var(--color-button-overlay-active) !important;
    --button-color-background: linear-gradient(var(--color-interactive-pressed), var(--color-interactive-pressed)),
      var(--button-color-background-active) !important;
  }
.button:active,
  .button.\!active {
    --button-color-overlay: var(--color-button-overlay-active) !important;
    --button-color-background: linear-gradient(var(--color-interactive-pressed), var(--color-interactive-pressed)),
      var(--button-color-background-active) !important;
  }
.button:disabled {
    --button-color-background: var(--button-color-background-disabled);
    --button-color-text: var(--button-color-text-disabled);
    cursor: not-allowed;
  }
.\!button:disabled {
    --button-color-background: var(--button-color-background-disabled) !important;
    --button-color-text: var(--button-color-text-disabled) !important;
    cursor: not-allowed !important;
  }
.button.button-activated {
    --button-border-width: 0;
    --button-border-color: var(--button-border-color-activated);
    --button-color-background: var(--button-color-background-activated);
    --button-color-text: var(--button-color-text-activated);
  }
.\!button.button-activated {
    --button-border-width: 0 !important;
    --button-border-color: var(--button-border-color-activated) !important;
    --button-color-background: var(--button-color-background-activated) !important;
    --button-color-text: var(--button-color-text-activated) !important;
  }
.button-shell {
    background: var(--button-color-background);
    border-radius: 999px;
    border: none;
    border: var(--button-border-width, 0) solid var(--button-border-color, transparent);
    box-shadow: var(--button-shadow);
    box-sizing: border-box;
    color: var(--button-color-text);
    cursor: pointer;
    display: inline-block;
    font: var(--button-font);
    height: var(--button-height);
    line-height: calc(var(--button-height) - (2 * var(--button-border-width, 0px)));
    overflow: hidden;
    padding: 0 calc(var(--button-padding) - var(--button-border-width, 0px));
    text-align: center;
    text-decoration: none;
    text-overflow: ellipsis;
    white-space: nowrap;
    --button-border-color: var(--button-border-color-default);
    --button-border-width: var(--button-border-width-default);
    --button-color-background: var(--button-color-background-default);
    --button-color-text: var(--button-color-text-default);
  }
.button-large {
    --button-height: var(--size-button-lg-h);
    --button-padding: var(--spacer-xs);
    --button-font: var(--font-button-lg);
    --button-border-width-default: var(--line-button-lg-border);
  }
.button-large.icon {
    padding: calc(var(--rem12) + var(--rem1));
  }
.button-large.\!icon {
    padding: calc(var(--rem12) + var(--rem1)) !important;
  }
.button-medium {
    --button-height: var(--size-button-md-h);
    --button-padding: var(--spacer-xs);
    --button-font: var(--font-button-md);
    --button-border-width-default: var(--line-button-md-border);
  }
.button-medium.icon {
    padding: calc(var(--rem8) + var(--rem1));
  }
.button-medium.\!icon {
    padding: calc(var(--rem8) + var(--rem1)) !important;
  }
.button-small {
    --button-height: var(--size-button-sm-h);
    --button-padding: var(--spacer-2xs);
    --button-font: var(--font-button-sm);
    --button-border-width-default: var(--line-button-sm-border);
  }
.button-small.icon {
    padding: calc(var(--rem6) + var(--rem1));
  }
.button-small.\!icon {
    padding: calc(var(--rem6) + var(--rem1)) !important;
  }
.button-x-small {
    --button-height: var(--size-button-xs-h);
    --button-padding: var(--spacer-sm);
    --button-font: var(--font-button-xs);
    --button-border-width-default: var(--line-button-xs-border);
  }
.button-icon {
    --button-padding: 0;
    width: var(--button-height);
  }
.button-primary {
    --button-color-background-default: var(--color-primary-background);
    --button-color-background-focus: var(--color-primary-background);
    --button-color-background-hover: var(--color-button-primary-background-hover);
    --button-color-background-active: linear-gradient(var(--color-button-primary-background-hover), var(--color-button-primary-background-hover));
    --button-color-background-disabled: var(--color-button-primary-background-disabled);
    --button-color-background-activated: var(--color-button-primary-background-activated);
    --button-color-text-default: var(--color-global-white);
    --button-color-text-disabled: var(--color-button-primary-text-disabled);
    --button-color-text-activated: var(--color-button-primary-text-activated);
    --button-border-color-default: transparent;
  }
.button-secondary {
    --button-color-background-default: var(--color-button-secondary-background);
    --button-color-background-focus: var(--color-button-secondary-background-focus);
    --button-color-background-hover: var(--color-button-secondary-background-hover);
    --button-color-background-active: linear-gradient(var(--color-button-secondary-background-hover), var(--color-button-secondary-background-hover));
    --button-color-background-disabled: var(--color-button-secondary-background-disabled);
    --button-color-background-activated: var(--color-button-secondary-background-activated);
    --button-color-text-default: var(--color-button-secondary-text);
    --button-color-text-disabled: var(--color-button-secondary-text-disabled);
    --button-color-text-activated: var(--color-button-secondary-text-activated);
    --button-border-color-default: var(--color-button-secondary-border);
  }
.button-tertiary {
    --button-color-background-default: var(--color-button-tertiary-background);
    --button-color-background-focus: var(--color-button-tertiary-background-focus);
    --button-color-background-hover: var(--color-button-tertiary-background-hover);
    --button-color-background-disabled: var(--color-button-tertiary-background-disabled);
    --button-color-background-activated: var(--color-button-tertiary-background-activated);
    --button-color-text-default: var(--color-button-tertiary-text);
    --button-color-text-disabled: var(--color-button-tertiary-text-disabled);
    --button-color-text-activated: var(--color-button-tertiary-text-activated);
    --button-border-color-default: transparent;
  }
.button-plain {
    --button-color-background-default: transparent;
    --button-color-background-focus: transparent;
    --button-color-background-hover: var(--color-button-plain-background-hover);
    --button-color-background-disabled: var(--color-button-plain-background-disabled);
    --button-color-background-activated: var(--color-button-plain-background-activated);
    --button-color-background-active: linear-gradient(var(--color-button-secondary-background-hover), var(--color-button-secondary-background-hover));
    --button-color-text-default: var(--color-button-plain-text);
    --button-color-text-disabled: var(--color-button-plain-text-disabled);
    --button-color-text-activated: var(--color-button-plain-text-activated);
    --button-border-color-default: transparent;
  }
.button-bordered {
    --button-color-background-default: transparent;
    --button-color-background-focus: transparent;
    --button-color-background-hover: transparent;
    --button-color-background-active: linear-gradient(transparent, transparent);
    --button-color-background-disabled: transparent;
    --button-color-background-activated: var(--color-button-secondary-background-activated);
    --button-color-text-default: var(--color-neutral-content);
    --button-color-text-disabled: var(--color-neutral-content-disabled);
    --button-color-text-activated: var(--color-neutral-content-strong);
    --button-border-color-default: var(--color-neutral-border-medium);
    --button-border-color-hover: var(--color-neutral-border-strong);
    --button-border-color-active: var(--color-neutral-border-strong);
    --button-border-color-activated: var(--color-neutral-border-strong);
    --button-border-color-disabled: var(--color-neutral-content-disabled);
    --button-border-width-default: var(--line-sm);
    --button-border-width-activated: var(--line-sm);
  }
.button-destructive {
    --button-color-background-default: var(--color-danger-background);
    --button-color-background-focus: var(--color-danger-background-hover);
    --button-color-background-hover: var(--color-danger-background-hover);
    --button-color-background-active: linear-gradient(var(--color-danger-background-hover), var(--color-danger-background-hover));
    --button-color-background-disabled: var(--color-button-secondary-background-disabled);
    --button-color-text-default: var(--color-danger-content-default);
    --button-color-text-disabled: var(--color-button-secondary-text-disabled);
    --button-border-color-default: transparent;
    --button-border-color-hover: transparent;
    --button-border-color-active: transparent;
  }
.button-media {
    --button-color-background-default: var(--color-media-background);
    --button-color-background-focus: var(--color-media-background-hover);
    --button-color-background-hover: var(--color-media-background-hover);
    --button-color-background-active: linear-gradient(var(--color-media-background-hover), var(--color-media-background-hover));
    --button-border-color-activated: var(--color-neutral-content-strong);
    --button-color-text-default: white;
    --button-color-text-disabled: var(--color-media-onbackground-disabled);
    --button-color-background-disabled: var(--color-media-background);
  }
.button-brand {
    --button-color-background-default: var(--color-brand-background);
    --button-color-background-hover: var(--color-brand-background-hover);
    --button-color-background-active: linear-gradient(var(--color-brand-background-hover), var(--color-brand-background-hover));
    --button-color-background-disabled: var(--color-interactive-background-disabled);
    --button-color-text-default: var(--color-danger-content-default);
    --button-color-text-disabled: var(--color-neutral-content-disabled);
    --button-border-color-default: transparent;
  }
.button-success {
    --button-color-background-default: var(--color-success-background);
    --button-color-background-focus: var(--color-success-background-hover);
    --button-color-background-hover: var(--color-success-background-hover);
    --button-color-background-active: linear-gradient(var(--color-success-background-hover), var(--color-success-background-hover));
    --button-color-background-disabled: var(--color-button-primary-background-disabled);
    --button-color-text-default: var(--color-success-onBackground);
    --button-color-text-disabled: var(--color-button-primary-text-disabled);
    --button-border-color-default: transparent;
  }
.button-plain-inverted {
    --button-color-background-default: transparent;
    --button-color-background-focus: var(--color-neutral-content);
    --button-color-background-hover: var(--color-neutral-content);
    --button-color-background-active: var(--color-interactive-pressed);
    --button-color-background-disabled: transparent;
    --button-color-text-default: var(--color-neutral-background-weak);
    --button-color-text-disabled: var(--color-neutral-content);
    --button-border-color-default: transparent;
    --button-color-background-activated: var(--color-button-plain-inverted-background-activated);
    --button-color-text-activated: var(--color-button-plain-inverted-text-activated);
  }
/* Featured avatar */
.full-snoo-xs {
    --full-snoo-xs-size: var(--rem48);
    height: var(--full-snoo-xs-size);
    width: var(--full-snoo-xs-size);
    margin-top: 0.125rem;
  }
.full-snoo-xs > img {
    width: var(--rem36);
    bottom: calc(-1 * 0.1875rem);
  }
.full-snoo-sm {
    --full-snoo-sm-size: var(--rem64);
    height: var(--full-snoo-sm-size);
    width: var(--full-snoo-sm-size);
    margin-top: 0.125rem;
  }
.full-snoo-sm > img {
    width: var(--rem48);
    bottom: calc(-1 * var(--rem4));
  }
.full-snoo-md {
    --full-snoo-md-size: var(--rem88);
    height: var(--full-snoo-md-size);
    width: var(--full-snoo-md-size);
    margin-top: var(--spacer-2xs);
  }
.full-snoo-md > img {
    width: var(--rem64);
    bottom: calc(-1 * var(--rem6));
  }
.full-snoo-lg {
    --full-snoo-lg-size: var(--rem144);
    height: var(--full-snoo-lg-size);
    width: var(--full-snoo-lg-size);
    margin-top: 0.375rem;
  }
.full-snoo-lg > img {
    width: 6.625rem;
    bottom: calc(-1 * var(--rem10));
  }
.full-snoo-xl {
    --full-snoo-xl-size: var(--rem192);
    height: var(--full-snoo-xl-size);
    width: var(--full-snoo-xl-size);
    margin-top: var(--spacer-xs);
  }
.full-snoo-xl > img {
    width: 8.8125rem;
    bottom: calc(-1 * var(--rem14));
  }
.full-snoo-2xl {
    --full-snoo-2xl-size: var(--rem320);
    height: var(--full-snoo-2xl-size);
    width: var(--full-snoo-2xl-size);
    margin-top: var(--spacer-sm);
  }
.full-snoo-2xl > img {
    width: 14.75rem;
    bottom: calc(-1 * var(--rem22));
  }
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
.pointer-events-none {
  pointer-events: none;
}
.pointer-events-auto {
  pointer-events: auto;
}
.visible {
  visibility: visible;
}
.\!visible {
  visibility: visible !important;
}
.invisible {
  visibility: hidden;
}
.static {
  position: static;
}
.fixed {
  position: fixed;
}
.absolute {
  position: absolute;
}
.relative {
  position: relative;
}
.sticky {
  position: sticky;
}
.\!sticky {
  position: sticky !important;
}
.inset-0 {
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
}
.top-0 {
  top: 0px;
}
.left-0 {
  left: 0px;
}
.right-0 {
  right: 0px;
}
.top-\[128px\] {
  top: 128px;
}
.top-\[30px\] {
  top: 30px;
}
.bottom-0 {
  bottom: 0px;
}
.top-1\/2 {
  top: 50%;
}
.bottom-2xl {
  bottom: 3rem;
}
.left-1\/2 {
  left: 50%;
}
.left-xs {
  left: 0.5rem;
}
.top-2xs {
  top: 0.25rem;
}
.right-2xs {
  right: 0.25rem;
}
.right-xs {
  right: 0.5rem;
}
.right-sm {
  right: 0.75rem;
}
.top-sm {
  top: 0.75rem;
}
.left-md {
  left: 1rem;
}
.top-md {
  top: 1rem;
}
.top-100 {
  top: 100%;
}
.left-lg {
  left: 1.5rem;
}
.top-3xl {
  top: 4rem;
}
.-right-\[0\.0625rem\] {
  right: -0.0625rem;
}
.-right-\[0\.0825rem\] {
  right: -0.0825rem;
}
.-right-\[0\.125rem\] {
  right: -0.125rem;
}
.-right-\[\.65rem\] {
  right: -.65rem;
}
.-right-\[\.75rem\] {
  right: -.75rem;
}
.isolate {
  isolation: isolate;
}
.z-\[80\] {
  z-index: 80;
}
.z-10 {
  z-index: 10;
}
.z-0 {
  z-index: 0;
}
.z-20 {
  z-index: 20;
}
.z-50 {
  z-index: 50;
}
.z-\[1\] {
  z-index: 1;
}
.z-\[2\] {
  z-index: 2;
}
.z-\[3\] {
  z-index: 3;
}
.col-span-full {
  grid-column: 1 / -1;
}
.col-span-6 {
  grid-column: span 6 / span 6;
}
.col-span-1 {
  grid-column: span 1 / span 1;
}
.col-span-4 {
  grid-column: span 4 / span 4;
}
.col-span-2 {
  grid-column: span 2 / span 2;
}
.col-start-1 {
  grid-column-start: 1;
}
.col-start-2 {
  grid-column-start: 2;
}
.col-start-3 {
  grid-column-start: 3;
}
.col-end-1 {
  grid-column-end: 1;
}
.col-end-4 {
  grid-column-end: 4;
}
.col-end-2 {
  grid-column-end: 2;
}
.row-start-1 {
  grid-row-start: 1;
}
.row-end-auto {
  grid-row-end: auto;
}
.float-right {
  float: right;
}
.m-0 {
  margin: 0px;
}
.m-lg {
  margin: 1.5rem;
}
.m-auto {
  margin: auto;
}
.m-xs {
  margin: 0.5rem;
}
.m-sm {
  margin: 0.75rem;
}
.m-md {
  margin: 1rem;
}
.my-0 {
  margin-top: 0px;
  margin-bottom: 0px;
}
.mx-auto {
  margin-left: auto;
  margin-right: auto;
}
.mx-md {
  margin-left: 1rem;
  margin-right: 1rem;
}
.mx-0 {
  margin-left: 0px;
  margin-right: 0px;
}
.mx-sm {
  margin-left: 0.75rem;
  margin-right: 0.75rem;
}
.mx-xs {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
}
.my-sm {
  margin-top: 0.75rem;
  margin-bottom: 0.75rem;
}
.mx-2xs {
  margin-left: 0.25rem;
  margin-right: 0.25rem;
}
.-mx-md {
  margin-left: -1rem;
  margin-right: -1rem;
}
.my-md {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.my-xs {
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}
.mb-xs {
  margin-bottom: 0.5rem;
}
.mb-lg {
  margin-bottom: 1.5rem;
}
.mr-md {
  margin-right: 1rem;
}
.mb-0 {
  margin-bottom: 0px;
}
.mt-\[2px\] {
  margin-top: 2px;
}
.ml-\[-4px\] {
  margin-left: -4px;
}
.ml-\[8px\] {
  margin-left: 8px;
}
.mt-\[4px\] {
  margin-top: 4px;
}
.ml-auto {
  margin-left: auto;
}
.mb-\[10px\] {
  margin-bottom: 10px;
}
.mt-2xs {
  margin-top: 0.25rem;
}
.mt-sm {
  margin-top: 0.75rem;
}
.mr-sm {
  margin-right: 0.75rem;
}
.mr-2xs {
  margin-right: 0.25rem;
}
.ml-md {
  margin-left: 1rem;
}
.mb-sm {
  margin-bottom: 0.75rem;
}
.ml-xs {
  margin-left: 0.5rem;
}
.ml-2xs {
  margin-left: 0.25rem;
}
.ml-sm {
  margin-left: 0.75rem;
}
.mt-md {
  margin-top: 1rem;
}
.mb-md {
  margin-bottom: 1rem;
}
.mt-lg {
  margin-top: 1.5rem;
}
.mt-0 {
  margin-top: 0px;
}
.mt-xs {
  margin-top: 0.5rem;
}
.mr-xs {
  margin-right: 0.5rem;
}
.mt-xl {
  margin-top: 2rem;
}
.-mt-xl {
  margin-top: -2rem;
}
.mr-0 {
  margin-right: 0px;
}
.mb-2xs {
  margin-bottom: 0.25rem;
}
.-ml-sm {
  margin-left: -0.75rem;
}
.mr-auto {
  margin-right: auto;
}
.ml-0 {
  margin-left: 0px;
}
.-ml-md {
  margin-left: -1rem;
}
.-mt-sm {
  margin-top: -0.75rem;
}
.mb-2xl {
  margin-bottom: 3rem;
}
.ml-px {
  margin-left: 1px;
}
.ml-xl {
  margin-left: 2rem;
}
.-ml-\[var\(--rem4\)\] {
  margin-left: calc(var(--rem4) * -1);
}
.-ml-\[var\(--rem6\)\] {
  margin-left: calc(var(--rem6) * -1);
}
.-ml-\[var\(--rem8\)\] {
  margin-left: calc(var(--rem8) * -1);
}
.-ml-\[var\(--rem10\)\] {
  margin-left: calc(var(--rem10) * -1);
}
.-ml-\[var\(--rem12\)\] {
  margin-left: calc(var(--rem12) * -1);
}
.-ml-\[var\(--rem14\)\] {
  margin-left: calc(var(--rem14) * -1);
}
.-ml-\[var\(--rem16\)\] {
  margin-left: calc(var(--rem16) * -1);
}
.-ml-\[var\(--rem18\)\] {
  margin-left: calc(var(--rem18) * -1);
}
.-ml-\[var\(--rem20\)\] {
  margin-left: calc(var(--rem20) * -1);
}
.mr-\[calc\(var\(--size-button-sm-h\)-var\(--rem10\)-var\(--button-border-width-default\)\)\] {
  margin-right: calc(var(--size-button-sm-h) - var(--rem10) - var(--button-border-width-default));
}
.mr-\[length\:var\(--rem6\)\] {
  margin-right: var(--rem6);
}
.mt-\[-0\.125rem\] {
  margin-top: -0.125rem;
}
.ml-\[-\.25rem\] {
  margin-left: -.25rem;
}
.mt-\[-0\.25rem\] {
  margin-top: -0.25rem;
}
.box-border {
  box-sizing: border-box;
}
.block {
  display: block;
}
.\!block {
  display: block !important;
}
.inline-block {
  display: inline-block;
}
.inline {
  display: inline;
}
.flex {
  display: flex;
}
.inline-flex {
  display: inline-flex;
}
.table {
  display: table;
}
.\!table {
  display: table !important;
}
.table-cell {
  display: table-cell;
}
.grid {
  display: grid;
}
.contents {
  display: contents;
}
.list-item {
  display: list-item;
}
.hidden {
  display: none;
}
.\!hidden {
  display: none !important;
}
.aspect-square {
  aspect-ratio: 1 / 1;
}
.h-\[10px\] {
  height: 10px;
}
.h-\[20px\] {
  height: 20px;
}
.\!h-\[32px\] {
  height: 32px !important;
}
.h-\[16px\] {
  height: 16px;
}
.h-full {
  height: 100%;
}
.h-3xl {
  height: 4rem;
}
.h-xs {
  height: 0.5rem;
}
.h-2xl {
  height: 3rem;
}
.h-100 {
  height: 100%;
}
.h-2xs {
  height: 0.25rem;
}
.h-lg {
  height: 1.5rem;
}
.h-md {
  height: 1rem;
}
.h-\[28px\] {
  height: 28px;
}
.h-sm {
  height: 0.75rem;
}
.h-px {
  height: 1px;
}
.h-auto {
  height: auto;
}
.h-xl {
  height: 2rem;
}
.h-4xl {
  height: 6rem;
}
.h-screen {
  height: 100vh;
}
.h-0 {
  height: 0px;
}
.h-\[60px\] {
  height: 60px;
}
.h-\[316px\] {
  height: 316px;
}
.h-\[240px\] {
  height: 240px;
}
.h-\[500px\] {
  height: 500px;
}
.h-\[1rem\] {
  height: 1rem;
}
.h-\[1\.25rem\] {
  height: 1.25rem;
}
.h-\[1\.5rem\] {
  height: 1.5rem;
}
.h-\[2rem\] {
  height: 2rem;
}
.h-\[2\.5rem\] {
  height: 2.5rem;
}
.h-\[3rem\] {
  height: 3rem;
}
.h-\[2\.87rem\] {
  height: 2.87rem;
}
.h-\[3\.25rem\] {
  height: 3.25rem;
}
.h-\[4\.5rem\] {
  height: 4.5rem;
}
.h-\[3\.5rem\] {
  height: 3.5rem;
}
.h-\[4rem\] {
  height: 4rem;
}
.h-\[5\.5rem\] {
  height: 5.5rem;
}
.h-\[\.25rem\] {
  height: .25rem;
}
.h-\[\.375rem\] {
  height: .375rem;
}
.h-\[\.625rem\] {
  height: .625rem;
}
.h-\[\.75rem\] {
  height: .75rem;
}
.max-h-\[4\.143em\] {
  max-height: 4.143em;
}
.max-h-full {
  max-height: 100%;
}
.max-h-\[240px\] {
  max-height: 240px;
}
.max-h-\[253px\] {
  max-height: 253px;
}
.min-h-\[20px\] {
  min-height: 20px;
}
.min-h-screen {
  min-height: 100vh;
}
.min-h-full {
  min-height: 100%;
}
.min-h-\[1rem\] {
  min-height: 1rem;
}
.w-100 {
  width: 100%;
}
.w-\[539px\] {
  width: 539px;
}
.w-\[16px\] {
  width: 16px;
}
.\!w-\[32px\] {
  width: 32px !important;
}
.w-full {
  width: 100%;
}
.w-3xl {
  width: 4rem;
}
.w-fit {
  width: fit-content;
}
.w-\[280px\] {
  width: 280px;
}
.w-\[268px\] {
  width: 268px;
}
.w-xs {
  width: 0.5rem;
}
.w-\[64px\] {
  width: 64px;
}
.w-lg {
  width: 1.5rem;
}
.w-md {
  width: 1rem;
}
.w-5xl {
  width: 8rem;
}
.w-xl {
  width: 2rem;
}
.w-auto {
  width: auto;
}
.w-screen {
  width: 100vw;
}
.w-2xl {
  width: 3rem;
}
.w-px {
  width: 1px;
}
.w-\[1rem\] {
  width: 1rem;
}
.w-\[1\.25rem\] {
  width: 1.25rem;
}
.w-\[1\.5rem\] {
  width: 1.5rem;
}
.w-\[2rem\] {
  width: 2rem;
}
.w-\[2\.5rem\] {
  width: 2.5rem;
}
.w-\[3rem\] {
  width: 3rem;
}
.w-\[2\.87rem\] {
  width: 2.87rem;
}
.w-\[3\.25rem\] {
  width: 3.25rem;
}
.w-\[4\.5rem\] {
  width: 4.5rem;
}
.w-\[3\.5rem\] {
  width: 3.5rem;
}
.w-\[4rem\] {
  width: 4rem;
}
.w-\[5\.5rem\] {
  width: 5.5rem;
}
.w-\[\.25rem\] {
  width: .25rem;
}
.w-\[\.375rem\] {
  width: .375rem;
}
.w-\[\.625rem\] {
  width: .625rem;
}
.w-\[\.75rem\] {
  width: .75rem;
}
.min-w-\[500px\] {
  min-width: 500px;
}
.min-w-0 {
  min-width: 0px;
}
.min-w-\[20px\] {
  min-width: 20px;
}
.min-w-full {
  min-width: 100%;
}
.min-w-\[0\.5rem\] {
  min-width: 0.5rem;
}
.max-w-\[12rem\] {
  max-width: 12rem;
}
.max-w-\[230px\] {
  max-width: 230px;
}
.max-w-full {
  max-width: 100%;
}
.max-w-\[240px\] {
  max-width: 240px;
}
.max-w-none {
  max-width: none;
}
.max-w-\[480px\] {
  max-width: 480px;
}
.flex-auto {
  flex: 1 1 auto;
}
.flex-1 {
  flex: 1 1 0%;
}
.flex-none {
  flex: none;
}
.flex-shrink-0 {
  flex-shrink: 0;
}
.flex-shrink {
  flex-shrink: 1;
}
.shrink {
  flex-shrink: 1;
}
.shrink-0 {
  flex-shrink: 0;
}
.flex-grow-0 {
  flex-grow: 0;
}
.flex-grow {
  flex-grow: 1;
}
.grow {
  flex-grow: 1;
}
.grow-0 {
  flex-grow: 0;
}
.basis-0 {
  flex-basis: 0px;
}
.basis-2xl {
  flex-basis: 3rem;
}
.basis-full {
  flex-basis: 100%;
}
.border-separate {
  border-collapse: separate;
}
.-translate-y-1\/2 {
  --tw-translate-y: -50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.-translate-x-1\/2 {
  --tw-translate-x: -50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.translate-x-0 {
  --tw-translate-x: 0px;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.translate-y-md {
  --tw-translate-y: 1rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.rotate-90 {
  --tw-rotate: 90deg;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.scale-75 {
  --tw-scale-x: .75;
  --tw-scale-y: .75;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.scale-150 {
  --tw-scale-x: 1.5;
  --tw-scale-y: 1.5;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.scale-100 {
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.-scale-x-100 {
  --tw-scale-x: -1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.transform {
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
.transform-gpu {
  transform: translate3d(var(--tw-translate-x), var(--tw-translate-y), 0) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
.animate-spin {
  animation: spin 1s linear infinite;
}
.cursor-pointer {
  cursor: pointer;
}
.cursor-default {
  cursor: default;
}
.cursor-none {
  cursor: none;
}
.select-none {
  user-select: none;
}
.resize-y {
  resize: vertical;
}
.resize {
  resize: both;
}
.list-none {
  list-style-type: none;
}
.columns-1 {
  columns: 1;
}
.grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
.grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr));
}
.grid-cols-8 {
  grid-template-columns: repeat(8, minmax(0, 1fr));
}
.flex-row {
  flex-direction: row;
}
.flex-col {
  flex-direction: column;
}
.flex-wrap {
  flex-wrap: wrap;
}
.flex-nowrap {
  flex-wrap: nowrap;
}
.items-start {
  align-items: flex-start;
}
.items-end {
  align-items: flex-end;
}
.items-center {
  align-items: center;
}
.items-stretch {
  align-items: stretch;
}
.justify-start {
  justify-content: flex-start;
}
.justify-end {
  justify-content: flex-end;
}
.justify-center {
  justify-content: center;
}
.justify-between {
  justify-content: space-between;
}
.justify-around {
  justify-content: space-around;
}
.justify-items-start {
  justify-items: start;
}
.justify-items-center {
  justify-items: center;
}
.gap-xs {
  gap: 0.5rem;
}
.gap-sm {
  gap: 0.75rem;
}
.gap-md {
  gap: 1rem;
}
.gap-2xs {
  gap: 0.25rem;
}
.gap-\[0\.5rem\] {
  gap: 0.5rem;
}
.gap-x-md {
  column-gap: 1rem;
}
.gap-x-xs {
  column-gap: 0.5rem;
}
.self-start {
  align-self: flex-start;
}
.self-end {
  align-self: flex-end;
}
.self-center {
  align-self: center;
}
.self-baseline {
  align-self: baseline;
}
.overflow-auto {
  overflow: auto;
}
.overflow-hidden {
  overflow: hidden;
}
.overflow-visible {
  overflow: visible;
}
.overflow-scroll {
  overflow: scroll;
}
.overflow-y-auto {
  overflow-y: auto;
}
.overflow-x-hidden {
  overflow-x: hidden;
}
.overflow-x-visible {
  overflow-x: visible;
}
.overflow-x-scroll {
  overflow-x: scroll;
}
.overscroll-none {
  overscroll-behavior: none;
}
.scroll-smooth {
  scroll-behavior: smooth;
}
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.overflow-ellipsis {
  text-overflow: ellipsis;
}
.text-ellipsis {
  text-overflow: ellipsis;
}
.whitespace-normal {
  white-space: normal;
}
.whitespace-nowrap {
  white-space: nowrap;
}
.break-normal {
  overflow-wrap: normal;
  word-break: normal;
}
.rounded-sm {
  border-radius: 0.25rem;
}
.rounded-full {
  border-radius: 624.9375rem;
}
.rounded-\[4px\] {
  border-radius: 4px;
}
.rounded-\[0\.5rem\] {
  border-radius: 0.5rem;
}
.rounded-lg {
  border-radius: 2rem;
}
.rounded-\[16px\] {
  border-radius: 16px;
}
.rounded-none {
  border-radius: 0rem;
}
.rounded-\[\.5rem\] {
  border-radius: .5rem;
}
.rounded-l-sm {
  border-top-left-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem;
}
.rounded-t-lg {
  border-top-left-radius: 2rem;
  border-top-right-radius: 2rem;
}
.rounded-r-sm {
  border-top-right-radius: 0.25rem;
  border-bottom-right-radius: 0.25rem;
}
.rounded-r-lg {
  border-top-right-radius: 2rem;
  border-bottom-right-radius: 2rem;
}
.rounded-b-none {
  border-bottom-right-radius: 0rem;
  border-bottom-left-radius: 0rem;
}
.rounded-br-none {
  border-bottom-right-radius: 0rem;
}
.border {
  border-width: 0.0625rem;
}
.border-sm {
  border-width: 0.0625rem;
}
.border-lg {
  border-width: 0.25rem;
}
.border-0 {
  border-width: 0rem;
}
.border-md {
  border-width: 0.125rem;
}
.border-y-sm {
  border-top-width: 0.0625rem;
  border-bottom-width: 0.0625rem;
}
.border-x-0 {
  border-left-width: 0rem;
  border-right-width: 0rem;
}
.border-y-0 {
  border-top-width: 0rem;
  border-bottom-width: 0rem;
}
.border-b {
  border-bottom-width: 0.0625rem;
}
.border-r-sm {
  border-right-width: 0.0625rem;
}
.border-t-sm {
  border-top-width: 0.0625rem;
}
.border-b-0 {
  border-bottom-width: 0rem;
}
.border-r-0 {
  border-right-width: 0rem;
}
.border-l-0 {
  border-left-width: 0rem;
}
.border-b-sm {
  border-bottom-width: 0.0625rem;
}
.border-t-0 {
  border-top-width: 0rem;
}
.border-t {
  border-top-width: 0.0625rem;
}
.border-l-sm {
  border-left-width: 0.0625rem;
}
.border-r-md {
  border-right-width: 0.125rem;
}
.border-r {
  border-right-width: 0.0625rem;
}
.border-l-lg {
  border-left-width: 0.25rem;
}
.border-solid {
  border-style: solid;
}
.border-none {
  border-style: none;
}
.border-neutral-border-weak {
  border-color: var(--color-neutral-border-weak);
}
.border-white {
  --tw-border-opacity: 1;
  border-color: rgb(255 255 255 / var(--tw-border-opacity));
}
.border-\[color\:var\(--newCommunityTheme-postLine\)\] {
  border-color: var(--newCommunityTheme-postLine);
}
.border-neutral-border {
  border-color: var(--color-neutral-border);
}
.border-global-white {
  border-color: var(--color-global-white);
}
.border-tone-2 {
  border-color: var(--color-tone-2);
}
.border-neutral-content {
  border-color: var(--color-neutral-content);
}
.border-tone-4 {
  border-color: var(--color-tone-4);
}
.border-action-secondary {
  border-color: var(--color-action-secondary);
}
.border-tone-7 {
  border-color: var(--color-tone-7);
}
.border-tone-5 {
  border-color: var(--color-tone-5);
}
.border-danger-content {
  border-color: var(--color-danger-content);
}
.border-tone-6 {
  border-color: var(--color-tone-6);
}
.border-tone-3 {
  border-color: var(--color-tone-3);
}
.border-coolgray-350 {
  --tw-border-opacity: 1;
  border-color: rgb(184 197 201 / var(--tw-border-opacity));
}
.border-transparent {
  border-color: transparent;
}
.border-alert-negative {
  border-color: var(--color-alert-negative);
}
.border-global-orangered {
  border-color: var(--color-global-orangered);
}
.border-neutral-border-medium {
  border-color: var(--color-neutral-border-medium);
}
.border-coolgray-100 {
  --tw-border-opacity: 1;
  border-color: rgb(242 244 245 / var(--tw-border-opacity));
}
.border-action-primary {
  border-color: var(--color-action-primary);
}
.border-alert-caution {
  border-color: var(--color-alert-caution);
}
.border-neutral-background {
  border-color: var(--color-neutral-background);
}
.border-secondary-background-selected {
  border-color: var(--color-secondary-background-selected);
}
.border-action-upvote {
  border-color: var(--color-action-upvote);
}
.border-action-downvote {
  border-color: var(--color-action-downvote);
}
.border-r-neutral-border-weak {
  border-right-color: var(--color-neutral-border-weak);
}
.bg-neutral-background {
  background-color: var(--color-neutral-background);
}
.bg-neutral-background-weak {
  background-color: var(--color-neutral-background-weak);
}
.bg-global-orangered {
  background-color: var(--color-global-orangered);
}
.bg-coolgray-350 {
  --tw-bg-opacity: 1;
  background-color: rgb(184 197 201 / var(--tw-bg-opacity));
}
.bg-\[color\:var\(--newCommunityTheme-body\)\] {
  background-color: var(--newCommunityTheme-body);
}
.bg-neutral-background-strong {
  background-color: var(--color-neutral-background-strong);
}
.bg-secondary-background-selected {
  background-color: var(--color-secondary-background-selected);
}
.bg-alert-caution {
  background-color: var(--color-alert-caution);
}
.bg-success-background {
  background-color: var(--color-success-background);
}
.bg-black {
  --tw-bg-opacity: 1;
  background-color: rgb(0 0 0 / var(--tw-bg-opacity));
}
.bg-white {
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}
.bg-opacity-50 {
  background-color: var(--color-opacity-50);
}
.bg-transparent {
  background-color: transparent;
}
.bg-scrim {
  background-color: var(--color-scrim);
}
.bg-tone-7 {
  background-color: var(--color-tone-7);
}
.bg-tone-6 {
  background-color: var(--color-tone-6);
}
.bg-tone-4 {
  background-color: var(--color-tone-4);
}
.bg-ui-modalbackground {
  background-color: var(--color-ui-modalbackground);
}
.bg-tone-5 {
  background-color: var(--color-tone-5);
}
.bg-tone-1 {
  background-color: var(--color-tone-1);
}
.bg-secondary-background {
  background-color: var(--color-secondary-background);
}
.bg-neutral-background-hover {
  background-color: var(--color-neutral-background-hover);
}
.bg-primary-background {
  background-color: var(--color-primary-background);
}
.bg-global-white {
  background-color: var(--color-global-white);
}
.bg-brand-background {
  background-color: var(--color-brand-background);
}
.bg-global-alienblue {
  background-color: var(--color-global-alienblue);
}
.bg-secondary-weak {
  background-color: var(--color-secondary-weak);
}
.bg-kiwigreen-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(85 189 70 / var(--tw-bg-opacity));
}
.bg-kiwigreen-600 {
  --tw-bg-opacity: 1;
  background-color: rgb(10 96 0 / var(--tw-bg-opacity));
}
.bg-yelloworange-400 {
  --tw-bg-opacity: 1;
  background-color: rgb(255 156 26 / var(--tw-bg-opacity));
}
.bg-action-primary {
  background-color: var(--color-action-primary);
}
.bg-orangered-300 {
  --tw-bg-opacity: 1;
  background-color: rgb(255 190 166 / var(--tw-bg-opacity));
}
.bg-coolgray-200 {
  --tw-bg-opacity: 1;
  background-color: rgb(226 231 233 / var(--tw-bg-opacity));
}
.bg-online {
  background-color: var(--color-online);
}
.bg-warning-content {
  background-color: var(--color-warning-content);
}
.bg-success-content {
  background-color: var(--color-success-content);
}
.bg-neutral-content {
  background-color: var(--color-neutral-content);
}
.bg-danger-content {
  background-color: var(--color-danger-content);
}
.bg-neutral-content-disabled {
  background-color: var(--color-neutral-content-disabled);
}
.bg-brand-onBackground {
  background-color: var(--color-brand-onBackground);
}
.bg-action-upvote {
  background-color: var(--color-action-upvote);
}
.bg-action-downvote {
  background-color: var(--color-action-downvote);
}
.bg-interactive-background-disabled {
  background-color: var(--color-interactive-background-disabled);
}
.bg-\[color\:var\(--button-color-background-default\)\] {
  background-color: var(--button-color-background-default);
}
.bg-neutral-background-selected {
  background-color: var(--color-neutral-background-selected);
}
.bg-\[color\:var\(--color-button-plain-background-disabled\)\] {
  background-color: var(--color-button-plain-background-disabled);
}
.bg-opacity-25 {
  --tw-bg-opacity: 0.25;
}
.bg-opacity-50 {
  --tw-bg-opacity: 0.5;
}
.bg-gradient-to-r {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
.bg-gradient-to-l {
  background-image: linear-gradient(to left, var(--tw-gradient-stops));
}
.bg-gradient-to-t {
  background-image: linear-gradient(to top, var(--tw-gradient-stops));
}
.from-white {
  --tw-gradient-from: #ffffff;
  --tw-gradient-to: rgb(255 255 255 / 0);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
.from-transparent {
  --tw-gradient-from: transparent;
  --tw-gradient-to: rgb(0 0 0 / 0);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
}
.via-white {
  --tw-gradient-to: rgb(255 255 255 / 0);
  --tw-gradient-stops: var(--tw-gradient-from), #ffffff, var(--tw-gradient-to);
}
.fill-brand-background {
  fill: var(--color-brand-background);
}
.fill-current {
  fill: currentColor;
}
.stroke-tone-2 {
  stroke: var(--color-tone-2);
}
.object-contain {
  object-fit: contain;
}
.p-md {
  padding: 1rem;
}
.p-sm {
  padding: 0.75rem;
}
.p-xs {
  padding: 0.5rem;
}
.p-\[32px\] {
  padding: 32px;
}
.p-px {
  padding: 1px;
}
.p-0 {
  padding: 0px;
}
.p-2xs {
  padding: 0.25rem;
}
.p-lg {
  padding: 1.5rem;
}
.px-lg {
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}
.px-\[8px\] {
  padding-left: 8px;
  padding-right: 8px;
}
.py-\[6px\] {
  padding-top: 6px;
  padding-bottom: 6px;
}
.px-\[length\:var\(--rem8\)\] {
  padding-left: var(--rem8);
  padding-right: var(--rem8);
}
.py-\[32px\] {
  padding-top: 32px;
  padding-bottom: 32px;
}
.px-\[16px\] {
  padding-left: 16px;
  padding-right: 16px;
}
.py-\[8px\] {
  padding-top: 8px;
  padding-bottom: 8px;
}
.py-sm {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}
.px-md {
  padding-left: 1rem;
  padding-right: 1rem;
}
.py-xs {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}
.px-2xs {
  padding-left: 0.25rem;
  padding-right: 0.25rem;
}
.py-lg {
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
}
.py-0 {
  padding-top: 0px;
  padding-bottom: 0px;
}
.px-sm {
  padding-left: 0.75rem;
  padding-right: 0.75rem;
}
.py-2xs {
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
}
.px-2xl {
  padding-left: 3rem;
  padding-right: 3rem;
}
.px-xs {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}
.py-md {
  padding-top: 1rem;
  padding-bottom: 1rem;
}
.px-0 {
  padding-left: 0px;
  padding-right: 0px;
}
.px-\[length\:var\(--rem10\)\] {
  padding-left: var(--rem10);
  padding-right: var(--rem10);
}
.px-\[length\:var\(--rem6\)\] {
  padding-left: var(--rem6);
  padding-right: var(--rem6);
}
.px-\[length\:var\(--rem14\)\] {
  padding-left: var(--rem14);
  padding-right: var(--rem14);
}
.px-\[length\:var\(--rem12\)\] {
  padding-left: var(--rem12);
  padding-right: var(--rem12);
}
.px-\[0\.375rem\] {
  padding-left: 0.375rem;
  padding-right: 0.375rem;
}
.py-\[0\.125rem\] {
  padding-top: 0.125rem;
  padding-bottom: 0.125rem;
}
.py-\[length\:var\(--rem6\)\] {
  padding-top: var(--rem6);
  padding-bottom: var(--rem6);
}
.py-\[length\:var\(--rem8\)\] {
  padding-top: var(--rem8);
  padding-bottom: var(--rem8);
}
.py-\[length\:var\(--rem10\)\] {
  padding-top: var(--rem10);
  padding-bottom: var(--rem10);
}
.py-\[length\:var\(--rem14\)\] {
  padding-top: var(--rem14);
  padding-bottom: var(--rem14);
}
.pr-0 {
  padding-right: 0px;
}
.pt-md {
  padding-top: 1rem;
}
.pt-sm {
  padding-top: 0.75rem;
}
.pb-xs {
  padding-bottom: 0.5rem;
}
.pl-sm {
  padding-left: 0.75rem;
}
.pb-2xs {
  padding-bottom: 0.25rem;
}
.pt-lg {
  padding-top: 1.5rem;
}
.pt-2xs {
  padding-top: 0.25rem;
}
.\!pt-2xs {
  padding-top: 0.25rem !important;
}
.pb-\[8px\] {
  padding-bottom: 8px;
}
.pt-\[4px\] {
  padding-top: 4px;
}
.pr-sm {
  padding-right: 0.75rem;
}
.pb-lg {
  padding-bottom: 1.5rem;
}
.pb-md {
  padding-bottom: 1rem;
}
.pr-lg {
  padding-right: 1.5rem;
}
.pl-xs {
  padding-left: 0.5rem;
}
.pl-md {
  padding-left: 1rem;
}
.pt-\[20px\] {
  padding-top: 20px;
}
.pb-\[6px\] {
  padding-bottom: 6px;
}
.pt-0 {
  padding-top: 0px;
}
.pt-px {
  padding-top: 1px;
}
.pt-xs {
  padding-top: 0.5rem;
}
.pr-xs {
  padding-right: 0.5rem;
}
.pb-sm {
  padding-bottom: 0.75rem;
}
.pl-2xs {
  padding-left: 0.25rem;
}
.pl-lg {
  padding-left: 1.5rem;
}
.pr-2xs {
  padding-right: 0.25rem;
}
.pr-md {
  padding-right: 1rem;
}
.pb-0 {
  padding-bottom: 0px;
}
.pb-xl {
  padding-bottom: 2rem;
}
.pt-xl {
  padding-top: 2rem;
}
.pr-xl {
  padding-right: 2rem;
}
.pr-2xl {
  padding-right: 3rem;
}
.pr-3xl {
  padding-right: 4rem;
}
.pl-0 {
  padding-left: 0px;
}
.pl-\[length\:var\(--rem10\)\] {
  padding-left: var(--rem10);
}
.pr-\[length\:var\(--rem14\)\] {
  padding-right: var(--rem14);
}
.pr-\[length\:var\(--rem6\)\] {
  padding-right: var(--rem6);
}
.pl-\[length\:var\(--rem14\)\] {
  padding-left: var(--rem14);
}
.pr-\[length\:var\(--rem10\)\] {
  padding-right: var(--rem10);
}
.pl-\[length\:var\(--rem12\)\] {
  padding-left: var(--rem12);
}
.pr-\[length\:var\(--rem12\)\] {
  padding-right: var(--rem12);
}
.pr-\[length\:var\(--rem16\)\] {
  padding-right: var(--rem16);
}
.pr-\[length\:var\(--rem8\)\] {
  padding-right: var(--rem8);
}
.pl-\[length\:var\(--rem16\)\] {
  padding-left: var(--rem16);
}
.text-left {
  text-align: left;
}
.text-center {
  text-align: center;
}
.text-right {
  text-align: right;
}
.indent-0 {
  text-indent: 0px;
}
.align-top {
  vertical-align: top;
}
.align-middle {
  vertical-align: middle;
}
.align-text-bottom {
  vertical-align: text-bottom;
}
.font-mono {
  font-family: var(--font-mono);
}
.font-sans {
  font-family: var(--font-sans);
}
.text-24 {
  font-size: 1.5rem;
  line-height: 1.75rem;
}
.text-16 {
  font-size: 1rem;
  line-height: 1.25rem;
}
.text-14 {
  font-size: 0.875rem;
  line-height: 1.25rem;
}
.text-12 {
  font-size: 0.75rem;
  line-height: 1rem;
}
.\!text-12 {
  font-size: 0.75rem !important;
  line-height: 1rem !important;
}
.text-\[32px\] {
  font-size: 32px;
}
.text-20 {
  font-size: 1.25rem;
  line-height: 1.25rem;
}
.\!text-\[32px\] {
  font-size: 32px !important;
}
.text-\[14px\] {
  font-size: 14px;
}
.text-\[12px\] {
  font-size: 12px;
}
.text-18 {
  font-size: 1.125rem;
  line-height: 1.5rem;
}
.text-64 {
  font-size: 4rem;
  line-height: 4rem;
}
.text-32 {
  font-size: 2rem;
  line-height: 2.25rem;
}
.text-10 {
  font-size: 0.625rem;
  line-height: 1rem;
}
.text-48 {
  font-size: 3rem;
  line-height: 3rem;
}
.font-semibold {
  font-weight: 600;
}
.font-bold {
  font-weight: 700;
}
.font-normal {
  font-weight: 400;
}
.uppercase {
  text-transform: uppercase;
}
.lowercase {
  text-transform: lowercase;
}
.capitalize {
  text-transform: capitalize;
}
.italic {
  font-style: italic;
}
.not-italic {
  font-style: normal;
}
.ordinal {
  --tw-ordinal: ordinal;
  font-variant-numeric: var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction);
}
.leading-5 {
  line-height: 1.25rem;
}
.leading-4 {
  line-height: 1rem;
}
.\!leading-none {
  line-height: 1 !important;
}
.leading-\[16px\] {
  line-height: 16px;
}
.leading-\[14px\] {
  line-height: 14px;
}
.leading-\[20px\] {
  line-height: 20px;
}
.leading-6 {
  line-height: 1.5rem;
}
.leading-none {
  line-height: 1;
}
.leading-3 {
  line-height: .75rem;
}
.leading-8 {
  line-height: 2rem;
}
.leading-normal {
  line-height: 1.5;
}
.leading-9 {
  line-height: 2.25rem;
}
.leading-7 {
  line-height: 1.75rem;
}
.tracking-normal {
  letter-spacing: 0em;
}
.tracking-widest {
  letter-spacing: 0.1em;
}
.text-white {
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}
.text-neutral-content-strong {
  color: var(--color-neutral-content-strong);
}
.text-neutral-content-weak {
  color: var(--color-neutral-content-weak);
}
.text-coolgray-900 {
  --tw-text-opacity: 1;
  color: rgb(11 20 22 / var(--tw-text-opacity));
}
.text-primary {
  color: var(--color-primary);
}
.text-action-primary {
  color: var(--color-action-primary);
}
.text-secondary-weak {
  color: var(--color-secondary-weak);
}
.text-neutral-content {
  color: var(--color-neutral-content);
}
.text-global-white {
  color: var(--color-global-white);
}
.text-tone-3 {
  color: var(--color-tone-3);
}
.text-global-alienblue {
  color: var(--color-global-alienblue);
}
.text-tone-1 {
  color: var(--color-tone-1);
}
.text-action-secondary {
  color: var(--color-action-secondary);
}
.text-primary-background-hover {
  color: var(--color-primary-background-hover);
}
.text-category-nsfw {
  color: var(--color-category-nsfw);
}
.text-tone-2 {
  color: var(--color-tone-2);
}
.text-puregray-400 {
  --tw-text-opacity: 1;
  color: rgb(172 172 172 / var(--tw-text-opacity));
}
.text-danger-content {
  color: var(--color-danger-content);
}
.text-tone-7 {
  color: var(--color-tone-7);
}
.text-primary-background {
  color: var(--color-primary-background);
}
.text-identity-moderator {
  color: var(--color-identity-moderator);
}
.text-alert-negative {
  color: var(--color-alert-negative);
}
.text-coolgray-850 {
  --tw-text-opacity: 1;
  color: rgb(15 26 28 / var(--tw-text-opacity));
}
.text-coolgray-650 {
  --tw-text-opacity: 1;
  color: rgb(42 60 66 / var(--tw-text-opacity));
}
.text-coolgray-550 {
  --tw-text-opacity: 1;
  color: rgb(75 96 102 / var(--tw-text-opacity));
}
.text-neutral-background-strong {
  color: var(--color-neutral-background-strong);
}
.text-periwinkle-500 {
  --tw-text-opacity: 1;
  color: rgb(106 92 255 / var(--tw-text-opacity));
}
.text-coolgray-950 {
  --tw-text-opacity: 1;
  color: rgb(4 9 10 / var(--tw-text-opacity));
}
.text-action-downvote {
  color: var(--color-action-downvote);
}
.text-global-black {
  color: var(--color-global-black);
}
.text-secondary {
  color: var(--color-secondary);
}
.text-alert-caution {
  color: var(--color-alert-caution);
}
.text-current {
  color: currentColor;
}
.text-category-spoiler {
  color: var(--color-category-spoiler);
}
.text-warning-content {
  color: var(--color-warning-content);
}
.text-primary-onBackground {
  color: var(--color-primary-onBackground);
}
.text-brand-onBackground {
  color: var(--color-brand-onBackground);
}
.text-neutral-content-disabled {
  color: var(--color-neutral-content-disabled);
}
.text-\[color\:var\(--button-color-text-default\)\] {
  color: var(--button-color-text-default);
}
.text-secondary-onBackground {
  color: var(--color-secondary-onBackground);
}
.text-\[color\:var\(--color-button-secondary-text-disabled\)\] {
  color: var(--color-button-secondary-text-disabled);
}
.text-\[color\:var\(--color-button-plain-text-disabled\)\] {
  color: var(--color-button-plain-text-disabled);
}
.underline {
  text-decoration-line: underline;
}
.line-through {
  text-decoration-line: line-through;
}
.no-underline {
  text-decoration-line: none;
}
.opacity-25 {
  opacity: 0.25;
}
.opacity-75 {
  opacity: 0.75;
}
.opacity-0 {
  opacity: 0;
}
.opacity-100 {
  opacity: 1;
}
.opacity-30 {
  opacity: 0.3;
}
.opacity-50 {
  opacity: 0.5;
}
.opacity-20 {
  opacity: 0.2;
}
.opacity-60 {
  opacity: 0.6;
}
.opacity-40 {
  opacity: 0.4;
}
.shadow-none {
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}
.shadow-sm {
  --tw-shadow: var(--elevation-sm);
  --tw-shadow-colored: var(--elevation-sm);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}
.shadow-md {
  --tw-shadow: var(--elevation-md);
  --tw-shadow-colored: var(--elevation-md);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}
.outline-none {
  outline: 2px solid transparent;
  outline-offset: 2px;
}
.outline {
  outline-style: solid;
}
.ring {
  --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
  --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(3px + var(--tw-ring-offset-width)) var(--tw-ring-color);
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}
.drop-shadow {
  --tw-drop-shadow: drop-shadow(0 1px 2px rgb(0 0 0 / 0.1)) drop-shadow(0 1px 1px rgb(0 0 0 / 0.06));
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}
.grayscale {
  --tw-grayscale: grayscale(100%);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}
.invert {
  --tw-invert: invert(100%);
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}
.transition {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
.transition-transform {
  transition-property: transform;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
.transition-opacity {
  transition-property: opacity;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
.duration-150 {
  transition-duration: 150ms;
}
.duration-300 {
  transition-duration: 300ms;
}
.duration-100 {
  transition-duration: 100ms;
}
.duration-1000 {
  transition-duration: 1000ms;
}
.ease-out {
  transition-timing-function: cubic-bezier(0, 0, 0.2, 1);
}
.ease-in-out {
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}
.ease-linear {
  transition-timing-function: linear;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.\[-webkit-line-clamp\:3\] {
  -webkit-line-clamp: 3;
}
.\[text-overflow\:ellipsis\] {
  text-overflow: ellipsis;
}
.\[display\:-webkit-box\] {
  display: -webkit-box;
}
.\[-webkit-box-orient\:vertical\] {
  -webkit-box-orient: vertical;
}
.before\:absolute::before {
  content: var(--tw-content);
  position: absolute;
}
.before\:top-\[28px\]::before {
  content: var(--tw-content);
  top: 28px;
}
.before\:left-\[9px\]::before {
  content: var(--tw-content);
  left: 9px;
}
.before\:top-\[-6px\]::before {
  content: var(--tw-content);
  top: -6px;
}
.before\:left-\[-6\.5px\]::before {
  content: var(--tw-content);
  left: -6.5px;
}
.before\:top-0::before {
  content: var(--tw-content);
  top: 0px;
}
.before\:left-\[11\.5px\]::before {
  content: var(--tw-content);
  left: 11.5px;
}
.before\:top-\[-3px\]::before {
  content: var(--tw-content);
  top: -3px;
}
.before\:left-\[-16\.5px\]::before {
  content: var(--tw-content);
  left: -16.5px;
}
.before\:left-\[16\.5px\]::before {
  content: var(--tw-content);
  left: 16.5px;
}
.before\:h-\[calc\(100\%-28px\)\]::before {
  content: var(--tw-content);
  height: calc(100% - 28px);
}
.before\:h-full::before {
  content: var(--tw-content);
  height: 100%;
}
.before\:h-\[calc\(100\%\+6px\)\]::before {
  content: var(--tw-content);
  height: calc(100% + 6px);
}
.before\:border-y-0::before {
  content: var(--tw-content);
  border-top-width: 0rem;
  border-bottom-width: 0rem;
}
.before\:border-l-\[1px\]::before {
  content: var(--tw-content);
  border-left-width: 1px;
}
.before\:border-r-\[0px\]::before {
  content: var(--tw-content);
  border-right-width: 0px;
}
.before\:border-solid::before {
  content: var(--tw-content);
  border-style: solid;
}
.before\:border-tone-4::before {
  content: var(--tw-content);
  border-color: var(--color-tone-4);
}
.before\:content-\[\'\'\]::before {
  --tw-content: '';
  content: var(--tw-content);
}
.after\:absolute::after {
  content: var(--tw-content);
  position: absolute;
}
.after\:-top-\[8px\]::after {
  content: var(--tw-content);
  top: -8px;
}
.after\:-left-\[6\.5px\]::after {
  content: var(--tw-content);
  left: -6.5px;
}
.after\:bottom-\[15px\]::after {
  content: var(--tw-content);
  bottom: 15px;
}
.after\:left-\[11\.5px\]::after {
  content: var(--tw-content);
  left: 11.5px;
}
.after\:-top-sm::after {
  content: var(--tw-content);
  top: -0.75rem;
}
.after\:left-\[-16\.5px\]::after {
  content: var(--tw-content);
  left: -16.5px;
}
.after\:left-\[3\.5px\]::after {
  content: var(--tw-content);
  left: 3.5px;
}
.after\:h-\[20px\]::after {
  content: var(--tw-content);
  height: 20px;
}
.after\:h-\[54px\]::after {
  content: var(--tw-content);
  height: 54px;
}
.after\:h-\[26px\]::after {
  content: var(--tw-content);
  height: 26px;
}
.after\:h-\[30px\]::after {
  content: var(--tw-content);
  height: 30px;
}
.after\:w-\[6px\]::after {
  content: var(--tw-content);
  width: 6px;
}
.after\:w-md::after {
  content: var(--tw-content);
  width: 1rem;
}
.after\:w-\[23px\]::after {
  content: var(--tw-content);
  width: 23px;
}
.after\:rounded-bl-\[12px\]::after {
  content: var(--tw-content);
  border-bottom-left-radius: 12px;
}
.after\:border-y-0::after {
  content: var(--tw-content);
  border-top-width: 0rem;
  border-bottom-width: 0rem;
}
.after\:border-l-\[1px\]::after {
  content: var(--tw-content);
  border-left-width: 1px;
}
.after\:border-r-\[0px\]::after {
  content: var(--tw-content);
  border-right-width: 0px;
}
.after\:border-b-\[1px\]::after {
  content: var(--tw-content);
  border-bottom-width: 1px;
}
.after\:border-solid::after {
  content: var(--tw-content);
  border-style: solid;
}
.after\:border-tone-4::after {
  content: var(--tw-content);
  border-color: var(--color-tone-4);
}
.after\:content-\[\'\'\]::after {
  --tw-content: '';
  content: var(--tw-content);
}
.first\:ml-0:first-child {
  margin-left: 0px;
}
.visited\:bg-transparent:visited {
  background-color: transparent;
}
.hover\:border-secondary-background-selected:hover {
  border-color: var(--color-secondary-background-selected);
}
.hover\:border-secondary-background-hover:hover {
  border-color: var(--color-secondary-background-hover);
}
.hover\:bg-neutral-background-hover:hover {
  background-color: var(--color-neutral-background-hover);
}
.hover\:bg-transparent:hover {
  background-color: transparent;
}
.hover\:bg-secondary-background-selected:hover {
  background-color: var(--color-secondary-background-selected);
}
.hover\:bg-secondary-background-hover:hover {
  background-color: var(--color-secondary-background-hover);
}
.hover\:bg-neutral-background-selected:hover {
  background-color: var(--color-neutral-background-selected);
}
.hover\:bg-brand-background-hover:hover {
  background-color: var(--color-brand-background-hover);
}
.hover\:text-secondary:hover {
  color: var(--color-secondary);
}
.hover\:text-danger-content-hover:hover {
  color: var(--color-danger-content-hover);
}
.hover\:text-secondary-hover:hover {
  color: var(--color-secondary-hover);
}
.hover\:text-global-white:hover {
  color: var(--color-global-white);
}
.hover\:text-action-upvote:hover {
  color: var(--color-action-upvote);
}
.hover\:text-action-downvote:hover {
  color: var(--color-action-downvote);
}
.hover\:underline:hover {
  text-decoration-line: underline;
}
.hover\:no-underline:hover {
  text-decoration-line: none;
}
.focus\:bg-transparent:focus {
  background-color: transparent;
}
.focus-visible\:text-action-upvote:focus-visible {
  color: var(--color-action-upvote);
}
.focus-visible\:text-action-downvote:focus-visible {
  color: var(--color-action-downvote);
}
.active\:bg-transparent:active {
  background-color: transparent;
}
.active\:bg-interactive-pressed:active {
  background-color: var(--color-interactive-pressed);
}
.active\:bg-secondary-background:active {
  background-color: var(--color-secondary-background);
}
.disabled\:bg-interactive-background-disabled:disabled {
  background-color: var(--color-interactive-background-disabled);
}
.disabled\:text-interactive-content-disabled:disabled {
  color: var(--color-interactive-content-disabled);
}


/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/vendors~Reddit.5e0ee9d505a551167136_.css.map*/</style><style data-href="chunkCSS/Governance~Reddit~Subreddit~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compo~bd4baca2.ed2e9c24ce3213d2fad1_.css" data-chunk="Reddit" key="chunkCSS/Governance~Reddit~Subreddit~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compo~bd4baca2.ed2e9c24ce3213d2fad1_.css">@keyframes _1tIZttmhLdrIGrB-6VvZcT{0%{opacity:0}to{opacity:1}}._3uK2I0hi3JFTKnMUFHD2Pd,.HQ2VJViRjokXpRbJzPvvc{--infoTextTooltip-overflow-left:0px;font-size:12px;font-weight:500;line-height:16px;padding:3px 9px;position:absolute;border-radius:4px;margin-top:-6px;background:#000;color:#fff;animation:_1tIZttmhLdrIGrB-6VvZcT .5s step-end;z-index:100;white-space:pre-wrap}._3uK2I0hi3JFTKnMUFHD2Pd:after,.HQ2VJViRjokXpRbJzPvvc:after{content:"";position:absolute;top:100%;left:calc(50% - 4px - var(--infoTextTooltip-overflow-left));width:0;height:0;border-top:3px solid #000;border-left:4px solid transparent;border-right:4px solid transparent}._3uK2I0hi3JFTKnMUFHD2Pd{margin-top:6px}._3uK2I0hi3JFTKnMUFHD2Pd:after{border-bottom:3px solid #000;border-top:none;bottom:100%;top:auto}
._2Gt13AX94UlLxkluAMsZqP{background-position:50%;background-repeat:no-repeat;background-size:contain;position:relative;display:inline-block}
._1QwShihKKlyRXyQSlqYaWW{height:16px;width:16px;vertical-align:bottom}._2X6EB3ZhEeXCh1eIVA64XM{margin-left:3px}._1jNPl3YUk6zbpLWdjaJT1r{font-size:12px;font-weight:500;line-height:16px;border-radius:2px;display:inline-block;margin-right:5px;overflow:hidden;text-overflow:ellipsis;vertical-align:text-bottom;white-space:pre;word-break:normal;padding:0 4px}._1jNPl3YUk6zbpLWdjaJT1r._39BEcWjOlYi1QGcJil6-yl{padding:0}._2hSecp_zkPm_s5ddV2htoj{font-size:12px;font-weight:500;line-height:16px;border-radius:2px;display:inline-block;margin-right:5px;overflow:hidden;text-overflow:ellipsis;vertical-align:text-bottom;white-space:pre;word-break:normal;margin-left:0;padding:0 4px}._2hSecp_zkPm_s5ddV2htoj._39BEcWjOlYi1QGcJil6-yl{padding:0}._1wzhGvvafQFOWAyA157okr{font-size:12px;font-weight:500;line-height:16px;border-radius:2px;margin-right:5px;overflow:hidden;text-overflow:ellipsis;vertical-align:text-bottom;white-space:pre;word-break:normal;box-sizing:border-box;line-height:14px;padding:0 4px}._3BPVpMSn5b1vb1yTQuqCRH,._1wzhGvvafQFOWAyA157okr{display:inline-block;height:16px}._3BPVpMSn5b1vb1yTQuqCRH{background-color:var(--newRedditTheme-body);border-radius:50%;margin-left:5px;text-align:center;width:16px}._2cvySYWkqJfynvXFOpNc5L{height:10px;width:10px}.aJrgrewN9C8x1Fusdx4hh{padding:2px 8px}._1wj6zoMi6hRP5YhJ8nXWXE{font-size:14px;padding:7px 12px}._2VqfzH0dZ9dIl3XWNxs42y{border-radius:20px}._2VqfzH0dZ9dIl3XWNxs42y:hover{opacity:.85}._2VqfzH0dZ9dIl3XWNxs42y:active{transform:scale(.95)}
._13svhQIUZqD9PVzFcLwOKT{font-size:12px;font-weight:400;line-height:16px;margin:4px 8px;white-space:nowrap;color:var(--newCommunityTheme-linkText);fill:var(--newCommunityTheme-linkText)}._13svhQIUZqD9PVzFcLwOKT:visited{color:var(--newCommunityTheme-linkTextWithBody);fill:var(--newCommunityTheme-linkTextWithBody)}._13svhQIUZqD9PVzFcLwOKT:hover{text-decoration:underline}
._3CquMWJ6RMh8E9D-_84AtZ{width:20px;height:20px;pointer-events:none}
._1Dl-kvSxyJMWO9nuoTof8N._1Dl-kvSxyJMWO9nuoTof8N{vertical-align:top}
.GnWcY6GPzeZ5rzsiQ98fo{background-size:cover;filter:blur(60px)}._2MkcR85HDnYngvlVW2gMMa{border-radius:4px;-ms-flex:1;flex:1;height:100%;width:100%;overflow:hidden;position:relative;vertical-align:bottom}._2hIvPRO2xz4rn9LXAJXYDa{color:var(--newCommunityTheme-button);height:20px;left:50%;margin-left:-10px;margin-top:-10px;pointer-events:none;position:absolute;top:50%;width:20px}._2hIvPRO2xz4rn9LXAJXYDa._10qSZsDWnOBwx4bc7GJ1QF{color:var(--newCommunityTheme-actionIcon)}._25ZOvQhQdAqwdxPd5z-KFB{display:none}._33Pa96SGhFVpZeI6a7Y_Pl{background-position:50% top;background-repeat:no-repeat;background-size:cover}.Fq7oYOARH1VVCaLAuAh37{background-position:50% 50%}.m0n699kowSp8Wfa40lqpF{background-color:var(--newCommunityTheme-button);border-top-left-radius:4px;bottom:0;height:18px;position:absolute;right:0;width:18px}.icon._2rOixIHGmpfZB93ihJsw3V{color:var(--newCommunityTheme-body);font-size:12px;line-height:18px;margin-left:4px;vertical-align:baseline}._2YO2O4rMRYYMeH_t2y8M5w{background-color:transparent;color:var(--newCommunityTheme-button);position:relative}._2c1ElNxHftd8W_nZtcG9zf{border-radius:4px;-ms-flex:1;flex:1;width:100%;border:1px solid;box-sizing:border-box}._2c1ElNxHftd8W_nZtcG9zf,._78ohNtfA1urjgUhnN1jLi{height:100%}._3HXDOeeCKnmgu_pIdoLofi{font-size:12px;font-weight:400;line-height:16px;color:var(--newCommunityTheme-body);margin-left:16px;max-width:124px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.lrzZ8b0L6AzLkQj5Ww7H1{display:inline-block}._2fiIRtMpITeCAzXc4cANKp{margin-bottom:10px;margin-right:10px;overflow:hidden}._2xu1HuBz1Yx6SP10AGVx_I{display:-ms-inline-flexbox;display:inline-flex;margin:0;padding:0;vertical-align:text-top}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/Governance~Reddit~Subreddit~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compo~bd4baca2.ed2e9c24ce3213d2fad1_.css.map*/</style><style data-href="chunkCSS/Reddit~StandalonePostPage~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compone~9b425435.8c84a9a99da41a2f4805_.css" data-chunk="Reddit" key="chunkCSS/Reddit~StandalonePostPage~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compone~9b425435.8c84a9a99da41a2f4805_.css">._26bOTAKvGixX5tMC3vGfTv{display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between}
._3nRJIwLuth2pKYrXnr2jPN{width:402px;max-width:100%;box-sizing:border-box}._3nRJIwLuth2pKYrXnr2jPN>*{border-bottom:1px solid var(--newCommunityTheme-line)}@media (max-width:640px){._3nRJIwLuth2pKYrXnr2jPN{width:360px}}
._30zvTaAcvBFmwfelq6Bvwg{vertical-align:middle}.BzonfS85jX2JTiu_i0Jyd{font-size:12px;font-weight:400;line-height:16px;border-bottom:none;color:var(--newCommunityTheme-bodyText);display:-ms-flexbox;display:flex;text-align:center;padding:22px 16px}.vynkb69RQyUY-PA6bCaW0,.BzonfS85jX2JTiu_i0Jyd{vertical-align:middle;white-space:nowrap}.vynkb69RQyUY-PA6bCaW0{box-sizing:border-box;margin-bottom:0;margin-left:8px;max-width:80%;overflow:hidden;text-overflow:ellipsis}
.Z7x0t_45z9vZGN2zw6US6{height:61px}.Z7x0t_45z9vZGN2zw6US6._3YjPWOd9tK9O_DN50RI_FN{height:24px}
.XZK-LTFT5CgGo9MvPQQsy{display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-align:center;align-items:center}
._11Rht_b1e-kmk12gkz7Lug{fill:var(--newCommunityTheme-actionIcon)}
._2e6fJknJ4noSygWYov8-F1:focus{outline:0 none}._2e6fJknJ4noSygWYov8-F1:focus ._1lzSnSABNXX12WerTnwqI3{border-radius:1000px;height:16px;width:16px;-ms-flex-preferred-size:16px;flex-basis:16px;border:2px solid -webkit-focus-ring-color}._2e6fJknJ4noSygWYov8-F1:focus ._1lzSnSABNXX12WerTnwqI3._1lzSnSABNXX12WerTnwqI3{border-color:Highlight}._3PYsg_uRJ6AGptv-hi7kqu{fill:#0079d3}._1lzSnSABNXX12WerTnwqI3,._3PYsg_uRJ6AGptv-hi7kqu{-ms-flex:0 0 16px;flex:0 0 16px;height:16px;margin-right:6px;width:16px}
._3z5CnRH3l7hQGI8TQYFyqX{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row-reverse;flex-direction:row-reverse;height:12px;line-height:1;overflow:hidden;position:relative}._3z5CnRH3l7hQGI8TQYFyqX .WBY6J5DJsZFZXSxBqtq0F{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;height:100%;transition:all ease;transform:translateY(0);line-height:1}._3z5CnRH3l7hQGI8TQYFyqX .WBY6J5DJsZFZXSxBqtq0F ._3LT2yD0gRFklddn3Ra9ElD{height:100%}._3z5CnRH3l7hQGI8TQYFyqX .D6SuXeSnAAagG8dKAb4O4{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
._1jsc29CjRXZWjd2tr0Ji0Y,._1jsc29CjRXZWjd2tr0Ji0Y:after{height:0;position:absolute;width:0}._1jsc29CjRXZWjd2tr0Ji0Y:after{background:#000;content:""}._2J_zB4R1FH2EjGMkQjedwc[data-popper-placement^=top]>._1jsc29CjRXZWjd2tr0Ji0Y{border-left:4px solid transparent;border-right:4px solid transparent;border-top:3px solid #000;bottom:-3px}._2J_zB4R1FH2EjGMkQjedwc[data-popper-placement^=bottom]>._1jsc29CjRXZWjd2tr0Ji0Y{border-bottom:3px solid #000;border-left:4px solid transparent;border-right:4px solid transparent;top:-3px}._2J_zB4R1FH2EjGMkQjedwc[data-popper-placement^=left]>._1jsc29CjRXZWjd2tr0Ji0Y{border-bottom:4px solid transparent;border-left:3px solid #000;border-top:4px solid transparent;right:-3px}._2J_zB4R1FH2EjGMkQjedwc[data-popper-placement^=right]>._1jsc29CjRXZWjd2tr0Ji0Y{border-bottom:4px solid transparent;border-right:3px solid #000;border-top:4px solid transparent;left:-3px}._2J_zB4R1FH2EjGMkQjedwc{font-size:12px;font-weight:500;line-height:16px;border-radius:4px;background:#000;color:#fff;opacity:0;padding:3px 9px;transition:opacity 0s step-end;white-space:pre-wrap;z-index:100}._2J_zB4R1FH2EjGMkQjedwc.u6HtAZu8_LKL721-EnKuR{opacity:1;transition-duration:.5s}
._1bdAduczElF9-gLoCvHz-p{background-color:var(--newRedditTheme-field);-ms-flex:1;flex:1;overflow-y:auto;padding:16px 0}._1bdAduczElF9-gLoCvHz-p ._2leID3tMN8hpvVd4XhEqTl{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}._1bdAduczElF9-gLoCvHz-p .FJIE5E2gciCA8q3Jzvcyg{cursor:pointer;line-height:16px;padding:4px 16px}._1bdAduczElF9-gLoCvHz-p .FJIE5E2gciCA8q3Jzvcyg:focus,._1bdAduczElF9-gLoCvHz-p .FJIE5E2gciCA8q3Jzvcyg:hover{background-color:#24a0ed;color:#fff;outline:none}._1bdAduczElF9-gLoCvHz-p ._3H_wwe03-Fkrm6oWGakXI8{fill:var(--newRedditTheme-actionIcon);height:16px;width:16px}._18cuM8Uu7RcIFu1bCT0r4t{position:relative;color:var(--newRedditTheme-actionIcon);margin:0 16px 16px}._18cuM8Uu7RcIFu1bCT0r4t ._2bECVWL_WJ9RGBx7-RnzfO{fill:currentColor;height:16px;left:12px;position:absolute;top:50%;transform:translateY(-50%);width:16px}._18cuM8Uu7RcIFu1bCT0r4t ._1nQbRaoAvb6Uy0oI-OfDtZ{background-color:var(--newRedditTheme-body);border-radius:4px;border:1px solid;box-sizing:border-box;color:var(--newRedditTheme-bodyText);height:48px;padding:0 16px 0 32px;width:100%}
._3g_cwSqBe5o5mAuhfMeGu5{margin:0 6px}._3g_cwSqBe5o5mAuhfMeGu5:before{content:"·"}.t4Hq30BDzTeJ85vREX7_M{padding-left:8px;font-size:12px}
._2AKP6aCod0Z6TuXXfc1ZqL{height:380px;-ms-flex-flow:column nowrap;flex-flow:column nowrap}._3w7b_fPwMuVD17J7epjTXi,._2AKP6aCod0Z6TuXXfc1ZqL{display:-ms-flexbox;display:flex}._3w7b_fPwMuVD17J7epjTXi{background:var(--newRedditTheme-line);border:none;-ms-flex-direction:row-reverse;flex-direction:row-reverse;padding:16px}._3w7b_fPwMuVD17J7epjTXi ._3WykjMvdVO5xibqd5xlfTC{color:var(--newRedditTheme-actionIcon);margin:0 8px}.SVd7IxchgiWetdYbftTHx{background:var(--newRedditTheme-body);padding:16px}.SVd7IxchgiWetdYbftTHx .KTa3kg9lzGPUeLuhAHMT_{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;color:var(--newRedditTheme-metaText);margin-bottom:8px}.SVd7IxchgiWetdYbftTHx ._1fV9kJfKnED9qQ2AF8f3iT{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px;color:var(--newRedditTheme-bodyText);margin-bottom:8px}
._1rZYMD_4xY3gRcSS3p8ODO{font-size:12px;font-weight:700;line-height:16px;pointer-events:none;word-break:normal}.uFieChpcVxrPI9VvCKqZu{font-size:16px;color:var(--newCommunityTheme-actionIcon)}._3bAGP2FKe97ijgBAGQOYsk{padding-left:0;white-space:nowrap}
.dLp3R7pmxclGjLS87yr5S{display:inline-block;vertical-align:middle;color:#ff4500}
.ogOEj4x-0BpDZWeccJwxx{min-width:84px}._2YxEi97B6Nm7NCgLG6pCud{line-height:22px;margin:10px 0;white-space:pre-wrap}
._1bFyAea2u1QxOQ1F5B4GkN{margin-left:-40px}._2HRj2_i58dkRRJQoLcPYos{display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-align:center;align-items:center;box-sizing:border-box;height:68px;padding:10px 14px;margin:8px 8px 10px;gap:10px;background:#fff;border-radius:4px;border:1.5px solid #edeff1}._1gHnZ35aZq6j7V6-yJI8Ex ._2HRj2_i58dkRRJQoLcPYos{background:#1a1a1b;border:1.5px solid #343536}._3-103Q5oLObJuUD_Kw30cF{margin-top:2px;color:var(--newCommunityTheme-button)}._1DC_jVf8m3dNMZizsj84j1{font-size:12px;font-weight:500;line-height:16px;color:var(--newCommunityTheme-titleText);font-weight:700}._142PYc7s46KPZKVON3XAN8{font-size:12px;line-height:16px;width:325px;color:var(--newCommunityTheme-metaText)}._1bYeQt_TV5_-qyJ0ou4R4g{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;margin-right:auto}.pSzvw13UmARlu2u6QGtsR{-ms-flex-negative:0;flex-shrink:0;padding:4px 14px}._38B5eqRnC0dTpzLkC_7APC{font-size:12px;font-weight:500;line-height:16px;font-weight:700}._3k7l59W74Y3dHDNBrT9oce{margin-left:4px}._9PWeID-JtyhyViXeQFfuq{color:var(--newCommunityTheme-postIcon)}
@media (max-width:709px){._3yh2bniLq7bYr4BaiXowdO._2sAFaB0tx4Hd5KxVkdUcAx._3sUJGnemgtNczijwoT8PGg{display:none}}@media (max-width:1079px){._3yh2bniLq7bYr4BaiXowdO._2sAFaB0tx4Hd5KxVkdUcAx._28vEaVlLWeas1CDiLuTCap,._3yh2bniLq7bYr4BaiXowdO._2sAFaB0tx4Hd5KxVkdUcAx.Z-VR19FVnE3nOS0_BU4Wy{display:none}}@media (max-width:-1px){._3yh2bniLq7bYr4BaiXowdO._1EKOhBHXAW9y8Bgn93c9f3._28vEaVlLWeas1CDiLuTCap,._3yh2bniLq7bYr4BaiXowdO._1EKOhBHXAW9y8Bgn93c9f3._3sUJGnemgtNczijwoT8PGg{display:none}}@media (max-width:519px){._3yh2bniLq7bYr4BaiXowdO._1EKOhBHXAW9y8Bgn93c9f3.Z-VR19FVnE3nOS0_BU4Wy{display:none}}@media (max-width:419px){._3yh2bniLq7bYr4BaiXowdO._1pShbCnOaF7EGWTq6IvZux._3sUJGnemgtNczijwoT8PGg{display:none}}@media (max-width:519px){._3yh2bniLq7bYr4BaiXowdO._1pShbCnOaF7EGWTq6IvZux._28vEaVlLWeas1CDiLuTCap{display:none}}@media (max-width:459px){._3yh2bniLq7bYr4BaiXowdO._1pShbCnOaF7EGWTq6IvZux.Z-VR19FVnE3nOS0_BU4Wy{display:none}}@media (max-width:1039px){._3yh2bniLq7bYr4BaiXowdO._1EWxiIupuIjiExPQeK4Kud._3sUJGnemgtNczijwoT8PGg{display:none}}@media (max-width:459px){._3yh2bniLq7bYr4BaiXowdO._1EWxiIupuIjiExPQeK4Kud._28vEaVlLWeas1CDiLuTCap{display:none}}@media (max-width:1039px){._3yh2bniLq7bYr4BaiXowdO._1EWxiIupuIjiExPQeK4Kud.Z-VR19FVnE3nOS0_BU4Wy{display:none}}@media (min-width:710px){._1k3nXWGGz2NdPr8dg49Tbs._2sAFaB0tx4Hd5KxVkdUcAx._3sUJGnemgtNczijwoT8PGg{display:none}}@media (min-width:1080px){._1k3nXWGGz2NdPr8dg49Tbs._2sAFaB0tx4Hd5KxVkdUcAx._28vEaVlLWeas1CDiLuTCap,._1k3nXWGGz2NdPr8dg49Tbs._2sAFaB0tx4Hd5KxVkdUcAx.Z-VR19FVnE3nOS0_BU4Wy{display:none}}@media (min-width:0){._1k3nXWGGz2NdPr8dg49Tbs._1EKOhBHXAW9y8Bgn93c9f3._28vEaVlLWeas1CDiLuTCap,._1k3nXWGGz2NdPr8dg49Tbs._1EKOhBHXAW9y8Bgn93c9f3._3sUJGnemgtNczijwoT8PGg{display:none}}@media (min-width:520px){._1k3nXWGGz2NdPr8dg49Tbs._1EKOhBHXAW9y8Bgn93c9f3.Z-VR19FVnE3nOS0_BU4Wy{display:none}}@media (min-width:420px){._1k3nXWGGz2NdPr8dg49Tbs._1pShbCnOaF7EGWTq6IvZux._3sUJGnemgtNczijwoT8PGg{display:none}}@media (min-width:520px){._1k3nXWGGz2NdPr8dg49Tbs._1pShbCnOaF7EGWTq6IvZux._28vEaVlLWeas1CDiLuTCap{display:none}}@media (min-width:460px){._1k3nXWGGz2NdPr8dg49Tbs._1pShbCnOaF7EGWTq6IvZux.Z-VR19FVnE3nOS0_BU4Wy{display:none}}@media (min-width:1040px){._1k3nXWGGz2NdPr8dg49Tbs._1EWxiIupuIjiExPQeK4Kud._3sUJGnemgtNczijwoT8PGg{display:none}}@media (min-width:460px){._1k3nXWGGz2NdPr8dg49Tbs._1EWxiIupuIjiExPQeK4Kud._28vEaVlLWeas1CDiLuTCap{display:none}}@media (min-width:1040px){._1k3nXWGGz2NdPr8dg49Tbs._1EWxiIupuIjiExPQeK4Kud.Z-VR19FVnE3nOS0_BU4Wy{display:none}}
._3-miAEojrCvx_4FQ8x3P-s{font-size:12px;font-weight:700;line-height:16px;-ms-flex-align:stretch;align-items:stretch;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;overflow:hidden;padding:0 8px 0 4px;-ms-flex-positive:1;flex-grow:1}@media (max-width:639px){._3-miAEojrCvx_4FQ8x3P-s{margin-right:-40px}}._3-miAEojrCvx_4FQ8x3P-s .YszYBnnIoNY8pZ6UwCivd{border-radius:2px;margin-right:4px;padding:8px;text-transform:capitalize;white-space:nowrap;width:auto;word-break:normal;word-wrap:normal;height:100%}._3-miAEojrCvx_4FQ8x3P-s .YszYBnnIoNY8pZ6UwCivd:focus,._3-miAEojrCvx_4FQ8x3P-s .YszYBnnIoNY8pZ6UwCivd:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}._3U_7i38RDPV5eBv7m4M-9J{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex}._70940WUuFmpHbhKlj8EjZ{overflow:hidden;text-overflow:ellipsis;line-height:12px;max-height:36px;display:-webkit-inline-box;-webkit-line-clamp:3;white-space:normal;-webkit-box-orient:vertical}.WH45FmM2j_4Snucem7pcm{overflow:visible}.x7sinePdvDKj7bf-cdm4Z{border-right:1px solid var(--newCommunityTheme-line);height:16px;margin-left:4px;vertical-align:middle}._21pmAV9gWG6F_UKVe7YIE0{-ms-flex:1 1 auto;flex:1 1 auto}._15c1hqseW25EvRu0WP2Dq5,._6_44iTtZoeY6_XChKt5b0{vertical-align:middle}._6_44iTtZoeY6_XChKt5b0{display:inline-block;line-height:1;text-align:left;overflow:hidden;text-overflow:ellipsis;line-height:12px;max-height:36px;display:-webkit-inline-box;-webkit-line-clamp:3;white-space:normal;-webkit-box-orient:vertical}._2qww3J5KKzsD7e5DO0BvvU,._3NIVQWStkLT7RXnwKpKNuT{margin-right:4px}._2qww3J5KKzsD7e5DO0BvvU{padding:8px;word-break:normal}._2qww3J5KKzsD7e5DO0BvvU>.YCL-CnLJKXzXbwuLZEyh1{overflow:hidden;text-overflow:ellipsis;line-height:12px;max-height:36px;display:-webkit-inline-box;-webkit-line-clamp:3;white-space:normal;-webkit-box-orient:vertical}.kU8ebCMnbXfjCWfqn0WPb{border-radius:2px;padding:8px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;text-transform:capitalize;height:100%}.kU8ebCMnbXfjCWfqn0WPb:focus,.kU8ebCMnbXfjCWfqn0WPb:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}.kU8ebCMnbXfjCWfqn0WPb ._1GQDWqbF-wkYWbrpmOvjqJ{line-height:16px;margin-right:6px}._JRBNstMcGxbZUxrrIKXe{margin:0 4px 0 0;width:auto;word-break:normal}._3rnnBQZL1OOttG3tFn629n{margin-bottom:4px}._3rnnBQZL1OOttG3tFn629n._1rz4qmtk19qk1KbsKVMbAq p{width:45px;white-space:normal}._3MmwvEEt6fv5kQPFCVJizH{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-pack:center;justify-content:center}.icon._3yNNYT3e1avhAAWVHd0-92{display:inline-block;line-height:18px}.icon._1Xe01txJfRB9udUU85DNeR{display:inline-block;margin-right:-2px}
.voteButton{height:24px;width:24px}.voteButton:focus{border-radius:2px;background-color:var(--newCommunityTheme-navIconFaded10);outline:none}._1E9mcoVn4MYnuBQSVDt1gC{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;fill:inherit;-ms-flex-direction:column;flex-direction:column}.nmB1I04Z-G4nY3g3s_17F{animation:nmB1I04Z-G4nY3g3s_17F .4s ease 0s 1 both}._1L6r7KisMt3CYUGWSEMGiR{animation:_1L6r7KisMt3CYUGWSEMGiR .4s ease 0s 1 both}@keyframes nmB1I04Z-G4nY3g3s_17F{0%{transform:translateY(0)}50%{transform:translateY(-10px)}90%{transform:translateY(2px)}to{transform:translateY(0)}}@keyframes _1L6r7KisMt3CYUGWSEMGiR{0%{transform:translateY(0)}50%{transform:translateY(10px)}90%{transform:translateY(-2px)}to{transform:translateY(0)}}.mvlZFfW9BWm1bmljE_0Rg{cursor:not-allowed}
._3ryJoIoycVkA88fy40qNJc{font-size:12px;font-weight:700;line-height:16px;color:var(--newCommunityTheme-bodyText);display:inline;line-height:20px;text-decoration:none;vertical-align:baseline}._3ryJoIoycVkA88fy40qNJc:hover{text-decoration:underline}
.Oqp_3zg4nUr27VgCF82qt{display:-ms-flexbox;display:flex}._3DV09faePsSW4n6z5V2kj1{margin-top:4px}.ITg0gjNXOhVKsSbURGUvp{margin-right:0}._2q9Jd9uoQVrgF0qTQz8xC1{width:250px}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/Reddit~StandalonePostPage~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compone~9b425435.8c84a9a99da41a2f4805_.css.map*/</style><style data-href="chunkCSS/Reddit~RichTextEditor~reddit-components-MediumPost~reddit-components-NotificationUnit-Button~removal~87f825ba.5569bbcfca5096e59799_.css" data-chunk="Reddit" key="chunkCSS/Reddit~RichTextEditor~reddit-components-MediumPost~reddit-components-NotificationUnit-Button~removal~87f825ba.5569bbcfca5096e59799_.css">._2FKpII1jz0h6xCAw1kQAvS{background-color:#fff;box-shadow:0 0 0 1px rgba(0,0,0,.1),0 2px 3px 0 rgba(0,0,0,.2);transition:left .15s linear;border-radius:57%;width:57%}._2FKpII1jz0h6xCAw1kQAvS:after{content:"";padding-top:100%;display:block}._2e2g485kpErHhJQUiyvvC2{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-pack:start;justify-content:flex-start;background-color:var(--newCommunityTheme-navIconFaded10);border:2px solid transparent;border-radius:100px;cursor:pointer;position:relative;width:35px;transition:border-color .15s linear,background-color .15s linear}._2e2g485kpErHhJQUiyvvC2._3kUvbpMbR21zJBboDdBH7D{background-color:var(--newRedditTheme-navIconFaded10)}._2e2g485kpErHhJQUiyvvC2._3kUvbpMbR21zJBboDdBH7D._1L5kUnhRYhUJ4TkMbOTKkI{background-color:var(--newRedditTheme-active)}._2e2g485kpErHhJQUiyvvC2._3kUvbpMbR21zJBboDdBH7D._1L5kUnhRYhUJ4TkMbOTKkI._3clF3xRMqSWmoBQpXv8U5z{background-color:var(--newRedditTheme-buttonAlpha10)}._2e2g485kpErHhJQUiyvvC2._1asGWL2_XadHoBuUlNArOq{border-width:2.25px;height:24px;width:37.5px}._2e2g485kpErHhJQUiyvvC2._1asGWL2_XadHoBuUlNArOq ._2FKpII1jz0h6xCAw1kQAvS{height:19.5px;width:19.5px}._2e2g485kpErHhJQUiyvvC2._1hku5xiXsbqzLmszstPyR3{border-width:3px;height:32px;width:50px}._2e2g485kpErHhJQUiyvvC2._1hku5xiXsbqzLmszstPyR3 ._2FKpII1jz0h6xCAw1kQAvS{height:26px;width:26px}._2e2g485kpErHhJQUiyvvC2._10hZCcuqkss2sf5UbBMCSD{border-width:3.75px;height:40px;width:62.5px}._2e2g485kpErHhJQUiyvvC2._10hZCcuqkss2sf5UbBMCSD ._2FKpII1jz0h6xCAw1kQAvS{height:32.5px;width:32.5px}._2e2g485kpErHhJQUiyvvC2._1fCdbQCDv6tiX242k80-LO{border-width:4.5px;height:48px;width:75px}._2e2g485kpErHhJQUiyvvC2._1fCdbQCDv6tiX242k80-LO ._2FKpII1jz0h6xCAw1kQAvS{height:39px;width:39px}._2e2g485kpErHhJQUiyvvC2._2Jp5Pv4tgpAsTcnUzTsXgO{border-width:5.25px;height:56px;width:87.5px}._2e2g485kpErHhJQUiyvvC2._2Jp5Pv4tgpAsTcnUzTsXgO ._2FKpII1jz0h6xCAw1kQAvS{height:45.5px;width:45.5px}._2e2g485kpErHhJQUiyvvC2._1L5kUnhRYhUJ4TkMbOTKkI{-ms-flex-pack:end;justify-content:flex-end;background-color:var(--newCommunityTheme-active)}._2e2g485kpErHhJQUiyvvC2._3clF3xRMqSWmoBQpXv8U5z{cursor:default}._2e2g485kpErHhJQUiyvvC2._3clF3xRMqSWmoBQpXv8U5z ._2FKpII1jz0h6xCAw1kQAvS{box-shadow:none}._2e2g485kpErHhJQUiyvvC2._1L5kUnhRYhUJ4TkMbOTKkI._3clF3xRMqSWmoBQpXv8U5z{background-color:var(--newCommunityTheme-buttonAlpha10)}
._3JOs2fo7GARfPQK9n9uvyr{position:absolute}._2GiazGbWQeG84CupoExWj9{font-size:12px;font-weight:700;line-height:16px}._2lSQO1uFdnaWbYRKtLg3H-{-ms-flex-align:center;align-items:center;position:absolute;right:4px}._2lSQO1uFdnaWbYRKtLg3H-:focus-visible{border-radius:9999px;height:20px}._1Vs6ZQxgSSIBCGCe2dcMoA{font-size:12px;font-weight:400;line-height:16px;color:var(--newRedditTheme-metaText)}._1qRmLv2PYGtqa3xyVEYz_R{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center}._2WVAyd_SvtylHMe7sKaua9{border:1px solid var(--newRedditTheme-line);border-radius:4px;box-shadow:none;color:var(--newRedditTheme-bodyText);height:32px;padding:0 24px 0 32px}._2WVAyd_SvtylHMe7sKaua9::-webkit-search-cancel-button{display:none}._1zG8KFMibgWr8ahovOZAUB{color:var(--newCommunityTheme-linkText)}._2i3sQHj_1l-LDzGfzQTjHM{padding:0 8px}._1rMy-IddyxrWMGR5hH5O1E{color:var(--newRedditTheme-postIcon)}._3AIIvG4My2zfaJh7r8TucE{position:relative}._34BFzBLxzKlRZTjBIHtnlh{line-height:20px;color:var(--newRedditTheme-line);padding:0 12px}.icon._1Z_UNdjZZu53GD24SI5BLG{color:var(--newRedditTheme-bodyText);font-size:16px}.icon._1rMy-IddyxrWMGR5hH5O1E{font-size:16px;font-weight:700}.icon._380giGvmbbYVTkgLoNx7ZP{font-size:12px;font-weight:700}
.XHbKeEqnW58ib9mTN6jnS{display:inline-block;fill:var(--newCommunityTheme-actionIcon);height:20px;margin-left:2px;width:20px;vertical-align:middle}.XHbKeEqnW58ib9mTN6jnS.u_kypUXmB-k1A5TcC8MI9{fill:var(--newRedditTheme-actionIcon)}
._2ulKn_zs7Y3LWsOqoFLHPo{background:var(--newCommunityTheme-body);border-bottom:1px solid var(--newCommunityTheme-line);display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;margin:0 48px 4px;padding:0 16px 4px 0}._2ulKn_zs7Y3LWsOqoFLHPo._3iO3U_i4YUx-2qahK_BTu1{padding:0 0 4px}._2ulKn_zs7Y3LWsOqoFLHPo ._1n6gZPmNQU56UBglU718cx.zW82EsY6Pakxpq4WWvsUG,._2ulKn_zs7Y3LWsOqoFLHPo ._1nMYOibX9neGRqvcaCrPDz.zW82EsY6Pakxpq4WWvsUG{border:none;padding:4px 8px 4px 0;text-transform:capitalize}._1avwNy0RnwlEwVEW-fwKCI{-ms-flex-pack:start;justify-content:flex-start}._1avwNy0RnwlEwVEW-fwKCI,._3N0NZT0gc58Hq7p0XRUjsH{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center}._3dAMO_XZMVp2K1JSO53ohA,._3LRBCA71BwLLXBNsSlY7HW{font-size:12px;font-weight:700;line-height:16px;color:var(--newCommunityTheme-linkText)}._3dAMO_XZMVp2K1JSO53ohA{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;margin-left:16px}._3dAMO_XZMVp2K1JSO53ohA._2_QzTCgd5SYB-X8CTqZf9T{margin-left:0;margin-right:16px}._3dAMO_XZMVp2K1JSO53ohA .JVPG0c9TNru5TLSq9sdUG{color:var(--newCommunityTheme-linkText);height:16px;margin-left:8px;width:26px}._3dAMO_XZMVp2K1JSO53ohA .JVPG0c9TNru5TLSq9sdUG div{height:12px;width:12px}._2MGxQvIhmM2I5CzPdSJTtM._2MGxQvIhmM2I5CzPdSJTtM{cursor:pointer;fill:var(--newCommunityTheme-linkText);margin:0 0 0 -5px}.uAIheeoxWlq57lu5ghv43{margin:0;padding:16px 0 0}._201SpO3todaXvcWUHaLymN{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex}._1urK6AxAk9Sl76RgLUHOqh{fill:var(--newCommunityTheme-linkText);height:16px;padding-left:4px;padding-top:2px;width:16px}._233thT4kQqtwrHDoMY0Dbv{padding-bottom:12px}.zW82EsY6Pakxpq4WWvsUG{font-size:12px;font-weight:700;letter-spacing:.5px;line-height:24px;text-transform:uppercase;background-color:inherit;border:none;letter-spacing:normal;color:var(--newCommunityTheme-linkText);display:-ms-flexbox;display:flex;width:auto}._1Pn7_008tGFVitpaAxNI9b{display:-ms-inline-flexbox;display:inline-flex;-ms-flex-align:center;align-items:center}._2iOrDLLjWlyPdmGh4fQMuE{color:var(--newCommunityTheme-bodyText)}@media (max-width:413px px){._2iOrDLLjWlyPdmGh4fQMuE{display:none}}._2C0TYCrsi0B3m8sQW0hmFv{font-size:12px;font-weight:700;line-height:16px;-ms-flex-align:center;align-items:center;color:var(--newCommunityTheme-linkText);margin-left:16px}._2C0TYCrsi0B3m8sQW0hmFv:focus{outline:0}._2C0TYCrsi0B3m8sQW0hmFv:hover{text-decoration:underline}._1MfL8RlT7Bsr76qYvR-nqM{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;color:var(--newCommunityTheme-metaText);cursor:pointer}._2PA6P-upB6MB4B4I4WgZGA{background-color:#373c3f;display:-ms-flexbox;display:flex;padding:8px 12px;text-align:center;width:230px}._2PA6P-upB6MB4B4I4WgZGA:after{border-top:3px solid #373c3f}._2Cjk95J3a3LyPUHsLEhO37{font-weight:400;margin-left:auto}._2Cjk95J3a3LyPUHsLEhO37,._3P3T6fdpdL6GGPyCM7zs9q{font-size:12px;line-height:16px;display:-ms-flexbox;display:flex}._3P3T6fdpdL6GGPyCM7zs9q{font-weight:700;-ms-flex-align:center;align-items:center;color:var(--newCommunityTheme-button);fill:var(--newCommunityTheme-button)}._3v-KNQB_UvJqSbWcQZmc0U{line-height:20px;color:var(--newRedditTheme-line);padding:0 12px}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/Reddit~RichTextEditor~reddit-components-MediumPost~reddit-components-NotificationUnit-Button~removal~87f825ba.5569bbcfca5096e59799_.css.map*/</style><style data-href="chunkCSS/Governance~ModListing~Reddit~ReportFlow.3f6a4b0a4bd41b00990b_.css" data-chunk="Reddit" key="chunkCSS/Governance~ModListing~Reddit~ReportFlow.3f6a4b0a4bd41b00990b_.css">._1tQt2CUWT3M7NNSMoh_o_4{cursor:auto;opacity:.3}
._37iEJpUpWXN00_fpZKHglg{display:none}
._1oxgVV3q47KbjEKqP5CHuM{margin-left:2px}._2uYY-KeuYHKiwl-9aF0UiL{border:1px solid var(--newCommunityTheme-line);border-radius:4px;box-shadow:0 2px 4px 0 var(--newCommunityTheme-bodyTextAlpha20);color:var(--newCommunityTheme-bodyText);overflow:hidden;background-color:var(--newCommunityTheme-body);position:absolute;z-index:10}._2uYY-KeuYHKiwl-9aF0UiL:focus{outline:none}
._2iuoyPiKHN3kfOoeIQalDT{-ms-flex-align:center;align-items:center;border-radius:9999px;box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;position:relative;text-align:center;width:auto}._34mIRHpFtnJ0Sk97S2Z3D9{width:100%}._1h6qKGhVsgNfytYFlo8m3f{min-height:16px;width:16px;padding:unset}._1h6qKGhVsgNfytYFlo8m3f ._1mvTX6krm3Q2d1CSyUm28s,._1h6qKGhVsgNfytYFlo8m3f i.icon._1mvTX6krm3Q2d1CSyUm28s{display:inline-block;height:12px;width:12px;font-size:12px;line-height:12px;padding:0}._1h6qKGhVsgNfytYFlo8m3f ._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy,._1h6qKGhVsgNfytYFlo8m3f i.icon._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy{float:left}._1h6qKGhVsgNfytYFlo8m3f ._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T,._1h6qKGhVsgNfytYFlo8m3f i.icon._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T{float:right}._3uJP0daPEH2plzVEYyTdaH{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:unset;line-height:16px;text-transform:unset;min-height:24px;min-width:24px;padding:4px 8px}._3uJP0daPEH2plzVEYyTdaH ._1mvTX6krm3Q2d1CSyUm28s,._3uJP0daPEH2plzVEYyTdaH i.icon._1mvTX6krm3Q2d1CSyUm28s{display:inline-block;height:16px;width:16px;font-size:16px;line-height:16px;padding:0 4px 0 0}._3uJP0daPEH2plzVEYyTdaH ._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy,._3uJP0daPEH2plzVEYyTdaH i.icon._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy{float:left}._3uJP0daPEH2plzVEYyTdaH ._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T,._3uJP0daPEH2plzVEYyTdaH i.icon._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T{float:right}.UEPNkU0rd1-nvbkOcBatc{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:unset;line-height:16px;text-transform:unset;min-height:24px;min-width:24px;padding:4px 16px}.UEPNkU0rd1-nvbkOcBatc ._1mvTX6krm3Q2d1CSyUm28s,.UEPNkU0rd1-nvbkOcBatc i.icon._1mvTX6krm3Q2d1CSyUm28s{display:inline-block;height:16px;width:16px;font-size:16px;line-height:16px;padding:0 4px 0 0}.UEPNkU0rd1-nvbkOcBatc ._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy,.UEPNkU0rd1-nvbkOcBatc i.icon._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy{float:left}.UEPNkU0rd1-nvbkOcBatc ._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T,.UEPNkU0rd1-nvbkOcBatc i.icon._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T{float:right}.HNozj_dKjQZ59ZsfEegz8{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:unset;line-height:17px;text-transform:unset;min-height:32px;min-width:32px;padding:4px 16px}.HNozj_dKjQZ59ZsfEegz8 ._1mvTX6krm3Q2d1CSyUm28s,.HNozj_dKjQZ59ZsfEegz8 i.icon._1mvTX6krm3Q2d1CSyUm28s{display:inline-block;padding:0 8px 0 0;height:20px;width:20px;font-size:20px;line-height:20px}.HNozj_dKjQZ59ZsfEegz8 ._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy,.HNozj_dKjQZ59ZsfEegz8 i.icon._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy{float:left}.HNozj_dKjQZ59ZsfEegz8 ._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T,.HNozj_dKjQZ59ZsfEegz8 i.icon._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T{float:right}._3ukcnQySDskQwK_wB2iXYl{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:unset;line-height:18px;text-transform:unset;min-height:40px;min-width:40px;padding:4px 16px}._3ukcnQySDskQwK_wB2iXYl ._1mvTX6krm3Q2d1CSyUm28s,._3ukcnQySDskQwK_wB2iXYl i.icon._1mvTX6krm3Q2d1CSyUm28s{display:inline-block;padding:0 8px 0 0;height:20px;width:20px;font-size:20px;line-height:20px}._3ukcnQySDskQwK_wB2iXYl ._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy,._3ukcnQySDskQwK_wB2iXYl i.icon._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy{float:left}._3ukcnQySDskQwK_wB2iXYl ._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T,._3ukcnQySDskQwK_wB2iXYl i.icon._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T{float:right}._1J4mN6_wNfCtSyMDUNGQqN{font-family:Noto Sans,Arial,sans-serif;font-size:16px;font-weight:700;letter-spacing:unset;line-height:20px;text-transform:unset;min-height:48px;min-width:48px;padding:4px 16px}._1J4mN6_wNfCtSyMDUNGQqN ._1mvTX6krm3Q2d1CSyUm28s,._1J4mN6_wNfCtSyMDUNGQqN i.icon._1mvTX6krm3Q2d1CSyUm28s{display:inline-block;padding:0 8px 0 0;height:20px;width:20px;font-size:20px;line-height:20px}._1J4mN6_wNfCtSyMDUNGQqN ._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy,._1J4mN6_wNfCtSyMDUNGQqN i.icon._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy{float:left}._1J4mN6_wNfCtSyMDUNGQqN ._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T,._1J4mN6_wNfCtSyMDUNGQqN i.icon._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T{float:right}.XpD6n11mOiKNg8ZKtvgVR{font-family:Noto Sans,Arial,sans-serif;font-size:18px;font-weight:700;letter-spacing:unset;line-height:22px;text-transform:unset;min-height:56px;min-width:56px;padding:4px 16px}.XpD6n11mOiKNg8ZKtvgVR ._1mvTX6krm3Q2d1CSyUm28s,.XpD6n11mOiKNg8ZKtvgVR i.icon._1mvTX6krm3Q2d1CSyUm28s{display:inline-block;padding:0 8px 0 0;height:24px;width:24px;font-size:24px;line-height:24px}.XpD6n11mOiKNg8ZKtvgVR ._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy,.XpD6n11mOiKNg8ZKtvgVR i.icon._1mvTX6krm3Q2d1CSyUm28s._1HHR_ND8U6x6YrIqKFeXZy{float:left}.XpD6n11mOiKNg8ZKtvgVR ._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T,.XpD6n11mOiKNg8ZKtvgVR i.icon._1mvTX6krm3Q2d1CSyUm28s._3tKmDp5VAtgWvabEmFkJ7T{float:right}._10BQ7pjWbeYP63SAPNS8Ts{position:relative;background-color:var(--newCommunityTheme-button);border:none;color:var(--newCommunityTheme-body);fill:var(--newCommunityTheme-body)}._10BQ7pjWbeYP63SAPNS8Ts:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-body);opacity:0}._10BQ7pjWbeYP63SAPNS8Ts:hover:before{opacity:.08}._10BQ7pjWbeYP63SAPNS8Ts:focus{outline:none}._10BQ7pjWbeYP63SAPNS8Ts:focus:before{opacity:.16}._10BQ7pjWbeYP63SAPNS8Ts._39a0Mt5b1i2joAqIaEHOWJ:before,._10BQ7pjWbeYP63SAPNS8Ts:active:before{opacity:.24}._10BQ7pjWbeYP63SAPNS8Ts:disabled,._10BQ7pjWbeYP63SAPNS8Ts[data-disabled],._10BQ7pjWbeYP63SAPNS8Ts[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:var(--newCommunityTheme-buttonTinted80);color:var(--newCommunityTheme-bodyAlpha50);fill:var(--newCommunityTheme-bodyAlpha50)}._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0{position:relative;background-color:var(--newRedditTheme-button);border:none;color:var(--newRedditTheme-body);fill:var(--newRedditTheme-body)}._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-body);opacity:0}._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0:hover:before{opacity:.08}._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0:focus{outline:none}._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0:focus:before{opacity:.16}._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0._39a0Mt5b1i2joAqIaEHOWJ:before,._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0:active:before{opacity:.24}._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0:disabled,._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0[data-disabled],._10BQ7pjWbeYP63SAPNS8Ts._2nelDm85zKKmuD94NequP0[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:var(--newRedditTheme-buttonTinted80);color:var(--newRedditTheme-bodyAlpha50);fill:var(--newRedditTheme-bodyAlpha50)}._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM{position:relative;background-color:#ff585b;border:none;color:var(--newCommunityTheme-body);fill:var(--newCommunityTheme-body)}._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-body);opacity:0}._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM:hover:before{opacity:.08}._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM:focus{outline:none}._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM:focus:before{opacity:.16}._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM._39a0Mt5b1i2joAqIaEHOWJ:before,._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM:active:before{opacity:.24}._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM:disabled,._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM[data-disabled],._10BQ7pjWbeYP63SAPNS8Ts._1t63zWyh9UUgsyQc6acROM[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:#ff595c;color:var(--newCommunityTheme-bodyAlpha50);fill:var(--newCommunityTheme-bodyAlpha50)}._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K{position:relative;background-color:#ddbd37;border:none;color:var(--newCommunityTheme-body);fill:var(--newCommunityTheme-body)}._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-body);opacity:0}._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K:hover:before{opacity:.08}._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K:focus{outline:none}._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K:focus:before{opacity:.16}._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K._39a0Mt5b1i2joAqIaEHOWJ:before,._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K:active:before{opacity:.24}._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K:disabled,._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K[data-disabled],._10BQ7pjWbeYP63SAPNS8Ts._10UWrWSil1Xu6pdSaa_3-K[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:#eede9b;color:var(--newCommunityTheme-bodyAlpha50);fill:var(--newCommunityTheme-bodyAlpha50)}._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-{--buttonText:#fff;position:relative;background-color:#ff4500;border:none;color:var(--buttonText);fill:var(--buttonText)}._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--buttonText);opacity:0}._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-:hover:before{opacity:.08}._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-:focus{outline:none}._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-:focus:before{opacity:.16}._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-._39a0Mt5b1i2joAqIaEHOWJ:before,._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-:active:before{opacity:.24}._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-:disabled,._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-[data-disabled],._10BQ7pjWbeYP63SAPNS8Ts.q_unSaY23rpdd3lDvGZ-[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:#ffa280;color:var(--newCommunityTheme-bodyAlpha50);fill:var(--newCommunityTheme-bodyAlpha50)}._2tU8R9NTqhvBrhoNAXWWcP{position:relative;border:1px solid var(--newCommunityTheme-button);color:var(--newCommunityTheme-button);fill:var(--newCommunityTheme-button)}._2tU8R9NTqhvBrhoNAXWWcP:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-button);opacity:0}._2tU8R9NTqhvBrhoNAXWWcP:hover:before{opacity:.04}._2tU8R9NTqhvBrhoNAXWWcP:focus{outline:none}._2tU8R9NTqhvBrhoNAXWWcP:focus:before{opacity:.08}._2tU8R9NTqhvBrhoNAXWWcP._39a0Mt5b1i2joAqIaEHOWJ:before,._2tU8R9NTqhvBrhoNAXWWcP:active:before{opacity:.16}._2tU8R9NTqhvBrhoNAXWWcP:disabled,._2tU8R9NTqhvBrhoNAXWWcP[data-disabled],._2tU8R9NTqhvBrhoNAXWWcP[disabled]{cursor:not-allowed;filter:grayscale(1);border-color:var(--newCommunityTheme-buttonAlpha50);color:var(--newCommunityTheme-buttonAlpha50);fill:var(--newCommunityTheme-buttonAlpha50)}._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0{position:relative;border:1px solid var(--newRedditTheme-button);color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-button);opacity:0}._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0:hover:before{opacity:.04}._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0:focus{outline:none}._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0:focus:before{opacity:.08}._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0._39a0Mt5b1i2joAqIaEHOWJ:before,._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0:active:before{opacity:.16}._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0:disabled,._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0[data-disabled],._2tU8R9NTqhvBrhoNAXWWcP._2nelDm85zKKmuD94NequP0[disabled]{cursor:not-allowed;filter:grayscale(1);border-color:var(--newRedditTheme-buttonAlpha50);color:var(--newRedditTheme-buttonAlpha50);fill:var(--newRedditTheme-buttonAlpha50)}.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5{--newRedditTheme-button:#0f1a1c;position:relative;background-color:var(--newCommunityTheme-field);border:1px solid transparent;color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-button);opacity:0}.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:hover:before{opacity:.08}.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:focus{outline:none}.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:focus:before{opacity:.16}.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5._39a0Mt5b1i2joAqIaEHOWJ:before,.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:active:before{opacity:.24}.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:disabled,.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5[data-disabled],.theme-light ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5[disabled]{cursor:not-allowed;filter:grayscale(1);background:none;color:var(--newRedditTheme-buttonAlpha50);fill:var(--newRedditTheme-buttonAlpha50)}.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5{--newRedditTheme-button:#0f1a1c;position:relative;background-color:var(--newCommunityTheme-button);border:1px solid transparent;color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-button);opacity:0}.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:hover:before{opacity:.08}.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:focus{outline:none}.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:focus:before{opacity:.16}.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5._39a0Mt5b1i2joAqIaEHOWJ:before,.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:active:before{opacity:.24}.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5:disabled,.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5[data-disabled],.theme-dark ._2tU8R9NTqhvBrhoNAXWWcP._2Z-LWN_PrkTncEM_mPuEW5[disabled]{cursor:not-allowed;filter:grayscale(1);background:none;color:var(--newRedditTheme-buttonAlpha50);fill:var(--newRedditTheme-buttonAlpha50)}._4Glnzr5LA7bNBGMWGW4pU{position:relative;background-color:var(--newCommunityTheme-field);border:1px solid transparent;color:var(--newCommunityTheme-button);fill:var(--newCommunityTheme-button)}._4Glnzr5LA7bNBGMWGW4pU:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-button);opacity:0}._4Glnzr5LA7bNBGMWGW4pU:hover:before{opacity:.08}._4Glnzr5LA7bNBGMWGW4pU:focus{outline:none}._4Glnzr5LA7bNBGMWGW4pU:focus:before{opacity:.16}._4Glnzr5LA7bNBGMWGW4pU._39a0Mt5b1i2joAqIaEHOWJ:before,._4Glnzr5LA7bNBGMWGW4pU:active:before{opacity:.24}._4Glnzr5LA7bNBGMWGW4pU:disabled,._4Glnzr5LA7bNBGMWGW4pU[data-disabled],._4Glnzr5LA7bNBGMWGW4pU[disabled]{cursor:not-allowed;filter:grayscale(1);background:none;color:var(--newCommunityTheme-buttonAlpha50);fill:var(--newCommunityTheme-buttonAlpha50)}._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0{position:relative;background-color:var(--newCommunityTheme-field);border:1px solid transparent;color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-button);opacity:0}._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0:hover:before{opacity:.08}._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0:focus{outline:none}._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0:focus:before{opacity:.16}._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0._39a0Mt5b1i2joAqIaEHOWJ:before,._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0:active:before{opacity:.24}._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0:disabled,._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0[data-disabled],._4Glnzr5LA7bNBGMWGW4pU._2nelDm85zKKmuD94NequP0[disabled]{cursor:not-allowed;filter:grayscale(1);background:none;color:var(--newRedditTheme-buttonAlpha50);fill:var(--newRedditTheme-buttonAlpha50)}._3zbhtNO0bdck0oYbYRhjMC{position:relative;border:1px solid transparent;color:var(--newCommunityTheme-button);fill:var(--newCommunityTheme-button)}._3zbhtNO0bdck0oYbYRhjMC:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-bodyText);opacity:0}._3zbhtNO0bdck0oYbYRhjMC:hover:before{opacity:.08}._3zbhtNO0bdck0oYbYRhjMC:focus{outline:none}._3zbhtNO0bdck0oYbYRhjMC:focus:before{opacity:.16}._3zbhtNO0bdck0oYbYRhjMC._39a0Mt5b1i2joAqIaEHOWJ:before,._3zbhtNO0bdck0oYbYRhjMC:active:before{opacity:.24}._3zbhtNO0bdck0oYbYRhjMC:disabled,._3zbhtNO0bdck0oYbYRhjMC[data-disabled],._3zbhtNO0bdck0oYbYRhjMC[disabled]{cursor:not-allowed;filter:grayscale(1);color:var(--newRedditTheme-metaText);fill:var(--newRedditTheme-metaText)}._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0{position:relative;border:1px solid transparent;color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-bodyText);opacity:0}._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0:hover:before{opacity:.08}._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0:focus{outline:none}._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0:focus:before{opacity:.16}._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0._39a0Mt5b1i2joAqIaEHOWJ:before,._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0:active:before{opacity:.24}._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0:disabled,._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0[data-disabled],._3zbhtNO0bdck0oYbYRhjMC._2nelDm85zKKmuD94NequP0[disabled]{cursor:not-allowed;filter:grayscale(1);color:var(--newRedditTheme-metaText);fill:var(--newRedditTheme-metaText)}._1tPpYVD73ugqp4k-VMFRki{padding:0}._1tPpYVD73ugqp4k-VMFRki._3ojSE1JW7jxNzUzZK8kt7m,._1tPpYVD73ugqp4k-VMFRki._3ojSE1JW7jxNzUzZK8kt7m:before{border-radius:4px}._1tPpYVD73ugqp4k-VMFRki ._1mvTX6krm3Q2d1CSyUm28s,._1tPpYVD73ugqp4k-VMFRki i.icon._1mvTX6krm3Q2d1CSyUm28s{padding:0}._2v8rCfSRT4mr5y4pwEhX41,._3kfXQpuyMJIMeWQCwjZKfw{border:1px solid transparent;border-radius:4px;box-sizing:border-box;text-align:center;letter-spacing:1px;text-decoration:none;font-size:12px;font-weight:700;letter-spacing:.5px;line-height:24px;text-transform:uppercase;padding:3px 16px}._13twe55MPRo1LqypxB-LJx{color:var(--newCommunityTheme-button);background:none}._13twe55MPRo1LqypxB-LJx,._13twe55MPRo1LqypxB-LJx:hover{fill:var(--newCommunityTheme-buttonTinted80)}._13twe55MPRo1LqypxB-LJx:hover{color:var(--newCommunityTheme-buttonTinted80)}._13twe55MPRo1LqypxB-LJx:active{color:var(--newCommunityTheme-button);fill:var(--newCommunityTheme-button)}._13twe55MPRo1LqypxB-LJx:disabled,._13twe55MPRo1LqypxB-LJx[data-disabled],._13twe55MPRo1LqypxB-LJx[disabled]{color:var(--newCommunityTheme-buttonAlpha50);fill:var(--newCommunityTheme-buttonAlpha50);cursor:not-allowed}._13twe55MPRo1LqypxB-LJx:disabled{background:none}._3kfXQpuyMJIMeWQCwjZKfw{position:relative;background-color:0;border:1px solid transparent;color:var(--newCommunityTheme-linkText);fill:var(--newCommunityTheme-linkText);background-color:transparent;padding-left:4px;padding-right:4px;text-decoration:underline;text-transform:none;width:auto}._3kfXQpuyMJIMeWQCwjZKfw:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-linkText);opacity:0}._3kfXQpuyMJIMeWQCwjZKfw:hover:before{opacity:.08}._3kfXQpuyMJIMeWQCwjZKfw:focus{outline:none}._3kfXQpuyMJIMeWQCwjZKfw:focus:before{opacity:.16}._3kfXQpuyMJIMeWQCwjZKfw._39a0Mt5b1i2joAqIaEHOWJ:before,._3kfXQpuyMJIMeWQCwjZKfw:active:before{opacity:.24}._3kfXQpuyMJIMeWQCwjZKfw:disabled,._3kfXQpuyMJIMeWQCwjZKfw[data-disabled],._3kfXQpuyMJIMeWQCwjZKfw[disabled]{cursor:not-allowed;filter:grayscale(1);background:none;color:var(--newCommunityTheme-linkTextAlpha50);fill:var(--newCommunityTheme-linkTextAlpha50)}._2UhHcZFBOYxMULbf2p-skl{color:var(--newCommunityTheme-linkText);background-color:unset;padding:0 12px}._2UhHcZFBOYxMULbf2p-skl:hover{color:var(--newCommunityTheme-linkTextShaded80)}._2UhHcZFBOYxMULbf2p-skl._2nelDm85zKKmuD94NequP0{color:var(--newRedditTheme-linkText)}._2UhHcZFBOYxMULbf2p-skl._2nelDm85zKKmuD94NequP0:hover{color:var(--newRedditTheme-linkTextShaded80)}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/Governance~ModListing~Reddit~ReportFlow.3f6a4b0a4bd41b00990b_.css.map*/</style><style data-href="chunkCSS/Chat~Governance~Reddit.4075ef68e55c88c9b008_.css" data-chunk="Reddit" key="chunkCSS/Chat~Governance~Reddit.4075ef68e55c88c9b008_.css">@font-face{font-family:IBMPlexSans;font-weight:400;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/IBMPlexSans/Regular-116bb6d508f5307861d3b1269bc597e7-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/IBMPlexSans/Regular-e6bbcdd30d3bd4d6b170bcb6d3552cab-font.woff) format("woff")}@font-face{font-family:IBMPlexSans;font-weight:500;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/IBMPlexSans/Medium-c4b185e25a4dde85a29f902cd5ce5360-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/IBMPlexSans/Medium-1051a531d3e1ee3483a6533158557139-font.woff) format("woff")}@font-face{font-family:IBMPlexSans;font-weight:700;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/IBMPlexSans/Bold-875de5047556e7c822519d95d7ee692d-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/IBMPlexSans/Bold-c34ba754b7235b49d33b294ff7a54179-font.woff) format("woff")}
@font-face{font-family:Noto Sans;font-weight:400;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/NotoSans/Regular-d6a6aa8dc0f93416a832ea04a18c6fb8-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/NotoSans/Regular-e6bbcdd30d3bd4d6b170bcb6d3552cab-font.woff) format("woff")}@font-face{font-family:Noto Sans;font-weight:400;font-style:italic;src:url(https://www.redditstatic.com/desktop2x/fonts/NotoSans/Italic-fca7c15cdda5570c8f739b9d71e9ed6d-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/NotoSans/Italic-5267af566ab853eb9d74db1a78a46c67-font.woff) format("woff")}@font-face{font-family:Noto Sans;font-weight:700;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/NotoSans/Bold-d4ba4ecba17e90993f442f7bb082a3a2-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/NotoSans/Bold-c34ba754b7235b49d33b294ff7a54179-font.woff) format("woff")}@font-face{font-family:Noto Sans;font-weight:700;font-style:italic;src:url(https://www.redditstatic.com/desktop2x/fonts/NotoSans/Bold-Italic-be39cd37f002d25d500c67b88871bed4-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/NotoSans/Bold-Italic-255b4934a1f414dd312aa89382d65114-font.woff) format("woff")}
._1VhYfuKTAdUU_3j4cMjkr5{display:none}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/Chat~Governance~Reddit.4075ef68e55c88c9b008_.css.map*/</style><style data-href="chunkCSS/Governance~ModListing~Reddit.f0e6814c2dd64ba3b618_.css" data-chunk="Reddit" key="chunkCSS/Governance~ModListing~Reddit.f0e6814c2dd64ba3b618_.css">.efdkOLo3oigH_95whTYCp,._2p14AQvJBvTrEEa4csiW9v{position:relative;height:100%}.efdkOLo3oigH_95whTYCp._1lxVpLf3223Gve3gRhbG-R,._2p14AQvJBvTrEEa4csiW9v._1lxVpLf3223Gve3gRhbG-R{height:100%}._3utuhrSAkEkzgaswqglvpN,._2TN8dEgAQbSyKntWpSPYM7{box-sizing:border-box;border:1px solid var(--newCommunityTheme-line);height:100%;object-fit:cover;object-position:center;width:100%}._3utuhrSAkEkzgaswqglvpN{background:#d7dfe2;fill:#fff}._3utuhrSAkEkzgaswqglvpN._2aVSEFJsIE0M-4uRE-U24H{background:var(--newRedditTheme-actionIcon)}._2TN8dEgAQbSyKntWpSPYM7{color:var(--newCommunityTheme-body);text-indent:-9999px}._3fhlcUDP9SJN47QMfuzW_j{position:absolute;top:57%;left:55%;width:180%;transform:translate(-50%,-50%)}._3ppYbU2ZS369JSNSb8585I{height:100%;width:100%;position:absolute;background:linear-gradient(146.27deg,#004e5f 36.02%,rgba(114,124,216,.81) 77.71%);-webkit-clip-path:polygon(0 30%,50% 0,90% 25%,90% 75%,50% 100%,5% 73%);clip-path:polygon(0 30%,50% 0,90% 25%,90% 75%,50% 100%,5% 73%)}._1AX7t-EP7R4ZoVC41DG-Jx{position:absolute;top:0;left:0}._1cyAeeYDGrx7MPL_jRwKZ{width:100%;height:100%;position:relative}._2_QqG5dG916znjlVV8ZCbw{background:var(--newRedditTheme-line);width:100%;height:100%;border-radius:50%}._3Bn5QwbgKslkdt4UwkP9r9 ._2_QqG5dG916znjlVV8ZCbw{background:none}._1XJXnCAngvZLEeLpB3oa4L{width:100%;position:absolute;bottom:0}.ScrrUjzznpAqm92uwgnvO{width:100%;transform-origin:bottom center;display:block;transform:scale(1.3);-webkit-clip-path:polygon(0 68.22%,12.12% 68.22%,12.85% 71.49%,13.86% 74.69%,15.14% 77.79%,16.69% 80.77%,18.49% 83.6%,20.54% 86.26%,22.8% 88.73%,25.28% 91%,27.94% 93.04%,30.77% 94.85%,33.75% 96.4%,36.85% 97.68%,40.05% 98.69%,43.32% 99.42%,46.65% 99.85%,50% 100%,53.35% 99.85%,56.68% 99.42%,59.95% 98.69%,63.15% 97.68%,66.25% 96.4%,69.23% 94.85%,72.06% 93.04%,74.72% 91%,77.2% 88.73%,79.46% 86.26%,81.51% 83.6%,83.31% 80.77%,84.86% 77.79%,86.14% 74.69%,87.15% 71.49%,87.88% 68.22%,100% 68.22%,100% 0,0 0);clip-path:polygon(0 68.22%,12.12% 68.22%,12.85% 71.49%,13.86% 74.69%,15.14% 77.79%,16.69% 80.77%,18.49% 83.6%,20.54% 86.26%,22.8% 88.73%,25.28% 91%,27.94% 93.04%,30.77% 94.85%,33.75% 96.4%,36.85% 97.68%,40.05% 98.69%,43.32% 99.42%,46.65% 99.85%,50% 100%,53.35% 99.85%,56.68% 99.42%,59.95% 98.69%,63.15% 97.68%,66.25% 96.4%,69.23% 94.85%,72.06% 93.04%,74.72% 91%,77.2% 88.73%,79.46% 86.26%,81.51% 83.6%,83.31% 80.77%,84.86% 77.79%,86.14% 74.69%,87.15% 71.49%,87.88% 68.22%,100% 68.22%,100% 0,0 0)}._3Bn5QwbgKslkdt4UwkP9r9 .ScrrUjzznpAqm92uwgnvO{-webkit-clip-path:polygon(0 0,100% 2%,100% 50%,100% 70%,47% 96%,6% 75%);clip-path:polygon(0 0,100% 2%,100% 50%,100% 70%,47% 96%,6% 75%)}._2dn5Ncenn0BSD4tCSmxQhA{height:50%;left:59%;position:absolute;top:59%;width:50%}._2dn5Ncenn0BSD4tCSmxQhA.GpWjjkZl5_kV4yZYWBaT2{fill:#46d160}._1TENjLYSaj4L4uJMZa3DRe{height:100%;position:relative}
._1g3Xfh9mljLHWv24M9A3Rw{fill:var(--newCommunityTheme-actionIcon)}._3SlBAJb2MbUHwgBZFH8eL7{fill:var(--newCommunityTheme-body)}._3SlBAJb2MbUHwgBZFH8eL7._1-JQy00VxG8hpTxxdxV32y{fill:var(--newCommunityTheme-activeAlpha10)}
._eYtD2XCVieq6emjKBH3m{display:inline}
._34CfAAowTqdbNDYXz5tBTW,._3-8BEp7zk8HU_Tq2SjmosX{border-radius:100%;vertical-align:middle}._34CfAAowTqdbNDYXz5tBTW._2P3jpibqK9Q2k2UJYzBNIy{filter:blur(6px)}._2WM2ef3imxyCFqHx0Nx5M4{border-radius:100%;vertical-align:middle;background:var(--newCommunityTheme-active);border:1px solid var(--newCommunityTheme-lightText);box-sizing:border-box;color:var(--newCommunityTheme-lightText);padding:3px;fill:var(--newCommunityTheme-lightText)}.RK004G8fbNOkGdNLEzm67{border-radius:100%;vertical-align:middle;background-size:20px 20px;display:inline-block}._7nyhK_sDI_8i22XNdcMzb{position:relative}._1AxWRIyg1lV9-r_CmqYj0o{vertical-align:middle;background:var(--newCommunityTheme-active);color:var(--newCommunityTheme-lightText);fill:var(--newCommunityTheme-lightText);border:none;height:32px;width:32px;cursor:pointer;background:var(--newCommunityTheme-field);margin-right:8px;border-radius:100%;box-sizing:border-box;padding:0;-ms-flex:none;flex:none}.-Mpi2pdgifDBOdpUYX2vh{display:-ms-inline-flexbox;display:inline-flex;-ms-flex-direction:column;flex-direction:column}._3H6u2CWhsluIPVF14GpEaA{font-size:12px;font-weight:700;line-height:16px;color:var(--newCommunityTheme-button);cursor:pointer;text-align:center;margin-top:4px}._1UpdjN7u66BU606z97t4HS{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center}._1UpdjN7u66BU606z97t4HS .ndkYE2hc8Y-V3NHpSYvxA{fill:var(--newCommunityTheme-banner-backgroundColor);height:44px;width:44px}._1iA7YdCRjbU9Rd_2VNGvsw{transition:all .1s linear 0s}._1AxWRIyg1lV9-r_CmqYj0o._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2{border:1px dashed var(--newCommunityTheme-active);transition:all .1s linear 0s;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center}._1AxWRIyg1lV9-r_CmqYj0o._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2>*{transition:all .1s linear 0s}._1AxWRIyg1lV9-r_CmqYj0o._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2 .Dh1qxsy_tIctL9f4LEzv9{fill:var(--newCommunityTheme-active);height:24px;width:24px}._1AxWRIyg1lV9-r_CmqYj0o._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2:hover{border:1px solid var(--newCommunityTheme-active)}._1AxWRIyg1lV9-r_CmqYj0o._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2:hover .Dh1qxsy_tIctL9f4LEzv9{height:32px;width:32px}.JBITiVY1zX1mMDq-sHkru.JBITiVY1zX1mMDq-sHkru.JBITiVY1zX1mMDq-sHkru{display:none}._3Dk8QRKhQImYqds2lSF6G4{--sizePx:10px}._3Dk8QRKhQImYqds2lSF6G4._3Dk8QRKhQImYqds2lSF6G4._3Dk8QRKhQImYqds2lSF6G4{border-left-color:var(--newCommunityTheme-active);position:absolute;left:calc(50% - var(--sizePx));top:calc(50% - var(--sizePx));margin-left:3px;margin-top:7px}._3Dk8QRKhQImYqds2lSF6G4._3Dk8QRKhQImYqds2lSF6G4._3Dk8QRKhQImYqds2lSF6G4._1U3KLnHX2TdXL5lNrrv4EW{margin-left:12px;margin-top:-5px}._7nyhK_sDI_8i22XNdcMzb._1h9JeZaSDxkh67Ns3QVUP2 ._3Dk8QRKhQImYqds2lSF6G4._3Dk8QRKhQImYqds2lSF6G4._3Dk8QRKhQImYqds2lSF6G4{margin-left:7px}._7nyhK_sDI_8i22XNdcMzb._1UpdjN7u66BU606z97t4HS._3-i_fdY8zqHIo3CjuVzTYE ._3Dk8QRKhQImYqds2lSF6G4._1U3KLnHX2TdXL5lNrrv4EW{margin-left:12px;margin-top:12px}.icon._1xvdfUtOPDANqHjxzxKX5b{border-radius:9999px;color:#0079d3}.icon._1xvdfUtOPDANqHjxzxKX5b._1TI6C7sqGL9TRdsq1jRks{color:#fff}.icon._1xvdfUtOPDANqHjxzxKX5b._2P3jpibqK9Q2k2UJYzBNIy{filter:blur(6px)}._1UpdjN7u66BU606z97t4HS .icon.ndkYE2hc8Y-V3NHpSYvxA{color:var(--newCommunityTheme-banner-backgroundColor);height:44px;width:44px;font-size:44px;line-height:44px}._1AxWRIyg1lV9-r_CmqYj0o._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2._1h9JeZaSDxkh67Ns3QVUP2 .icon.Dh1qxsy_tIctL9f4LEzv9{color:var(--newCommunityTheme-banner-backgroundColor);height:24px;width:24px;font-size:24px;line-height:24px}._35ahToY-XcU6llULyYdy2A{display:contents}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/Governance~ModListing~Reddit.f0e6814c2dd64ba3b618_.css.map*/</style><style data-href="chunkCSS/ModListing~Reddit~StandalonePostPage.9cc9a122bf677a5c6071_.css" data-chunk="Reddit" key="chunkCSS/ModListing~Reddit~StandalonePostPage.9cc9a122bf677a5c6071_.css">._39Glgtoolpdt4PIzcnjPSW{text-decoration:none;fill:currentColor;color:inherit}
._10K5i7NW6qcm-UoCtpB3aK{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;text-align:left;width:100%}
.pthKOcceozMuXLYrLlbL1{margin-right:6px}._2-cXnP74241WI7fpcpfPmg{display:inline-block}._3LwUIE7yX7CZQKmD2L87vf{font-size:14px;font-weight:500;line-height:18px;display:block;padding:8px;text-transform:capitalize;white-space:nowrap;color:var(--newRedditTheme-actionIcon);fill:var(--newRedditTheme-actionIcon)}._3LwUIE7yX7CZQKmD2L87vf.kR_ljR-F8vtc-ORj1uipB{color:var(--newCommunityTheme-bodyText)}._3LwUIE7yX7CZQKmD2L87vf ._3Iua3qlR9JiTwjjk6NKye1{height:16px;width:16px;fill:var(--newCommunityTheme-button);margin-left:auto}._3LwUIE7yX7CZQKmD2L87vf.ui39KJ4PwbdKkxvIBbLbV{text-transform:none}._3LwUIE7yX7CZQKmD2L87vf:not(:first-child){border-top:1px solid var(--newRedditTheme-line);border-bottom:none}._3LwUIE7yX7CZQKmD2L87vf:not(:first-child).kR_ljR-F8vtc-ORj1uipB{border-top:none}._3LwUIE7yX7CZQKmD2L87vf:not(:first-child).sK8_uuNiAqPNlw-HoD2HG{border:1px solid var(--newRedditTheme-actionIconAlpha20)}._3LwUIE7yX7CZQKmD2L87vf._1IKtbRloF_LV1hPqMzP3MC{color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}._3LwUIE7yX7CZQKmD2L87vf._1IKtbRloF_LV1hPqMzP3MC.kR_ljR-F8vtc-ORj1uipB{color:var(--newCommunityTheme-button);fill:var(--newCommunityTheme-button);display:-ms-flexbox;display:flex}._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:active,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:focus,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:hover{color:var(--newRedditTheme-bodyText);fill:var(--newRedditTheme-bodyText);background-color:var(--newRedditTheme-highlight);outline:none}._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:active ._3Iua3qlR9JiTwjjk6NKye1,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:focus ._3Iua3qlR9JiTwjjk6NKye1,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:hover ._3Iua3qlR9JiTwjjk6NKye1{fill:var(--newCommunityTheme-body)}._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:active._1IKtbRloF_LV1hPqMzP3MC,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:focus._1IKtbRloF_LV1hPqMzP3MC,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:hover._1IKtbRloF_LV1hPqMzP3MC{color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:active._1IKtbRloF_LV1hPqMzP3MC.kR_ljR-F8vtc-ORj1uipB,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:focus._1IKtbRloF_LV1hPqMzP3MC.kR_ljR-F8vtc-ORj1uipB,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:hover._1IKtbRloF_LV1hPqMzP3MC.kR_ljR-F8vtc-ORj1uipB{color:var(--newCommunityTheme-body);fill:var(--newCommunityTheme-body);display:-ms-flexbox;display:flex}._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:active.kR_ljR-F8vtc-ORj1uipB,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:focus.kR_ljR-F8vtc-ORj1uipB,._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:hover.kR_ljR-F8vtc-ORj1uipB{color:var(--newCommunityTheme-body);fill:var(--newCommunityTheme-body);background-color:var(--newCommunityTheme-button);outline:none}._3LwUIE7yX7CZQKmD2L87vf._1oYEKCssGFjqxQ9jJMNj5G:disabled{color:var(--newRedditTheme-actionIcon);fill:var(--newRedditTheme-actionIcon);background-color:var(--newCommunityTheme-body);outline:none;cursor:not-allowed;opacity:.3}
._1DK52RbaamLOWw5UPaht_S{-ms-flex-align:center;align-items:center;box-sizing:border-box;display:-ms-flexbox;display:flex;height:100%;overflow:auto;padding:75px 30px 20px;pointer-events:none;position:fixed;top:0;width:100%;z-index:55}._1DK52RbaamLOWw5UPaht_S._1acwN_tUhJ8w-n7oCp-Aw3{background-color:rgba(28,28,28,.9);pointer-events:unset}._1DK52RbaamLOWw5UPaht_S._1acwN_tUhJ8w-n7oCp-Aw3._3Tq-_9917Q-o0iyzcNAeZn{background:rgba(0,0,0,.4)}._2Bejocqb-InO8686E2ehf{background-color:var(--newCommunityTheme-body);border:1px solid var(--newCommunityTheme-line);border-radius:4px;box-shadow:0 2px 20px 0 rgba(0,0,0,.3);margin:auto;pointer-events:auto;z-index:55}._2Bejocqb-InO8686E2ehf:focus{outline:none}
._2GCoZTwJW7199HSwNZwlHk{position:relative}.jR747Vd1NbfaLusf5bHre{display:inline-block;overflow:hidden;width:16px;height:18px;line-height:16px;font-size:16px}.icon.ZyxIIl4FP5gHGrJDzNpUC{line-height:24px;position:relative}._1iKd82bq_nqObFvSH1iC_Q{display:inline-block;overflow:hidden;height:24px;width:24px;font-size:16px;line-height:24px}
._3eoXtlBWKbkFYoOHUIcIgK{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:21px;border:none;color:var(--newCommunityTheme-actionIcon);display:block;height:36px;padding:0 8px;outline:none}
.Q0BxYHtCOJ_rNSPJMU2Y7{color:var(--newCommunityTheme-actionIcon)}.Q0BxYHtCOJ_rNSPJMU2Y7._2fe-KdD2OM0ciaiux-G1EL{border-radius:2px;cursor:pointer}.Q0BxYHtCOJ_rNSPJMU2Y7._2fe-KdD2OM0ciaiux-G1EL:focus,.Q0BxYHtCOJ_rNSPJMU2Y7._2fe-KdD2OM0ciaiux-G1EL:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}.Q0BxYHtCOJ_rNSPJMU2Y7._2fe-KdD2OM0ciaiux-G1EL:active{color:var(--newCommunityTheme-voteText-downvoteTinted80)}.Q0BxYHtCOJ_rNSPJMU2Y7._3emIxnIscWEPB7o5LgU_rn{color:var(--newCommunityTheme-voteText-downvote)!important}.Q0BxYHtCOJ_rNSPJMU2Y7._3yQIOwaIuF6gn8db96Gu7y:hover{color:var(--newCommunityTheme-voteText-downvoteShaded80)}
._3XSQHPxjCTSWWZh_u-d0Xf{height:16px;width:16px;fill:var(--newCommunityTheme-actionIcon)}._2R3RlhymCOkPrz9TusvcPq{box-shadow:0 2 15px rgba(0,0,0,.3);max-width:538px;min-width:410px}.HydQQ-TD4TUsVnxkYk_5F{border:1px solid var(--newRedditTheme-line);background-color:var(--newRedditTheme-field);padding:12px 16px;border-radius:4px 4px 0 0;border-bottom:0}.mFTHPdbEAklUs8yhT4Xm7{font-size:14px;line-height:21px;display:block}._3cwQrg-XvocnoG0U22wT8t,.mFTHPdbEAklUs8yhT4Xm7{font-family:Noto Sans,Arial,sans-serif;font-weight:400;color:var(--newCommunityTheme-bodyText)}._3cwQrg-XvocnoG0U22wT8t{font-size:12px;line-height:18px;margin-bottom:8px}._12g_PUGHD-w7T1w4Q3oTsq{color:var(--newCommunityTheme-actionIcon)}._12g_PUGHD-w7T1w4Q3oTsq,._27eskYssCs-urVW1uHI4YI{font-size:12px;font-weight:400;line-height:16px}._27eskYssCs-urVW1uHI4YI{color:var(--newCommunityTheme-metaText)}._3xiY8nTCVp16qSb6CGW2Kv{display:block;margin-bottom:16px}._20ZSV7ktyDYzPcd1UMQWZT{background-color:var(--newCommunityTheme-body);box-sizing:border-box;color:var(--newCommunityTheme-bodyText);border:1px solid var(--newCommunityTheme-line);border-radius:4px;padding:12px;width:100%}._20ZSV7ktyDYzPcd1UMQWZT:focus{border-color:var(--newCommunityTheme-active)}._20ZSV7ktyDYzPcd1UMQWZT::placeholder{color:var(--newCommunityTheme-placeholder)}.HVADn-LHFLaS8r6IBJWeq{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;color:var(--newRedditTheme-actionIcon);display:block;margin-bottom:8px}._-0i7atRJ5NBsrRM5wuPpX{background-color:var(--newCommunityTheme-line);border-top:1px solid var(--newCommunityTheme-line);display:-ms-flexbox;display:flex;-ms-flex-pack:end;justify-content:flex-end;padding:16px;border-bottom-right-radius:4px;border-bottom-left-radius:4px}._1Fa5Xv7f16v5IC2Tq1m2Fy{border-bottom:1px solid var(--newCommunityTheme-line);border-top-right-radius:4px;border-top-left-radius:4px;padding:16px}._1Fa5Xv7f16v5IC2Tq1m2Fy svg{display:block}.eLnlHLGCDxjFf3jfGTcZu{font-size:16px;font-weight:500;line-height:20px}._1uaasV6RaxBfRyVgQJdiKs,.eLnlHLGCDxjFf3jfGTcZu{color:var(--newCommunityTheme-bodyText)}._1uaasV6RaxBfRyVgQJdiKs{padding:16px}.gLlWG7Oj89Ost4_twUu8w{font-size:12px;font-weight:400;line-height:16px;color:var(--newCommunityTheme-actionIcon)}.gLlWG7Oj89Ost4_twUu8w a{color:var(--newCommunityTheme-linkText)}.gLlWG7Oj89Ost4_twUu8w strong{font-weight:500}._2h8O7PjrCXfaJJWKrAxJPL{background-color:var(--newCommunityTheme-body);border:1px solid var(--newCommunityTheme-line);border-radius:4px;box-sizing:border-box;color:var(--newCommunityTheme-bodyText);display:block;height:78px;padding:9px 10px;width:100%}._2h8O7PjrCXfaJJWKrAxJPL:focus{outline:none;border:1px solid var(--newCommunityTheme-button)}._2h8O7PjrCXfaJJWKrAxJPL::placeholder{color:var(--newCommunityTheme-actionIcon)}._17UyTSs2atqnKg9dIq5ERg{background-color:#ea0027;border-color:#ea0027;margin-left:8px}._17UyTSs2atqnKg9dIq5ERg:disabled,._17UyTSs2atqnKg9dIq5ERg:hover,._17UyTSs2atqnKg9dIq5ERg[data-disabled],._17UyTSs2atqnKg9dIq5ERg[disabled]{background-color:rgba(234,0,39,.8);border-color:rgba(234,0,39,.8);color:#fff}._2X1FFYUx3jzlnbcegBC_Sr{margin-left:8px}._1QUX9-zZuGtifS6jJBUyh-{border-color:var(--newCommunityTheme-actionIcon);color:var(--newCommunityTheme-actionIcon)}._1QUX9-zZuGtifS6jJBUyh-:hover{border-color:rgba(135,138,140,.8);color:rgba(135,138,140,.8)}._2ulRgczjI5SWCMgSA1CNLj{color:#ea0027}._2ulRgczjI5SWCMgSA1CNLj:hover{color:rgba(234,0,39,.8)}.JZC61-VzVuaiHdWuRUiSC{background-color:#ff4500;border-color:#ff4500;margin-left:8px;color:var(--newRedditTheme-lightText)}.JZC61-VzVuaiHdWuRUiSC:hover{background-color:rgba(255,69,0,.8);border-color:rgba(255,69,0,.8)}.JZC61-VzVuaiHdWuRUiSC:disabled{color:var(--newRedditTheme-lightText);background-color:#ff4500;border-color:#ff4500;filter:none;opacity:.3}.JZC61-VzVuaiHdWuRUiSC:disabled:hover:before{opacity:0}
._39UOLMgvssWenwbRxz_iEn{position:relative}._3wVayy5JvIMI67DheMYra2{display:inline-block;overflow:hidden;width:16px;height:16px;line-height:16px;font-size:16px}.icon._2Jxk822qXs4DaXwsN7yyHA{line-height:24px;position:relative}._2q7IQ0BUOWeEZoeAxN555e{display:inline-block;overflow:hidden;height:24px;width:24px;font-size:16px;line-height:24px}
.qYzY57HWQ8W424hj3s10-{font-size:12px;font-weight:700;letter-spacing:.5px;line-height:24px;text-transform:uppercase;background:transparent;border:none;padding:0;text-decoration:underline}
._3SUsITjKNQ7Tp0Wi2jGxIM{color:var(--newCommunityTheme-actionIcon)}._3SUsITjKNQ7Tp0Wi2jGxIM.qW0l8Af61EP35WIG6vnGk{border-radius:2px;cursor:pointer}._3SUsITjKNQ7Tp0Wi2jGxIM.qW0l8Af61EP35WIG6vnGk:focus,._3SUsITjKNQ7Tp0Wi2jGxIM.qW0l8Af61EP35WIG6vnGk:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}._3SUsITjKNQ7Tp0Wi2jGxIM.qW0l8Af61EP35WIG6vnGk:active{color:var(--newCommunityTheme-voteText-upvoteTinted80)}._3SUsITjKNQ7Tp0Wi2jGxIM.Z3lT0VGlALek4Q9j0ZQCr{color:var(--newCommunityTheme-voteText-upvote)!important}._3SUsITjKNQ7Tp0Wi2jGxIM._3edNsMs0PNfyQYofMNVhsG:hover{color:var(--newCommunityTheme-voteText-upvoteShaded80)}
._5gAwSCo7K8G413IoE78Ml{color:var(--newCommunityTheme-bodyText);-ms-flex:1 1 100%;flex:1 1 100%;width:100%}._2ghjBMFIsORwdO3oh2Kq6g{-ms-flex:0 0;flex:0 0}._1zTJo0Ndih4fp__5DjbClN{display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row}
.ceU_3ot04pOVIcrrXH9fY{--verticalvotes-customdownvote-active:"";--verticalvotes-customdownvote-inactive:"";background-position:50%;background-repeat:no-repeat;background-size:contain;cursor:pointer;height:24px;outline:none;width:24px;background-image:var(--verticalvotes-customdownvote-inactive)}.ceU_3ot04pOVIcrrXH9fY._3sO1xEnOT_9CQBjRzczQjS{height:20px;width:20px}.ceU_3ot04pOVIcrrXH9fY._8dpZTfzgKPKCUTjp9SAn1{background-image:var(--verticalvotes-customdownvote-active)}._2k73nZrjAYiwAj9hv7K-kq{--verticalvotes-customupvote-active:"";--verticalvotes-customupvote-inactive:"";background-position:50%;background-repeat:no-repeat;background-size:contain;cursor:pointer;height:24px;outline:none;width:24px;background-image:var(--verticalvotes-customupvote-inactive)}._2k73nZrjAYiwAj9hv7K-kq._3sO1xEnOT_9CQBjRzczQjS{height:20px;width:20px}._2k73nZrjAYiwAj9hv7K-kq._8dpZTfzgKPKCUTjp9SAn1{background-image:var(--verticalvotes-customupvote-active)}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/ModListing~Reddit~StandalonePostPage.9cc9a122bf677a5c6071_.css.map*/</style><style data-href="chunkCSS/Governance~Reddit.af725272a97a52ae2008_.css" data-chunk="Reddit" key="chunkCSS/Governance~Reddit.af725272a97a52ae2008_.css">@font-face{font-family:Noto Mono;font-weight:400;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/NotoMono/Regular-b16bb0524a7e7ee597970333c0c67180-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/NotoMono/Regular-e6bbcdd30d3bd4d6b170bcb6d3552cab-font.woff) format("woff")}@font-face{font-family:Noto Mono;font-weight:400;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/NotoMono/el-Regular-29d72243d2cd6145b28bcb80dc33f0e4-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/NotoMono/el-Regular-06ee3f893717454d11a16c3e8d0aa9f9-font.woff) format("woff");unicode-range:U+0370-03ff,U+1f??}
._34xisDRo0OvDRw0vh1tu5F{color:var(--newCommunityTheme-active)}._2NHlJ2WAZ0u5ebeJE3NHhI{background-color:var(--newRedditTheme-field)}.UQphgTZz-YLqJ1AJuwqmi{background-color:var(--newRedditTheme-body)}._1l5ReXTNeGQXHe-jzoS0sd{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:18px}._2JmouYbCEI5jhxWIp44V_6{color:var(--newRedditTheme-bodyText)}._2TJNEv970Kn5chU69vgAB4{border-bottom:1px solid var(--newCommunityTheme-line)}._2TJNEv970Kn5chU69vgAB4:last-of-type{border-bottom:none}._4y0ErgWHnHg-LqPeQoYKE{border-top:1px solid var(--newCommunityTheme-line)}._3R_dvs6bfcA-tygC7FL7kx{border-top:2px solid var(--newCommunityTheme-line)}._19DndzbKSqGxpzJ7gycTJL{-ms-flex-item-align:center;-ms-grid-row-align:center;align-self:center;fill:var(--newRedditTheme-linkText);padding-left:4px;pointer-events:none;width:12px}.SGuQkxXoYRPmcIRKtJnQ{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column}._1HnfZtTmYelxTj6QL6aaXS{background-color:var(--newCommunityTheme-body);border-top-width:1px;border:1px solid var(--newCommunityTheme-line);border-top:0 solid var(--newCommunityTheme-line);padding:0}._37mWd5gyv2BM4g00nmlZuD{padding:12px 16px}._1U-nknzRP43RdLab5D4_lK{position:fixed}._3AhxoqURjuFZmaySn4D12W{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex}._2nLtz9ffUxNdVSXrwhsrDg{-ms-flex-positive:1;flex-grow:1}._1jD48cwTYTTvOjusPtaja_{-ms-flex-wrap:wrap;flex-wrap:wrap}._3LzqitwwvqMy0VShIuQwvX{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase}._20OHBqoDD71_8fv7tuG6u6{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;padding:12px 16px}._20OHBqoDD71_8fv7tuG6u6:hover{background-color:var(--newCommunityTheme-field);border-color:var(--newCommunityTheme-line)}._20OHBqoDD71_8fv7tuG6u6._4V8jUxy7iuElvae9SRoVI{width:100%;text-align:start}._1jKZytiaP074XAKQIdEzzq{font-size:12px;font-weight:500;line-height:16px;color:var(--newRedditTheme-linkText);display:-ms-flexbox;display:flex}._3wwag2ZgVLfNKLCuEuXF7h{background-color:var(--newRedditTheme-line);height:20px;margin:12px 16px;max-width:calc(100% - 24px);width:auto}.F6UjYfPpQi9ycdulmJnnf{margin-bottom:8px}._3vubwQI518j2qoj8dYdhwW{margin-left:4px}._1QVrieUoti9cxiQSRw314E{margin-left:8px}._3iXUDNuLPuwiYhJfqGPJEg{margin-top:8px}._33A2uwwTbNBE44RwzNWbk6{width:4px;margin-right:4px;margin-left:4px}._3C9CntSKG4Z9k6ul3_ugNH{color:var(--newCommunityTheme-metaText)}._3X3sIziqqmPSvYCMJmkipO{font-size:12px;font-weight:400;line-height:16px}._2JD4mokfQk2Qnin9rHTe6Y{border-top:2px solid var(--newCommunityTheme-line);padding-bottom:8px}._1wYvb87VusZUTcm5C6KC6U{font-size:14px;font-weight:500;line-height:18px;padding:12px 16px}._1f4QVsU6jdEkvigYTcqIG7{border-top:2px solid var(--newCommunityTheme-line);display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;padding:12px 16px;width:100%}._1f4QVsU6jdEkvigYTcqIG7:hover{background-color:var(--newRedditTheme-field);border-color:var(--newRedditTheme-line)}._39RbKXGDidws2W3278Lj1A{padding-top:4px}.YeMwUP22Up8CVxmgTayyQ{color:var(--newRedditTheme-metaText);margin-bottom:8px;margin-top:8px;overflow:hidden;text-overflow:ellipsis}._3MnH55IylwBZcJD46S4KFO{border-top-width:0;border-radius:0 0 4px 4px;box-sizing:border-box;left:-1px;margin-top:-1px;max-height:482px;overflow-x:hidden;overflow-y:scroll;position:absolute;right:0;top:100%;width:270px}._1H3lgd1i4NTn9aM5VR9BQX{-ms-flex-pack:justify;justify-content:space-between}.sb9GBNKICO504iABZENf3{font-size:14px;font-weight:500;line-height:18px}._2NH7qxA8P_UowZKF4-LUNe{padding-bottom:8px;padding-top:16px}.uSWMIsxB2_3C40ulyecE-{margin-left:24px}._4V8jUxy7iuElvae9SRoVI:hover{background-color:var(--newRedditTheme-field);border-color:var(--newRedditTheme-line)}._3tgXQ-cvqUY_NlKDJgdSdy{padding-bottom:8px;padding-top:12px}._2LJ9gkn2k4DlHhF8C1QhF6{padding-top:8px}._2Tfe4NhLJlRQkuO1yhzqR2,._3uBNO7SvsRGN4W794WAO_p,._26nS8Ogzm0pqOjlwfGRgJR,.icon.nltZBKTbnoPZEcEaIufmh,.icon._36TN0XrEYqhIZ5kQ0uHWhu,.icon._2VyZLE_5g-CDpUucbfHyOg{border-radius:9999px;box-sizing:border-box;display:inline-block;-ms-flex:none;flex:none;margin-bottom:-2px;vertical-align:middle}._3uBNO7SvsRGN4W794WAO_p{background-position:50%;background-repeat:no-repeat;background-size:100%;height:24px;width:24px}._2Tfe4NhLJlRQkuO1yhzqR2{background:var(--newRedditTheme-active);fill:var(--newRedditTheme-lightText);padding:3px}.icon._2VyZLE_5g-CDpUucbfHyOg{color:#0079d3}.icon.nltZBKTbnoPZEcEaIufmh{background:none;color:#0079d3;border-radius:100px;font-size:24px;height:24px;line-height:24px;width:24px}.icon.nltZBKTbnoPZEcEaIufmh.TiWmxUzfBQADxToVGHQeM{color:#fff;background:#0079d3}.icon._36TN0XrEYqhIZ5kQ0uHWhu{height:24px;width:24px}.icon._20HzJOjpEAN2C311EILlL9{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;height:24px;-ms-flex-pack:center;justify-content:center;width:24px}.icon._33A2uwwTbNBE44RwzNWbk6{width:4px;margin-right:4px;margin-left:4px}
._2c-0jMA2BuDIlKjWFiOUOt{margin-right:-8px;margin-bottom:8px}._2c-0jMA2BuDIlKjWFiOUOt._17HI1sHAGvXEekFXNNcehn{margin-bottom:-8px;margin-top:4px}.nL7Q54U2LLg9rkVdSxxLe{display:block;background-color:var(--newCommunityTheme-bodyTextAlpha03)}._1Y6dfr4zLlrygH-FLmr8x-{-ms-flex:1 1 100%;flex:1 1 100%;position:relative;word-break:break-word}@media (min-width:640px){._1Y6dfr4zLlrygH-FLmr8x-{margin-left:8px}}._1Y6dfr4zLlrygH-FLmr8x-.W-Z7cDkcZIo1dPic9COiN{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;min-height:112px}._1Y6dfr4zLlrygH-FLmr8x-.W-Z7cDkcZIo1dPic9COiN ._36kpXQ-z7Hr61j8878uRkP{margin-top:auto}._2I70Qhfz-GbGzP54PWXR3P._2I70Qhfz-GbGzP54PWXR3P{padding-left:120px}._1qc1-Anfrhr6APGcBKFk8M{margin-bottom:8px}._3r40yytzBnldjGGOrs2mCw{width:auto}.ssgs3QQidkqeycI33hlBa{-ms-flex-positive:1;flex-grow:1;height:100%}._36kpXQ-z7Hr61j8878uRkP{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;height:36px;margin-top:8px}@media (max-width:639px){._1wDt70OnYnqsrm0XIsNn8v{display:none}}._3ytybPoFoY12sGn375PMy1{max-height:24px}@media (min-width:640px){._3ytybPoFoY12sGn375PMy1{display:none!important}}a._35zWJjb5RJMIMkexZ2Prus,button._35zWJjb5RJMIMkexZ2Prus{-ms-flex:0 0 36px;flex:0 0 36px}@media (max-width:639px){a._35zWJjb5RJMIMkexZ2Prus,button._35zWJjb5RJMIMkexZ2Prus{display:none}}._2XDITKxlj4y3M99thqyCsO{display:-ms-flexbox;display:flex;position:relative;-ms-flex-direction:row;flex-direction:row;padding:8px 8px 0}@media (max-width:639px){._2XDITKxlj4y3M99thqyCsO{-ms-flex-direction:row-reverse;flex-direction:row-reverse}}a._2Ddj1d6vOe9NlJqkdothNe,button._2Ddj1d6vOe9NlJqkdothNe{position:absolute;bottom:4px;right:8px}@media (min-width:640px){a._2Ddj1d6vOe9NlJqkdothNe,button._2Ddj1d6vOe9NlJqkdothNe{display:none}}.iRkLLvxarfGu_2c7HxhW0{padding-bottom:8px}._2FcpdQwjwRwk7X_NiZub8x{margin-right:8px}._2e9Lv1I3dOmICVO9fg3uTG._2e9Lv1I3dOmICVO9fg3uTG{transition:filter .5s;height:72px;width:96px;border:none;border-radius:4px}._38EcSQ9jzVrdtzkXO1cydX{display:none;border-radius:4px;display:block}@media (min-width:320px){._38EcSQ9jzVrdtzkXO1cydX{display:-ms-flexbox;display:flex;-ms-flex:0 0 96px;flex:0 0 96px;height:72px}}@media (min-width:375px){._38EcSQ9jzVrdtzkXO1cydX{display:-ms-flexbox;display:flex;-ms-flex:0 0 96px;flex:0 0 96px;height:72px}}@media (min-width:414px){._38EcSQ9jzVrdtzkXO1cydX{display:-ms-flexbox;display:flex;-ms-flex:0 0 96px;flex:0 0 96px;height:72px}}@media (min-width:436px){._38EcSQ9jzVrdtzkXO1cydX{display:-ms-flexbox;display:flex;-ms-flex:0 0 96px;flex:0 0 96px;height:72px}}@media (max-width:639px){._38EcSQ9jzVrdtzkXO1cydX{display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;-ms-flex-align:end;align-items:flex-end;-ms-flex-direction:column;flex-direction:column;min-height:80px}}.rmPDRyja27ULjwD3rW14H.rmPDRyja27ULjwD3rW14H{margin-bottom:0}.D3IyhBGwXo9jPwz-Ka0Ve{cursor:pointer}[data-scroller-first] .D3IyhBGwXo9jPwz-Ka0Ve{border-radius:4px 4px 0 0}._3FOlcZoWAvyAWZYSVd8-WD._3FOlcZoWAvyAWZYSVd8-WD{overflow:visible}._2g8Jz2obQVOELSfntlgVsJ{border-radius:5px}._1LAkIKOirJP5Hor0NamqyY{-ms-flex-wrap:wrap-reverse;flex-wrap:wrap-reverse;padding-bottom:24px}@media (max-width:639px){._1LAkIKOirJP5Hor0NamqyY{-ms-flex-direction:row;flex-direction:row}}._1LAkIKOirJP5Hor0NamqyY hr{border:none;width:100%;margin:0}
._3yYOHq_rWQcgaR_pinEQU7{font-size:12px;line-height:20px}._1poH87fXNrjNu84jKXBtun{margin-left:4px}
.icon.qgDkGQIoFEpMMeNtfI0BY{font-size:12px;padding-left:4px}.FKej75-i0z1XubMqeVh9Q{display:inline-block;margin-right:8px}.SQnoC3ObvgnGjWt90zD9Z{color:inherit}a:visited ._2SdHzo12ISmrC8H86TgSCp{color:var(--postTitleLink-VisitedLinkColor)}.y8HYJ-y_lTUHkQIc1mdCq{display:inline;position:relative;text-decoration:none;word-break:break-word}.y8HYJ-y_lTUHkQIc1mdCq._2_QBmCTk6VD4M3dvKqXD23{display:-ms-flexbox;display:flex;min-width:0}.y8HYJ-y_lTUHkQIc1mdCq._2INHSNB8V5eaWp4P0rY_mE:visited ._2SdHzo12ISmrC8H86TgSCp{color:var(--postTitle-VisitedLinkColor)}._1hLrLjnE1G_RBCNcN9MVQf{visibility:hidden;position:absolute;left:-99999px;top:0}._2SdHzo12ISmrC8H86TgSCp{color:var(--posttitletextcolor);display:inline;padding-right:5px;word-wrap:break-word}._2SdHzo12ISmrC8H86TgSCp._1Y3R-LNfq0EOkZUcePSt1j{filter:blur(6px)}._2SdHzo12ISmrC8H86TgSCp._29WrubtjAcKqzJSPdQqQ4h{font-size:20px;font-weight:500;line-height:24px}._2SdHzo12ISmrC8H86TgSCp._3wqmjmv3tb_k-PROt7qFZe{font-size:18px;font-weight:500;line-height:22px}._2SdHzo12ISmrC8H86TgSCp._1zpZYP8cFNLfLDexPY65Y7{font-size:16px;font-weight:500;line-height:20px}._2SdHzo12ISmrC8H86TgSCp.uWdXen_41bh0iwLrgzFkc{font-size:14px;font-weight:500;line-height:18px}._2SdHzo12ISmrC8H86TgSCp._1aqE18-N18ZIRlkE1wa7DP{font-size:12px;font-weight:500;line-height:16px}._2SdHzo12ISmrC8H86TgSCp._2_YD0sbnnLrJvpCrMxBFaC{font-size:12px;font-weight:400;line-height:16px}._2SdHzo12ISmrC8H86TgSCp._2_QBmCTk6VD4M3dvKqXD23{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}@media (max-width:639px){._2SdHzo12ISmrC8H86TgSCp{font-size:14px;font-weight:500;line-height:18px}}._2FCtq-QzlfuN-SwVMUZMM3{--posttitletextcolor:var(--newCommunityTheme-titleText);--postTitle-VisitedLinkColor:var(--newCommunityTheme-titleText);--postTitleLink-VisitedLinkColor:var(--newCommunityTheme-titleText)}
.XEkFoehJNxIH9Wlr5Ilzd{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row}.XEkFoehJNxIH9Wlr5Ilzd._3Av66iQf7_N4Z-XZxsek76{background-color:var(--newRedditTheme-field)}._17q-ew4FcK6U0ZiybWkIGG{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex}.ENGeNwSHzwN-SV2KTH2s7,._3HTtcITrR-crvsRovLrijl._3HTtcITrR-crvsRovLrijl._3HTtcITrR-crvsRovLrijl{height:20px;width:20px;border-radius:100%}._2aqH0n-kSzFY7HZZ5GL-Jb{font-size:14px;line-height:18px}._2Efd4uMAp4YawdvL9Zhdhv,._2aqH0n-kSzFY7HZZ5GL-Jb{-ms-flex-positive:1;flex-grow:1;margin-left:8px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}._2Efd4uMAp4YawdvL9Zhdhv{font-size:12px;font-weight:400;line-height:16px;padding-right:4px;display:inline-block;vertical-align:top}._1JNAu7U5gWAkRoykwfUWhY{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;padding:16px 16px 8px}.icon.t2A0mgkgGzc8cAahJsR7a{color:var(--newRedditTheme-actionIcon);margin-left:8px}.icon.t2A0mgkgGzc8cAahJsR7a._2cEhEGN_WTLlwspw_bpqTr{color:#0079d3}.ENGeNwSHzwN-SV2KTH2s7{border-radius:4px}._3P_WRCH8aFjwOFA7B1RlBL{margin-left:24px}.bpYVdL9hAnIqOnrKi8PVS{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;margin-bottom:5px;color:#0079d3}
._1blFGqU8stoZgWSZ8MQNpf{position:relative}._1M-azLenSs2UgxeZ2rJX20{margin-left:8px}._2-DL_E9cFo1xsqU3Q8BXnJ{-ms-flex:none;flex:none}._2me05I1oHEys1gUyyDWswt,.icon._2me05I1oHEys1gUyyDWswt{border-radius:9001px;border:none;box-sizing:border-box;display:inline-block;-ms-flex:none;flex:none;font-size:16px;height:16px;line-height:16px;margin-right:4px;vertical-align:sub;width:16px}._2me05I1oHEys1gUyyDWswt._1biYoFBD4CLgOvrr_HinV4,.icon._2me05I1oHEys1gUyyDWswt._1biYoFBD4CLgOvrr_HinV4{border:0;height:32px;width:32px}
._17IuRdA-NY8vFk-Tt991sn{fill:var(--newCommunityTheme-actionIcon)}
._3LO_LEpMLN8-uaedpg6nl4{display:-ms-flexbox;display:flex;opacity:1;min-height:26px;transform:translateY(0);transition:opacity .3s ease-out,transform .3s ease-out;width:-webkit-fit-content;width:fit-content}
._3CUdiRoAXQxoYJ-UeFCjPS{-ms-flex-align:center;align-items:center;border-radius:9999px;display:-ms-flexbox;display:flex;font-weight:500;padding:4px 6px}._2SVIoeexI3lRGCH0NAYAMx{background-color:var(--newRedditTheme-placeholder)}.QRGfIrC3QhcjQPpbXOPJy{background-color:var(--newRedditTheme-canvas);color:#d4d7d9}
._2Xr7MVf-5monsBWevLifeW{-ms-flex-align:center;align-items:center;margin-right:8px}.XuI5nsPhP6eDNKSKFz-e4{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;height:26px;padding:0 8px}._3WmD5z1Jh2YlJtFiczfOPQ._3WmD5z1Jh2YlJtFiczfOPQ{margin-right:8px}.WBGmEslY0knAV_FJ6nxJG.WBGmEslY0knAV_FJ6nxJG{fill:var(--newRedditTheme-bodyText);font-size:16px;line-height:1;height:16px;margin-left:8px;width:16px}._1xMEc-Wt4Qb0j1YKfgnaV-{height:16px;border-radius:9999px;margin-left:8px;width:16px}._1xMEc-Wt4Qb0j1YKfgnaV-.fHi-ixYo4c6B0nG6gLHfT{background-color:var(--newRedditTheme-placeholder);opacity:1;color:var(--newRedditTheme-titleText);font-weight:700;padding:0}._1xMEc-Wt4Qb0j1YKfgnaV-.fHi-ixYo4c6B0nG6gLHfT._14dJJyNdhmM1o-aAiUtZu6:before{opacity:0}._1xMEc-Wt4Qb0j1YKfgnaV-.fHi-ixYo4c6B0nG6gLHfT._3s3sI85UQf8tQPFQZxjTzN{background-color:transparent}._1xMEc-Wt4Qb0j1YKfgnaV-.fHi-ixYo4c6B0nG6gLHfT:hover{background:linear-gradient(0deg,var(--newRedditTheme-menuButtonBackground-hover),var(--newRedditTheme-menuButtonBackground-hover)),var(--newRedditTheme-placeholder)}._1xMEc-Wt4Qb0j1YKfgnaV-.fHi-ixYo4c6B0nG6gLHfT:disabled{background-color:transparent;opacity:.5}._1xMEc-Wt4Qb0j1YKfgnaV-.fHi-ixYo4c6B0nG6gLHfT:active{background:linear-gradient(0deg,var(--newRedditTheme-menuButtonBackground-active),var(--newRedditTheme-menuButtonBackground-active)),var(--newRedditTheme-placeholder)}._1xMEc-Wt4Qb0j1YKfgnaV-.fHi-ixYo4c6B0nG6gLHfT:active:before{opacity:0}._1xMEc-Wt4Qb0j1YKfgnaV-._1QDgUGnYSgM-nXLPnwcp6j{color:#d4d7d9;background-color:var(--newRedditTheme-canvas);opacity:1;color:var(--newRedditTheme-titleText);font-weight:700;padding:0}._1xMEc-Wt4Qb0j1YKfgnaV-._1QDgUGnYSgM-nXLPnwcp6j._14dJJyNdhmM1o-aAiUtZu6:before{opacity:0}._1xMEc-Wt4Qb0j1YKfgnaV-._1QDgUGnYSgM-nXLPnwcp6j._3s3sI85UQf8tQPFQZxjTzN{background-color:transparent}._1xMEc-Wt4Qb0j1YKfgnaV-._1QDgUGnYSgM-nXLPnwcp6j:hover{background:linear-gradient(0deg,var(--newRedditTheme-menuButtonBackground-hover),var(--newRedditTheme-menuButtonBackground-hover)),#000}._1xMEc-Wt4Qb0j1YKfgnaV-._1QDgUGnYSgM-nXLPnwcp6j:disabled{background-color:transparent;opacity:.5}._1xMEc-Wt4Qb0j1YKfgnaV-._1QDgUGnYSgM-nXLPnwcp6j:active{background:linear-gradient(0deg,var(--newRedditTheme-menuButtonBackground-active),var(--newRedditTheme-menuButtonBackground-active)),#000}._1xMEc-Wt4Qb0j1YKfgnaV-._1QDgUGnYSgM-nXLPnwcp6j:active:before{opacity:0}._1xMEc-Wt4Qb0j1YKfgnaV- .WBGmEslY0knAV_FJ6nxJG{margin-left:0}
._1RIl585IYPW6cmNXwgRz0J{position:absolute!important;clip:rect(1px 1px 1px 1px);clip:rect(1px,1px,1px,1px)}
._1DeR7_QiQnu2UK0e2dDfYD{-ms-flex-align:center;align-items:center;box-sizing:border-box;background-color:var(--newRedditTheme-field);border:1px solid var(--newRedditTheme-line);border-radius:1.25em;box-shadow:none;height:40px}._1DeR7_QiQnu2UK0e2dDfYD,._1DeR7_QiQnu2UK0e2dDfYD ._1ugesNSGtWAUEmFe-hdnyI{display:-ms-flexbox;display:flex}._1DeR7_QiQnu2UK0e2dDfYD ._1ugesNSGtWAUEmFe-hdnyI{width:100%}._1DeR7_QiQnu2UK0e2dDfYD ._1K7ubH9z5v9E6C19j2fjQU{background-color:var(--newRedditTheme-field)}._1DeR7_QiQnu2UK0e2dDfYD.h5AN6BnHrFmiSiSIKQbi0{border-bottom-left-radius:unset;border-bottom-right-radius:unset}._1DeR7_QiQnu2UK0e2dDfYD:focus-within,._1DeR7_QiQnu2UK0e2dDfYD:hover{background-color:var(--newRedditTheme-body);border:1px solid var(--newRedditTheme-button)}._1DeR7_QiQnu2UK0e2dDfYD:focus-within ._1K7ubH9z5v9E6C19j2fjQU,._1DeR7_QiQnu2UK0e2dDfYD:hover ._1K7ubH9z5v9E6C19j2fjQU{background-color:var(--newRedditTheme-body)}._1DeR7_QiQnu2UK0e2dDfYD:focus-within ._3XsEUsC3uEaiEi63QWpAM,._1DeR7_QiQnu2UK0e2dDfYD:hover ._3XsEUsC3uEaiEi63QWpAM{display:-ms-flexbox;display:flex;visibility:visible}._1t0x2fnX0IYp1-sp47CSHI{display:-ms-flexbox;display:flex}._1K7ubH9z5v9E6C19j2fjQU{-webkit-appearance:none;appearance:none;color:var(--newRedditTheme-bodyText);font-size:14px;line-height:14px;margin-right:16px;outline:none;width:100%}._1K7ubH9z5v9E6C19j2fjQU ::-webkit-input-placeholder{color:var(--newRedditTheme-actionIcon)}._1K7ubH9z5v9E6C19j2fjQU ::-moz-placeholder{color:var(--newRedditTheme-actionIcon)}._1K7ubH9z5v9E6C19j2fjQU :-ms-input-placeholder{color:var(--newRedditTheme-actionIcon)}._1K7ubH9z5v9E6C19j2fjQU::-webkit-search-cancel-button{display:none}.cNtxQ5c1PdvcDe82u_yz9{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;padding:0 9px 0 15px}._3ylUT2QX58nnEl8r4H26ys{color:var(--newRedditTheme-actionIcon);position:relative;top:1px}._3XsEUsC3uEaiEi63QWpAM{-ms-flex-align:center;align-items:center;visibility:hidden;fill:var(--newRedditTheme-bodyText);margin-right:16px}._3XsEUsC3uEaiEi63QWpAM:focus-visible{border-radius:9999px;height:20px}
._2PnG5snRqhlCLmlBFW9Dud{box-sizing:border-box;height:100%;overflow:auto;pointer-events:none;position:fixed;top:0;width:100%;z-index:55}._2PnG5snRqhlCLmlBFW9Dud._1LKHMvN5rVxTXGRnTa9hrB{background-color:rgba(0,0,0,.5);pointer-events:unset}._3GVs_x5BtyiLy35GpmGSyo{margin-top:-20px}._2EusAZo7A7uyI8gxC0nJdp{background-color:transparent;border:none;box-shadow:none;height:242px;overflow:visible;position:relative;width:540px}._2EusAZo7A7uyI8gxC0nJdp ._1BsafzE6q8PmCVU5uqiTWj{background-color:var(--newCommunityTheme-body);border-radius:8px;height:222px;margin-bottom:20px;margin-right:20px;overflow:visible;width:520px}._2EusAZo7A7uyI8gxC0nJdp ._1BsafzE6q8PmCVU5uqiTWj:after{font-size:50px;position:absolute;line-height:6px;transform:scaleY(1.1);margin-left:-6px;color:var(--newCommunityTheme-body);content:"▶";left:calc(100% - 38px);top:45px;z-index:-1}._2EusAZo7A7uyI8gxC0nJdp ._1BsafzE6q8PmCVU5uqiTWj ._1BFO2H2-rybL94nyL7n-e_{display:-ms-flexbox;display:flex;font-size:28px;font-weight:700;line-height:34px;padding:16px;text-align:center;width:calc(100% - 32px)}._2EusAZo7A7uyI8gxC0nJdp ._1BsafzE6q8PmCVU5uqiTWj ._2DnHuFoYoKwYaBvTkLrs0v{font-size:12px;font-weight:400;line-height:16px;padding:0 94px;text-align:center}._2EusAZo7A7uyI8gxC0nJdp ._1BsafzE6q8PmCVU5uqiTWj ._2DnHuFoYoKwYaBvTkLrs0v ._16moQ9CB6asKjB-qTj8Tvf{text-decoration:underline}._2EusAZo7A7uyI8gxC0nJdp ._1BsafzE6q8PmCVU5uqiTWj ._2x6OQ6vZfN3PNhM6Eh6FLq{margin:20px 169px;width:182px}
.grecaptcha-badge{visibility:hidden}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/Governance~Reddit.af725272a97a52ae2008_.css.map*/</style><style data-href="chunkCSS/Reddit.911524dea63800915309_.css" data-chunk="Reddit" key="chunkCSS/Reddit.911524dea63800915309_.css">@font-face{font-family:redesignFont2020;src:url(https://www.redditstatic.com/desktop2x/fonts/redesignIcon2020/redesignFont2020.b133f9247bc5bb41b64a1daebd57ace5.eot),url(https://www.redditstatic.com/desktop2x/fonts/redesignIcon2020/redesignFont2020.b133f9247bc5bb41b64a1daebd57ace5.woff),url(https://www.redditstatic.com/desktop2x/fonts/redesignIcon2020/redesignFont2020.b133f9247bc5bb41b64a1daebd57ace5.ttf),url(https://www.redditstatic.com/desktop2x/fonts/redesignIcon2020/redesignFont2020.b133f9247bc5bb41b64a1daebd57ace5.svg)}.icon:before{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;font-family:redesignFont2020}.icon-activity:before{content:"\f101"}.icon-activity_fill:before{content:"\f102"}.icon-ad_group:before{content:"\f103"}.icon-ad_group_fill:before{content:"\f104"}.icon-add:before{content:"\f105"}.icon-add_emoji:before{content:"\f106"}.icon-add_emoji_fill:before{content:"\f107"}.icon-add_fill:before{content:"\f108"}.icon-add_media:before{content:"\f109"}.icon-add_media_fill:before{content:"\f10a"}.icon-add_to_feed:before{content:"\f10b"}.icon-add_to_feed_fill:before{content:"\f10c"}.icon-admin:before{content:"\f10d"}.icon-admin_fill:before{content:"\f10e"}.icon-all:before{content:"\f10f"}.icon-all_fill:before{content:"\f110"}.icon-appearance:before{content:"\f111"}.icon-appearance_fill:before{content:"\f112"}.icon-approve:before{content:"\f113"}.icon-approve_fill:before{content:"\f114"}.icon-archived:before{content:"\f115"}.icon-archived_fill:before{content:"\f116"}.icon-aspect_ratio:before{content:"\f117"}.icon-aspect_ratio_fill:before{content:"\f118"}.icon-aspect_rectangle:before{content:"\f119"}.icon-aspect_rectangle_fill:before{content:"\f11a"}.icon-attach:before{content:"\f11b"}.icon-attach_fill:before{content:"\f11c"}.icon-audio:before{content:"\f11d"}.icon-audio_fill:before{content:"\f11e"}.icon-author:before{content:"\f11f"}.icon-author_fill:before{content:"\f120"}.icon-avatar_style:before{content:"\f121"}.icon-avatar_style_fill:before{content:"\f122"}.icon-award:before{content:"\f123"}.icon-award_fill:before{content:"\f124"}.icon-back:before{content:"\f125"}.icon-back_fill:before{content:"\f126"}.icon-ban:before{content:"\f127"}.icon-ban_fill:before{content:"\f128"}.icon-best:before{content:"\f129"}.icon-best_fill:before{content:"\f12a"}.icon-block:before{content:"\f12b"}.icon-block_fill:before{content:"\f12c"}.icon-bold:before{content:"\f12d"}.icon-bold_fill:before{content:"\f12e"}.icon-bot:before{content:"\f12f"}.icon-bot_fill:before{content:"\f130"}.icon-bounce:before{content:"\f131"}.icon-bounce_fill:before{content:"\f132"}.icon-browse:before{content:"\f133"}.icon-browse_fill:before{content:"\f134"}.icon-browser:before{content:"\f135"}.icon-browser_fill:before{content:"\f136"}.icon-cake:before{content:"\f137"}.icon-cake_fill:before{content:"\f138"}.icon-calendar:before{content:"\f139"}.icon-camera:before{content:"\f13a"}.icon-camera_fill:before{content:"\f13b"}.icon-campaign:before{content:"\f13c"}.icon-campaign_fill:before{content:"\f13d"}.icon-caret_down:before{content:"\f13e"}.icon-caret_down_fill:before{content:"\f13f"}.icon-caret_left:before{content:"\f140"}.icon-caret_left_fill:before{content:"\f141"}.icon-caret_right:before{content:"\f142"}.icon-caret_right_fill:before{content:"\f143"}.icon-caret_up:before{content:"\f144"}.icon-caret_up_fill:before{content:"\f145"}.icon-chat:before{content:"\f146"}.icon-chat_fill:before{content:"\f147"}.icon-chat_group:before{content:"\f148"}.icon-chat_group_fill:before{content:"\f149"}.icon-chat_new:before{content:"\f14a"}.icon-chat_new_fill:before{content:"\f14b"}.icon-checkbox:before{content:"\f14c"}.icon-checkbox_dismiss:before{content:"\f14d"}.icon-checkbox_dismiss_fill:before{content:"\f14e"}.icon-checkbox_fill:before{content:"\f14f"}.icon-checkmark:before{content:"\f150"}.icon-checkmark_fill:before{content:"\f151"}.icon-chrome:before{content:"\f152"}.icon-chrome_fill:before{content:"\f153"}.icon-clear:before{content:"\f154"}.icon-clear_fill:before{content:"\f155"}.icon-close:before{content:"\f156"}.icon-close_fill:before{content:"\f157"}.icon-closed_captioning:before{content:"\f158"}.icon-closed_captioning_fill:before{content:"\f159"}.icon-closet_1:before{content:"\f15a"}.icon-closet_1_fill:before{content:"\f15b"}.icon-closet_2:before{content:"\f15c"}.icon-closet_2_fill:before{content:"\f15d"}.icon-closet_3:before{content:"\f15e"}.icon-closet_3_fill:before{content:"\f15f"}.icon-code_block:before{content:"\f160"}.icon-code_block_fill:before{content:"\f161"}.icon-code_inline:before{content:"\f162"}.icon-code_inline_fill:before{content:"\f163"}.icon-coins:before{content:"\f164"}.icon-coins_fill:before{content:"\f165"}.icon-coins_outline_color:before{content:"\f166"}.icon-collapse:before{content:"\f167"}.icon-collapse_fill:before{content:"\f168"}.icon-collapse_left:before{content:"\f169"}.icon-collapse_left_fill:before{content:"\f16a"}.icon-collapse_right:before{content:"\f16b"}.icon-collapse_right_fill:before{content:"\f16c"}.icon-collection:before{content:"\f16d"}.icon-collection_fill:before{content:"\f16e"}.icon-comment:before{content:"\f16f"}.icon-comment_fill:before{content:"\f170"}.icon-comments:before{content:"\f171"}.icon-comments_fill:before{content:"\f172"}.icon-community:before{content:"\f173"}.icon-community_fill:before{content:"\f174"}.icon-controversial:before{content:"\f175"}.icon-controversial_fill:before{content:"\f176"}.icon-conversion_1:before{content:"\f177"}.icon-conversion_1_fill:before{content:"\f178"}.icon-conversion_2:before{content:"\f179"}.icon-conversion_2_fill:before{content:"\f17a"}.icon-copyid:before{content:"\f17b"}.icon-copyid_fill:before{content:"\f17c"}.icon-crop:before{content:"\f17d"}.icon-crop_fill:before{content:"\f17e"}.icon-crosspost:before{content:"\f17f"}.icon-crosspost_fill:before{content:"\f180"}.icon-crowd_control:before{content:"\f181"}.icon-crowd_control_fill:before{content:"\f182"}.icon-csv:before{content:"\f183"}.icon-csv_fill:before{content:"\f184"}.icon-custom_feed:before{content:"\f185"}.icon-custom_feed_fill:before{content:"\f186"}.icon-customize:before{content:"\f187"}.icon-customize_fill:before{content:"\f188"}.icon-day:before{content:"\f189"}.icon-day_fill:before{content:"\f18a"}.icon-delete:before{content:"\f18b"}.icon-delete_fill:before{content:"\f18c"}.icon-discover:before{content:"\f18d"}.icon-discover_fill:before{content:"\f18e"}.icon-dismiss_all:before{content:"\f18f"}.icon-dismiss_all_fill:before{content:"\f190"}.icon-distinguish:before{content:"\f191"}.icon-distinguish_fill:before{content:"\f192"}.icon-down:before{content:"\f193"}.icon-down_fill:before{content:"\f194"}.icon-download:before{content:"\f195"}.icon-download_fill:before{content:"\f196"}.icon-downvote:before{content:"\f197"}.icon-downvote_fill:before{content:"\f198"}.icon-downvotes:before{content:"\f199"}.icon-downvotes_fill:before{content:"\f19a"}.icon-drag:before{content:"\f19b"}.icon-duplicate:before{content:"\f19c"}.icon-duplicate_fill:before{content:"\f19d"}.icon-edit:before{content:"\f19e"}.icon-edit_fill:before{content:"\f19f"}.icon-effect:before{content:"\f1a0"}.icon-effect_fill:before{content:"\f1a1"}.icon-embed:before{content:"\f1a2"}.icon-embed_fill:before{content:"\f1a3"}.icon-emoji:before{content:"\f1a4"}.icon-emoji_fill:before{content:"\f1a5"}.icon-expand:before{content:"\f1a6"}.icon-expand_fill:before{content:"\f1a7"}.icon-expand_left:before{content:"\f1a8"}.icon-expand_left_fill:before{content:"\f1a9"}.icon-expand_right:before{content:"\f1aa"}.icon-expand_right_fill:before{content:"\f1ab"}.icon-external_link:before{content:"\f1ac"}.icon-external_link_fill:before{content:"\f1ad"}.icon-faceplate:before{content:"\f1ae"}.icon-faceplate_fill:before{content:"\f1af"}.icon-feed_posts:before{content:"\f1b0"}.icon-feed_posts_fill:before{content:"\f1b1"}.icon-feed_video:before{content:"\f1b2"}.icon-feed_video_fill:before{content:"\f1b3"}.icon-filter:before{content:"\f1b4"}.icon-filter_fill:before{content:"\f1b5"}.icon-format:before{content:"\f1b6"}.icon-format_fill:before{content:"\f1b7"}.icon-forward:before{content:"\f1b8"}.icon-forward_fill:before{content:"\f1b9"}.icon-gif_post:before{content:"\f1ba"}.icon-gif_post_fill:before{content:"\f1bb"}.icon-heart:before{content:"\f1bc"}.icon-heart_fill:before{content:"\f1bd"}.icon-help:before{content:"\f1be"}.icon-help_fill:before{content:"\f1bf"}.icon-hide:before{content:"\f1c0"}.icon-hide_fill:before{content:"\f1c1"}.icon-history:before{content:"\f1c2"}.icon-history_fill:before{content:"\f1c3"}.icon-home:before{content:"\f1c4"}.icon-home_fill:before{content:"\f1c5"}.icon-hot:before{content:"\f1c6"}.icon-hot_fill:before{content:"\f1c7"}.icon-icon_vault:before{content:"\f1c8"}.icon-icon_vault_fill:before{content:"\f1c9"}.icon-ignore_reports:before{content:"\f1ca"}.icon-ignore_reports_fill:before{content:"\f1cb"}.icon-image_post:before{content:"\f1cc"}.icon-image_post_fill:before{content:"\f1cd"}.icon-info:before{content:"\f1ce"}.icon-info_fill:before{content:"\f1cf"}.icon-invite:before{content:"\f1d0"}.icon-invite_fill:before{content:"\f1d1"}.icon-italic:before{content:"\f1d2"}.icon-italic_fill:before{content:"\f1d3"}.icon-join:before{content:"\f1d4"}.icon-join_fill:before{content:"\f1d5"}.icon-joined:before{content:"\f1d6"}.icon-joined_fill:before{content:"\f1d7"}.icon-jump_down:before{content:"\f1d8"}.icon-jump_down_fill:before{content:"\f1d9"}.icon-jump_up:before{content:"\f1da"}.icon-jump_up_fill:before{content:"\f1db"}.icon-karma:before{content:"\f1dc"}.icon-karma_fill:before{content:"\f1dd"}.icon-keyboard:before{content:"\f1de"}.icon-keyboard_fill:before{content:"\f1df"}.icon-kick:before{content:"\f1e0"}.icon-kick_fill:before{content:"\f1e1"}.icon-leave:before{content:"\f1e2"}.icon-leave_fill:before{content:"\f1e3"}.icon-left:before{content:"\f1e4"}.icon-left_fill:before{content:"\f1e5"}.icon-link_post:before{content:"\f1e6"}.icon-link_post_fill:before{content:"\f1e7"}.icon-list_bulleted:before{content:"\f1e8"}.icon-list_bulleted_fill:before{content:"\f1e9"}.icon-list_numbered:before{content:"\f1ea"}.icon-list_numbered_fill:before{content:"\f1eb"}.icon-live:before{content:"\f1ec"}.icon-live_fill:before{content:"\f1ed"}.icon-load:before{content:"\f1ee"}.icon-location:before{content:"\f1ef"}.icon-location_fill:before{content:"\f1f0"}.icon-lock:before{content:"\f1f1"}.icon-lock_fill:before{content:"\f1f2"}.icon-logout:before{content:"\f1f3"}.icon-logout_fill:before{content:"\f1f4"}.icon-loop:before{content:"\f1f5"}.icon-loop_fill:before{content:"\f1f6"}.icon-mark_read:before{content:"\f1f7"}.icon-mark_read_fill:before{content:"\f1f8"}.icon-mask:before{content:"\f1f9"}.icon-mask_fill:before{content:"\f1fa"}.icon-media_gallery:before{content:"\f1fb"}.icon-media_gallery_fill:before{content:"\f1fc"}.icon-meme:before{content:"\f1fd"}.icon-meme_fill:before{content:"\f1fe"}.icon-menu:before{content:"\f1ff"}.icon-menu_fill:before{content:"\f200"}.icon-message:before{content:"\f201"}.icon-message_fill:before{content:"\f202"}.icon-mic:before{content:"\f203"}.icon-mic_fill:before{content:"\f204"}.icon-mic_mute:before{content:"\f205"}.icon-mic_mute_fill:before{content:"\f206"}.icon-mod:before{content:"\f207"}.icon-mod_fill:before{content:"\f208"}.icon-mod_mail:before{content:"\f209"}.icon-mod_mail_fill:before{content:"\f20a"}.icon-mod_mode:before{content:"\f20b"}.icon-mod_mode_fill:before{content:"\f20c"}.icon-mod_mute:before{content:"\f20d"}.icon-mod_mute_fill:before{content:"\f20e"}.icon-mod_overflow:before{content:"\f20f"}.icon-mod_overflow_fill:before{content:"\f210"}.icon-mod_queue:before{content:"\f211"}.icon-mod_queue_fill:before{content:"\f212"}.icon-mod_unmute:before{content:"\f213"}.icon-mod_unmute_fill:before{content:"\f214"}.icon-new:before{content:"\f215"}.icon-new_fill:before{content:"\f216"}.icon-night:before{content:"\f217"}.icon-night_fill:before{content:"\f218"}.icon-notification:before{content:"\f219"}.icon-notification_fill:before{content:"\f21a"}.icon-notification_frequent:before{content:"\f21b"}.icon-notification_frequent_fill:before{content:"\f21c"}.icon-notification_off:before{content:"\f21d"}.icon-notification_off_fill:before{content:"\f21e"}.icon-nsfw:before{content:"\f21f"}.icon-nsfw_fill:before{content:"\f220"}.icon-nsfw_language:before{content:"\f221"}.icon-nsfw_language_fill:before{content:"\f222"}.icon-nsfw_violence:before{content:"\f223"}.icon-nsfw_violence_fill:before{content:"\f224"}.icon-original:before{content:"\f225"}.icon-original_fill:before{content:"\f226"}.icon-overflow_carat:before{content:"\f227"}.icon-overflow_carat_fill:before{content:"\f228"}.icon-overflow_horizontal:before{content:"\f229"}.icon-overflow_vertical:before{content:"\f22a"}.icon-pause:before{content:"\f22b"}.icon-pause_fill:before{content:"\f22c"}.icon-payment:before{content:"\f22d"}.icon-payment_fill:before{content:"\f22e"}.icon-peace:before{content:"\f22f"}.icon-peace_fill:before{content:"\f230"}.icon-pending_posts:before{content:"\f231"}.icon-pending_posts_fill:before{content:"\f232"}.icon-pin:before{content:"\f233"}.icon-pin_fill:before{content:"\f234"}.icon-play:before{content:"\f235"}.icon-play_fill:before{content:"\f236"}.icon-poll_post:before{content:"\f237"}.icon-poll_post_fill:before{content:"\f238"}.icon-popular:before{content:"\f239"}.icon-popular_fill:before{content:"\f23a"}.icon-powerup:before{content:"\f23b"}.icon-powerup_color_outline:before{content:"\f23c"}.icon-powerup_fill:before{content:"\f23d"}.icon-powerup_fill_color:before{content:"\f23e"}.icon-prediction:before{content:"\f23f"}.icon-prediction_fill:before{content:"\f240"}.icon-predictions:before{content:"\f241"}.icon-predictions_fill:before{content:"\f242"}.icon-premium:before{content:"\f243"}.icon-premium_fill:before{content:"\f244"}.icon-privacy:before{content:"\f245"}.icon-privacy_fill:before{content:"\f246"}.icon-profile:before{content:"\f247"}.icon-profile_fill:before{content:"\f248"}.icon-promote_snoo:before{content:"\f249"}.icon-qr_code:before{content:"\f24a"}.icon-quarantined:before{content:"\f24b"}.icon-quarantined_fill:before{content:"\f24c"}.icon-quote:before{content:"\f24d"}.icon-quote_fill:before{content:"\f24e"}.icon-r_slash:before{content:"\f24f"}.icon-r_slash_fill:before{content:"\f250"}.icon-radio_button:before{content:"\f251"}.icon-radio_button_fill:before{content:"\f252"}.icon-raise_hand:before{content:"\f253"}.icon-raise_hand_fill:before{content:"\f254"}.icon-random:before{content:"\f255"}.icon-random_fill:before{content:"\f256"}.icon-rating_drugs:before{content:"\f257"}.icon-rating_everyone:before{content:"\f258"}.icon-rating_mature:before{content:"\f259"}.icon-rating_nsfw:before{content:"\f25a"}.icon-rating_violence:before{content:"\f25b"}.icon-refresh:before{content:"\f25c"}.icon-refresh_fill:before{content:"\f25d"}.icon-remove:before{content:"\f25e"}.icon-remove_fill:before{content:"\f25f"}.icon-reply:before{content:"\f260"}.icon-reply_fill:before{content:"\f261"}.icon-report:before{content:"\f262"}.icon-report_fill:before{content:"\f263"}.icon-reverse:before{content:"\f264"}.icon-reverse_fill:before{content:"\f265"}.icon-right:before{content:"\f266"}.icon-right_fill:before{content:"\f267"}.icon-rising:before{content:"\f268"}.icon-rising_fill:before{content:"\f269"}.icon-rotate:before{content:"\f26a"}.icon-rotate_fill:before{content:"\f26b"}.icon-rpan:before{content:"\f26c"}.icon-rpan_fill:before{content:"\f26d"}.icon-rules:before{content:"\f26e"}.icon-rules_fill:before{content:"\f26f"}.icon-safari:before{content:"\f270"}.icon-safari_fill:before{content:"\f271"}.icon-save:before{content:"\f272"}.icon-save_fill:before{content:"\f273"}.icon-save_table:before{content:"\f274"}.icon-save_table_fill:before{content:"\f275"}.icon-saved:before{content:"\f276"}.icon-saved_fill:before{content:"\f277"}.icon-scheduled:before{content:"\f278"}.icon-scheduled_fill:before{content:"\f279"}.icon-search:before{content:"\f27a"}.icon-search_fill:before{content:"\f27b"}.icon-self:before{content:"\f27c"}.icon-self_fill:before{content:"\f27d"}.icon-send:before{content:"\f27e"}.icon-send_fill:before{content:"\f27f"}.icon-settings:before{content:"\f280"}.icon-settings_fill:before{content:"\f281"}.icon-share:before{content:"\f282"}.icon-share_android:before{content:"\f283"}.icon-share_android_fill:before{content:"\f284"}.icon-share_fill:before{content:"\f285"}.icon-share_ios:before{content:"\f286"}.icon-share_ios_fill:before{content:"\f287"}.icon-show:before{content:"\f288"}.icon-show_fill:before{content:"\f289"}.icon-side_menu:before{content:"\f28a"}.icon-side_menu_fill:before{content:"\f28b"}.icon-skipback10:before{content:"\f28c"}.icon-skipback10_fill:before{content:"\f28d"}.icon-skipforward10:before{content:"\f28e"}.icon-skipforward10_fill:before{content:"\f28f"}.icon-sort:before{content:"\f290"}.icon-sort_fill:before{content:"\f291"}.icon-spam:before{content:"\f292"}.icon-spam_fill:before{content:"\f293"}.icon-spoiler:before{content:"\f294"}.icon-spoiler_fill:before{content:"\f295"}.icon-sponsored:before{content:"\f296"}.icon-sponsored_fill:before{content:"\f297"}.icon-star:before{content:"\f298"}.icon-star_fill:before{content:"\f299"}.icon-statistics:before{content:"\f29a"}.icon-statistics_fill:before{content:"\f29b"}.icon-sticker:before{content:"\f29c"}.icon-sticker_fill:before{content:"\f29d"}.icon-strikethrough:before{content:"\f29e"}.icon-strikethrough_fill:before{content:"\f29f"}.icon-subtract:before{content:"\f2a0"}.icon-subtract_fill:before{content:"\f2a1"}.icon-superscript:before{content:"\f2a2"}.icon-superscript_fill:before{content:"\f2a3"}.icon-swap_camera:before{content:"\f2a4"}.icon-swap_camera_fill:before{content:"\f2a5"}.icon-swipe_back:before{content:"\f2a6"}.icon-swipe_back_fill:before{content:"\f2a7"}.icon-swipe_down:before{content:"\f2a8"}.icon-swipe_down_fill:before{content:"\f2a9"}.icon-swipe_forward:before{content:"\f2aa"}.icon-swipe_forward_fill:before{content:"\f2ab"}.icon-swipe_up:before{content:"\f2ac"}.icon-swipe_up_fill:before{content:"\f2ad"}.icon-table:before{content:"\f2ae"}.icon-table_fill:before{content:"\f2af"}.icon-tag:before{content:"\f2b0"}.icon-tag_fill:before{content:"\f2b1"}.icon-tap:before{content:"\f2b2"}.icon-tap_fill:before{content:"\f2b3"}.icon-text_post:before{content:"\f2b4"}.icon-text_post_fill:before{content:"\f2b5"}.icon-text_size:before{content:"\f2b6"}.icon-text_size_fill:before{content:"\f2b7"}.icon-top:before{content:"\f2b8"}.icon-top_fill:before{content:"\f2b9"}.icon-topic:before{content:"\f2ba"}.icon-topic_activism:before{content:"\f2bb"}.icon-topic_activism_fill:before{content:"\f2bc"}.icon-topic_addiction_support:before{content:"\f2bd"}.icon-topic_addictionsupport:before{content:"\f2be"}.icon-topic_addictionsupport_fill:before{content:"\f2bf"}.icon-topic_advice:before{content:"\f2c0"}.icon-topic_advice_fill:before{content:"\f2c1"}.icon-topic_animals:before{content:"\f2c2"}.icon-topic_animals_fill:before{content:"\f2c3"}.icon-topic_anime:before{content:"\f2c4"}.icon-topic_anime_fill:before{content:"\f2c5"}.icon-topic_art:before{content:"\f2c6"}.icon-topic_art_fill:before{content:"\f2c7"}.icon-topic_beauty:before{content:"\f2c8"}.icon-topic_beauty_fill:before{content:"\f2c9"}.icon-topic_business:before{content:"\f2ca"}.icon-topic_business_fill:before{content:"\f2cb"}.icon-topic_careers:before{content:"\f2cc"}.icon-topic_careers_fill:before{content:"\f2cd"}.icon-topic_cars:before{content:"\f2ce"}.icon-topic_cars_fill:before{content:"\f2cf"}.icon-topic_celebrity:before{content:"\f2d0"}.icon-topic_celebrity_fill:before{content:"\f2d1"}.icon-topic_crafts:before{content:"\f2d2"}.icon-topic_crafts_fill:before{content:"\f2d3"}.icon-topic_crypto:before{content:"\f2d4"}.icon-topic_crypto_fill:before{content:"\f2d5"}.icon-topic_culture:before{content:"\f2d6"}.icon-topic_culture_fill:before{content:"\f2d7"}.icon-topic_diy:before{content:"\f2d8"}.icon-topic_diy_fill:before{content:"\f2d9"}.icon-topic_entertainment:before{content:"\f2da"}.icon-topic_entertainment_fill:before{content:"\f2db"}.icon-topic_ethics:before{content:"\f2dc"}.icon-topic_ethics_fill:before{content:"\f2dd"}.icon-topic_family:before{content:"\f2de"}.icon-topic_family_fill:before{content:"\f2df"}.icon-topic_fashion:before{content:"\f2e0"}.icon-topic_fill:before{content:"\f2e1"}.icon-topic_fitness:before{content:"\f2e2"}.icon-topic_fitness_fill:before{content:"\f2e3"}.icon-topic_food:before{content:"\f2e4"}.icon-topic_food_fill:before{content:"\f2e5"}.icon-topic_funny:before{content:"\f2e6"}.icon-topic_funny_fill:before{content:"\f2e7"}.icon-topic_gender:before{content:"\f2e8"}.icon-topic_gender_fill:before{content:"\f2e9"}.icon-topic_health:before{content:"\f2ea"}.icon-topic_health_fill:before{content:"\f2eb"}.icon-topic_help:before{content:"\f2ec"}.icon-topic_help_fill:before{content:"\f2ed"}.icon-topic_history:before{content:"\f2ee"}.icon-topic_history_fill:before{content:"\f2ef"}.icon-topic_internet:before{content:"\f2f0"}.icon-topic_internet_fill:before{content:"\f2f1"}.icon-topic_law:before{content:"\f2f2"}.icon-topic_law_fill:before{content:"\f2f3"}.icon-topic_learning:before{content:"\f2f4"}.icon-topic_learning_fill:before{content:"\f2f5"}.icon-topic_lifestyle:before{content:"\f2f6"}.icon-topic_lifestyle_fill:before{content:"\f2f7"}.icon-topic_mature:before{content:"\f2f8"}.icon-topic_mature_fill:before{content:"\f2f9"}.icon-topic_mensfashion:before{content:"\f2fa"}.icon-topic_mensfashion_fill:before{content:"\f2fb"}.icon-topic_menshealth:before{content:"\f2fc"}.icon-topic_menshealth_fill:before{content:"\f2fd"}.icon-topic_meta:before{content:"\f2fe"}.icon-topic_meta_fill:before{content:"\f2ff"}.icon-topic_military:before{content:"\f300"}.icon-topic_military_fill:before{content:"\f301"}.icon-topic_movies:before{content:"\f302"}.icon-topic_movies_fill:before{content:"\f303"}.icon-topic_music:before{content:"\f304"}.icon-topic_music_fill:before{content:"\f305"}.icon-topic_nature:before{content:"\f306"}.icon-topic_nature_fill:before{content:"\f307"}.icon-topic_news:before{content:"\f308"}.icon-topic_news_fill:before{content:"\f309"}.icon-topic_other:before{content:"\f30a"}.icon-topic_other_fill:before{content:"\f30b"}.icon-topic_outdoors:before{content:"\f30c"}.icon-topic_pets:before{content:"\f30d"}.icon-topic_pets_fill:before{content:"\f30e"}.icon-topic_photography:before{content:"\f30f"}.icon-topic_photography_fill:before{content:"\f310"}.icon-topic_places:before{content:"\f311"}.icon-topic_places_fill:before{content:"\f312"}.icon-topic_podcasts:before{content:"\f313"}.icon-topic_podcasts_fill:before{content:"\f314"}.icon-topic_politics:before{content:"\f315"}.icon-topic_politics_fill:before{content:"\f316"}.icon-topic_programming:before{content:"\f317"}.icon-topic_programming_fill:before{content:"\f318"}.icon-topic_reading:before{content:"\f319"}.icon-topic_reading_fill:before{content:"\f31a"}.icon-topic_religion:before{content:"\f31b"}.icon-topic_religion_fill:before{content:"\f31c"}.icon-topic_science:before{content:"\f31d"}.icon-topic_science_fill:before{content:"\f31e"}.icon-topic_sexorientation:before{content:"\f31f"}.icon-topic_sexorientation_fill:before{content:"\f320"}.icon-topic_sports:before{content:"\f321"}.icon-topic_sports_fill:before{content:"\f322"}.icon-topic_style:before{content:"\f323"}.icon-topic_style_fill:before{content:"\f324"}.icon-topic_tabletop:before{content:"\f325"}.icon-topic_tabletopgames:before{content:"\f326"}.icon-topic_tabletopgames_fill:before{content:"\f327"}.icon-topic_technology:before{content:"\f328"}.icon-topic_technology_fill:before{content:"\f329"}.icon-topic_television:before{content:"\f32a"}.icon-topic_television_fill:before{content:"\f32b"}.icon-topic_traumasupport:before{content:"\f32c"}.icon-topic_travel:before{content:"\f32d"}.icon-topic_travel_fill:before{content:"\f32e"}.icon-topic_videogaming:before{content:"\f32f"}.icon-topic_videogaming_fill:before{content:"\f330"}.icon-topic_womensfashion:before{content:"\f331"}.icon-topic_womensfashion_fill:before{content:"\f332"}.icon-topic_womenshealth:before{content:"\f333"}.icon-topic_womenshealth_fill:before{content:"\f334"}.icon-traumasupport:before{content:"\f335"}.icon-traumasupport_fill:before{content:"\f336"}.icon-trim:before{content:"\f337"}.icon-trim_fill:before{content:"\f338"}.icon-trophy:before{content:"\f339"}.icon-trophy_fill:before{content:"\f33a"}.icon-u_slash:before{content:"\f33b"}.icon-u_slash_fill:before{content:"\f33c"}.icon-unban:before{content:"\f33d"}.icon-unban_fill:before{content:"\f33e"}.icon-undo:before{content:"\f33f"}.icon-undo_fill:before{content:"\f340"}.icon-unheart:before{content:"\f341"}.icon-unlock:before{content:"\f342"}.icon-unlock_fill:before{content:"\f343"}.icon-unmod:before{content:"\f344"}.icon-unmod_fill:before{content:"\f345"}.icon-unpin:before{content:"\f346"}.icon-unpin_fill:before{content:"\f347"}.icon-unverified:before{content:"\f348"}.icon-unverified_fill:before{content:"\f349"}.icon-up:before{content:"\f34a"}.icon-up_fill:before{content:"\f34b"}.icon-upload:before{content:"\f34c"}.icon-upload_fill:before{content:"\f34d"}.icon-upvote:before{content:"\f34e"}.icon-upvote_fill:before{content:"\f34f"}.icon-upvotes:before{content:"\f350"}.icon-upvotes_fill:before{content:"\f351"}.icon-user:before{content:"\f352"}.icon-user_fill:before{content:"\f353"}.icon-user_note:before{content:"\f354"}.icon-user_note_fill:before{content:"\f355"}.icon-vault:before{content:"\f356"}.icon-vault_fill:before{content:"\f357"}.icon-verified:before{content:"\f358"}.icon-verified_fill:before{content:"\f359"}.icon-video_camera:before{content:"\f35a"}.icon-video_camera_fill:before{content:"\f35b"}.icon-video_feed:before{content:"\f35c"}.icon-video_feed_fill:before{content:"\f35d"}.icon-video_live:before{content:"\f35e"}.icon-video_live_fill:before{content:"\f35f"}.icon-video_post:before{content:"\f360"}.icon-video_post_fill:before{content:"\f361"}.icon-view_card:before{content:"\f362"}.icon-view_card_fill:before{content:"\f363"}.icon-view_classic:before{content:"\f364"}.icon-view_classic_fill:before{content:"\f365"}.icon-view_compact:before{content:"\f366"}.icon-view_compact_fill:before{content:"\f367"}.icon-view_grid:before{content:"\f368"}.icon-view_grid_fill:before{content:"\f369"}.icon-view_grid_fill_1:before{content:"\f36a"}.icon-views:before{content:"\f36b"}.icon-views_fill:before{content:"\f36c"}.icon-volume:before{content:"\f36d"}.icon-volume_fill:before{content:"\f36e"}.icon-volume_mute:before{content:"\f36f"}.icon-volume_mute_fill:before{content:"\f370"}.icon-wiki:before{content:"\f371"}.icon-wiki_ban:before{content:"\f372"}.icon-wiki_ban_fill:before{content:"\f373"}.icon-wiki_fill:before{content:"\f374"}.icon-wiki_unban:before{content:"\f375"}.icon-wiki_unban_fill:before{content:"\f376"}.icon-world:before{content:"\f377"}.icon-world_fill:before{content:"\f378"}
@font-face{font-family:BentonSans;font-weight:300;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Light-6dccf00b06936bd0fb2913d5e7279816-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Light-56973edfcf61447fc1ffeb7a6eb6b178-font.woff) format("woff")}@font-face{font-family:BentonSans;font-weight:300;font-style:italic;src:url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Light-Italic-36b388f18999631c032ceeade2312d41-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Light-Italic-112953068bc678d61f4553a1184561f0-font.woff) format("woff")}@font-face{font-family:BentonSans;font-weight:400;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Regular-10f4d2158069741ac4ddbc45710381a1-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Regular-e6bbcdd30d3bd4d6b170bcb6d3552cab-font.woff) format("woff")}@font-face{font-family:BentonSans;font-weight:400;font-style:italic;src:url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Italic-a79b88d69296747b773f0e224cc42ea1-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Italic-5267af566ab853eb9d74db1a78a46c67-font.woff) format("woff")}@font-face{font-family:BentonSans;font-weight:500;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Medium-d7c31b2e9ada52f5ad11194858e44a93-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Medium-1051a531d3e1ee3483a6533158557139-font.woff) format("woff")}@font-face{font-family:BentonSans;font-weight:500;font-style:italic;src:url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Medium-Italic-9abd3f23e60e4f632817ebdff606b8ec-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Medium-Italic-a25d440012460eb8883e539f93040fa7-font.woff) format("woff")}@font-face{font-family:BentonSans;font-weight:700;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Bold-91e4c20cbb21e802d984a5ca6ac174a0-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Bold-c34ba754b7235b49d33b294ff7a54179-font.woff) format("woff")}@font-face{font-family:BentonSans;font-weight:700;font-style:italic;src:url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Bold-Italic-fc6d8a3f6499b32d9a6be03168b8066f-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/BentonSans/Bold-Italic-255b4934a1f414dd312aa89382d65114-font.woff) format("woff")}
@font-face{font-family:RedditSans;font-weight:400;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-Regular-f6da4a74985e726695c5550b2a96360d-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-Regular-938c6d17d3195feb74fbfcbf6d028c47-font.woff) format("woff")}@font-face{font-family:RedditSans;font-weight:700;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-Bold-00b9ceb8410bb0559de9132fb8c5ddbd-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-Bold-919ed023cc331c1b982510dce87edaf0-font.woff) format("woff")}@font-face{font-family:RedditSans;font-weight:600;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-SemiBold-fcee61fe0a8b9eb173d0b097bdf1be07-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-SemiBold-a8cf195e6dc5180d834bd4ba84701907-font.woff) format("woff")}@font-face{font-family:RedditSans;font-weight:800;font-style:italic;src:url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-ExtraBoldItalic-0346885b2f9e13f7d733268cb8916a8c-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-ExtraBoldItalic-84b1042d8aac344ee8f4d25444049aa7-font.woff) format("woff")}@font-face{font-family:RedditSans;font-weight:800;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-ExtraBold-a6a549325ce2e7248e5bf8997bbde759-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/RedditSans/RedditSans-ExtraBold-6633c8402da41892cddf755223abb785-font.woff) format("woff")}
@font-face{font-family:VCR;font-weight:400;font-style:normal;src:url(https://www.redditstatic.com/desktop2x/fonts/VCR/Regular-8917e4f4dcb46c5f44221e2652d435d4-font.woff2) format("woff2"),url(https://www.redditstatic.com/desktop2x/fonts/VCR/Regular-e6bbcdd30d3bd4d6b170bcb6d3552cab-font.woff) format("woff")}
.theme-light,:root{--rem320:20rem;--rem192:12rem;--rem144:9rem;--rem128:8rem;--rem96:6rem;--rem88:5.5rem;--rem64:4rem;--rem56:3.5rem;--rem48:3rem;--rem40:2.5rem;--rem36:2.25rem;--rem32:2rem;--rem28:1.75rem;--rem26:1.625rem;--rem24:1.5rem;--rem22:1.375rem;--rem20:1.25rem;--rem18:1.125rem;--rem16:1rem;--rem15:0.9375rem;--rem14:0.875rem;--rem12:0.75rem;--rem10:0.625rem;--rem8:0.5rem;--rem6:0.375rem;--rem4:0.25rem;--rem2:0.125rem;--rem1:0.0625rem;--spacer-2xs:0.25rem;--spacer-xs:0.5rem;--spacer-sm:0.75rem;--spacer-md:1rem;--spacer-lg:1.5rem;--spacer-xl:2rem;--spacer-2xl:3rem;--spacer-a-px:0px;--spacer-button-lg-px:var(--spacer-lg);--spacer-button-md-px:var(--spacer-lg);--spacer-button-sm-px:var(--spacer-md);--spacer-input-padding-left:0px;--spacer-input-padding-top:0px;--spacer-label-default:0px;--spacer-switch-input-active-pl:0px;--size-2xs:0.25rem;--size-xs:0.5rem;--size-sm:0.75rem;--size-md:1rem;--size-lg:1.5rem;--size-xl:2rem;--size-2xl:3rem;--size-3xl:4rem;--size-4xl:6rem;--size-5xl:8rem;--size-button-lg-h:3.375rem;--size-button-md-h:2.75rem;--size-button-sm-h:2.125rem;--size-button-xs-h:1.375rem;--size-switch-input-h:1.25rem;--size-switch-input-w:2rem;--line-sm:0.0625rem;--line-md:0.125rem;--line-lg:0.25rem;--line-a-focus:0px;--line-a-outline-moz:0.0625rem;--line-a-outline-wb:0.3125rem;--line-button-lg-border:0.0625rem;--line-button-md-border:0.0625rem;--line-button-sm-border:0.0625rem;--line-button-xs-border:0.0625rem;--line-button-border-activated:0.0625rem;--line-input-border:var(--line-sm);--radius-sm:0.25rem;--radius-lg:2rem;--radius-full:624.9375rem;--radius-accordion-size:var(--radius-sm);--font-10-15-bold:normal 700 0.625rem/0.9375rem var(--font-sans);--font-button-lg:normal 700 1.125rem/1.375rem var(--font-sans);--font-button-md:normal 700 1rem/1.25rem var(--font-sans);--font-button-sm:normal 700 0.875rem/1.125rem var(--font-sans);--font-button-xs:normal 700 0.75rem/0.875rem var(--font-sans);--font-label-default:var(--font-10-15-bold);--misc-accordion-border:1px solid var(--color-tone-5);--misc-accordion-open-list-style-type:disclosure-open;--misc-accordion-closed-list-style-type:disclosure-closed;--misc-divider-margin:0.5rem auto;--misc-label-text-transform:uppercase;--misc-label-letter-spacing:0.5px;--color-primary-visited:#609;--color-primary-background:#24a0ed;--color-primary-background-hover:#006cbf;--color-danger-content:#ea0027;--color-success-content:#46d160;--color-global-black:#000;--color-global-white:#fff;--color-global-orangered:#d93a00;--color-global-alienblue:#0079d3;--color-global-darkblue:#1d2535;--color-tone-1:#1a1a1b;--color-tone-2:#6a6d6f;--color-tone-3:#878a8c;--color-tone-4:#d3d6da;--color-tone-5:#edeff1;--color-tone-6:#f6f7f8;--color-tone-7:#fff;--color-action-primary:var(--color-primary-background);--color-action-secondary:var(--color-primary-background-hover);--color-action-upvote:var(--color-global-orangered);--color-action-downvote:#7193ff;--color-alert-positive:var(--color-success-content);--color-alert-negative:var(--color-danger-content);--color-alert-caution:#ffb000;--color-identity-admin:var(--color-global-orangered);--color-identity-moderator:#46d160;--color-identity-self:#0dd3bb;--color-identity-coins:#ddbd37;--color-category-live:var(--color-global-orangered);--color-category-nsfw:#ff3881;--color-category-spoiler:var(--color-tone-1);--color-ui-canvas:var(--color-tone-5);--color-ui-modalbackground:var(--color-tone-7);--color-opacity-highlight:linear-gradient(rgba(0,108,191,0.10196078431372549),var(--color-tone-6));--color-opacity-08:rgba(26,26,27,0.0784313725490196);--color-opacity-50:rgba(0,0,0,0.5019607843137255);--color-scrim:rgba(26,26,27,0.30196078431372547);--color-a-default:var(--color-primary-background-hover);--color-a-hover:var(--color-primary-background-hover);--color-a-visited:var(--color-primary-background-hover);--color-button-overlay-focus:hsla(0,0%,100%,0.10196078431372549);--color-button-overlay-active:rgba(0,0,0,0.0784313725490196);--color-button-primary-background-hover:var(--color-primary-background);--color-button-primary-background-disabled:var(--color-tone-6);--color-button-primary-border-hover:transparent;--color-button-primary-border-active:transparent;--color-button-primary-border-activated:transparent;--color-button-primary-border-disabled:transparent;--color-button-primary-text-disabled:var(--color-tone-2);--color-button-secondary-background:transparent;--color-button-secondary-background-focus:transparent;--color-button-secondary-background-hover:transparent;--color-button-secondary-background-disabled:var(--color-tone-6);--color-button-secondary-background-activated:transparent;--color-button-secondary-border:var(--color-primary-background-hover);--color-button-secondary-border-hover:var(--color-primary-background-hover);--color-button-secondary-border-active:var(--color-primary-background-hover);--color-button-secondary-border-activated:var(--color-primary-background-hover);--color-button-secondary-border-disabled:var(--color-tone-2);--color-button-secondary-text:var(--color-primary-background-hover);--color-button-secondary-text-disabled:var(--color-tone-2);--color-button-secondary-text-activated:var(--color-button-secondary-text);--color-button-tertiary-background:var(--color-tone-6);--color-button-tertiary-background-focus:var(--color-tone-6);--color-button-tertiary-background-hover:var(--color-tone-6);--color-button-tertiary-background-disabled:var(--color-tone-6);--color-button-tertiary-background-activated:var(--color-tone-6);--color-button-tertiary-border-hover:transparent;--color-button-tertiary-border-active:transparent;--color-button-tertiary-text:var(--color-primary-background-hover);--color-button-tertiary-text-disabled:var(--color-tone-2);--color-button-tertiary-text-activated:var(--color-primary-background-hover);--color-button-plain-background-hover:transparent;--color-button-plain-background-disabled:var(--color-tone-7);--color-button-plain-background-activated:transparent;--color-button-plain-border-hover:transparent;--color-button-plain-border-active:transparent;--color-button-plain-text:var(--color-primary-background-hover);--color-button-plain-text-disabled:var(--color-tone-2);--color-button-plain-text-activated:var(--color-primary-background-hover);--color-divider-default:var(--color-tone-5);--color-input-default:var(--color-tone-6);--color-input-hover:var(--color-primary-background-hover);--color-input-border:var(--color-tone-5);--color-input-text:var(--color-tone-1);--color-input-helper-text:var(--color-tone-1);--color-label-default:var(--color-tone-1);--color-switch-input-background-default:var(--color-tone-3);--color-switch-input-background-checked:var(--color-global-alienblue);--color-switch-input-background-disabled:var(--color-tone-6);--color-switch-input-background-checked-disabled:var(--color-tone-5);--color-switch-input-background-hover:var(--color-tone-3);--color-switch-input-background-checked-hover:var(--color-global-alienblue);--elevation-xs:0 0.0625rem 0.125rem 0 rgba(0,0,0,0.25098039215686274);--elevation-sm:0 0.0625rem 0.25rem 0 rgba(0,0,0,0.14901960784313725),0 0.25rem 0.25rem 0 rgba(0,0,0,0.14901960784313725);--elevation-md:0 0.25rem 0.5rem 0 rgba(0,0,0,0.10196078431372549),0 0.375rem 0.75rem 0 rgba(0,0,0,0.25098039215686274);--elevation-lg:0 0.75rem 0.75rem 0 rgba(0,0,0,0.14901960784313725),0 1rem 2rem 0 rgba(0,0,0,0.25098039215686274);--elevation-focus-ring:0 0 0 0.25rem var(--color-global-alienblue);--font-sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol",sans-serif;--font-mono:Noto Mono,Menlo,Monaco,Consolas,monospace;--font-title-h0:normal 500 1.625rem/2rem var(--font-sans);--font-title-h1:normal 500 1.375rem/1.625rem var(--font-sans);--font-title-h2:normal 500 1.25rem/1.5rem var(--font-sans);--font-title-h3:normal 500 1.125rem/1.375rem var(--font-sans);--font-title-h4:normal 500 1rem/1.25rem var(--font-sans);--font-title-h5:normal 500 0.875rem/1.125rem var(--font-sans);--font-title-h6:normal 500 0.75rem/1rem var(--font-sans);--font-body:0.875rem;--font-small:0.75rem;--font-code:0.875rem;--font-subheading:0.75rem;--font-label:0.625rem;--font-button-b1:normal bold 1.125rem/1.375rem var(--font-sans);--font-button-b2:normal bold 1rem/1.25rem var(--font-sans);--font-button-b3:normal bold 0.875rem/1.125rem var(--font-sans);--font-button-b4:normal bold 0.75rem/0.875rem var(--font-sans);--color-gradient-orangeyellow:linear-gradient(89.94deg,#ec0623,#ff8717);--color-gradient-bluepink:linear-gradient(89.94deg,#51b9ff,#7785ff 52.6%,#b279ff 73.96%,#ff81ed);--boxshadow-modal:0 2px 15px rgba(26,26,27,0.3);--boxshadow-navigation:0 4px 14px rgba(0,0,0,0.1);--boxshadow-tooltip:0 1px 4px rgba(0,0,0,0.15),0 4px 4px rgba(0,0,0,0.15);color-scheme:light}.theme-light dialog::-webkit-backdrop,:root dialog::-webkit-backdrop{--color-dialog-background:rgba(0,0,0,0.5019607843137255)}.theme-light dialog::backdrop,:root dialog::backdrop{--color-dialog-background:rgba(0,0,0,0.5019607843137255)}@media (prefers-color-scheme:dark){:root:not(.theme-light){--color-primary-visited:#c58af9;--color-primary-background:#006cbf;--color-primary-background-hover:#24a0ed;--color-tone-1:#d7dadc;--color-tone-2:#818384;--color-tone-3:#565758;--color-tone-4:#3a3a3c;--color-tone-5:#272729;--color-tone-6:#1a1a1b;--color-tone-7:#121213;--color-identity-coins:#ffe600;--color-ui-canvas:#050505;--color-ui-modalbackground:var(--color-tone-6);--color-opacity-50:rgba(215,218,220,0.5019607843137255);--color-scrim:rgba(0,0,0,0.30196078431372547);--elevation-xs:0 0.0625rem 0.125rem 0 rgba(0,0,0,0.6705882352941176);--elevation-sm:0 0.0625rem 0.25rem 0 rgba(0,0,0,0.32941176470588235),0 0.25rem 0.25rem 0 rgba(0,0,0,0.32941176470588235);--elevation-md:0 0.25rem 0.5rem 0 rgba(0,0,0,0.2),0 0.375rem 0.75rem 0 rgba(0,0,0,0.5019607843137255);--elevation-lg:0 0.75rem 0.75rem 0 rgba(0,0,0,0.2),0 1rem 2rem 0 rgba(0,0,0,0.5019607843137255);--boxshadow-modal:0 2px 15px rgba(0,0,0,0.3);--boxshadow-tooltip:0 1px 4px rgba(0,0,0,0.33),0 4px 4px rgba(0,0,0,0.33);color-scheme:dark}:root:not(.theme-light) dialog::-webkit-backdrop{--color-dialog-background:rgba(215,218,220,0.5019607843137255)}:root:not(.theme-light) dialog::backdrop{--color-dialog-background:rgba(215,218,220,0.5019607843137255)}}.theme-dark{--color-primary-visited:#c58af9;--color-primary-background:#006cbf;--color-primary-background-hover:#24a0ed;--color-tone-1:#d7dadc;--color-tone-2:#818384;--color-tone-3:#565758;--color-tone-4:#3a3a3c;--color-tone-5:#272729;--color-tone-6:#1a1a1b;--color-tone-7:#121213;--color-identity-coins:#ffe600;--color-ui-canvas:#050505;--color-ui-modalbackground:var(--color-tone-6);--color-opacity-50:rgba(215,218,220,0.5019607843137255);--color-scrim:rgba(0,0,0,0.30196078431372547);--elevation-xs:0 0.0625rem 0.125rem 0 rgba(0,0,0,0.6705882352941176);--elevation-sm:0 0.0625rem 0.25rem 0 rgba(0,0,0,0.32941176470588235),0 0.25rem 0.25rem 0 rgba(0,0,0,0.32941176470588235);--elevation-md:0 0.25rem 0.5rem 0 rgba(0,0,0,0.2),0 0.375rem 0.75rem 0 rgba(0,0,0,0.5019607843137255);--elevation-lg:0 0.75rem 0.75rem 0 rgba(0,0,0,0.2),0 1rem 2rem 0 rgba(0,0,0,0.5019607843137255);--boxshadow-modal:0 2px 15px rgba(0,0,0,0.3);--boxshadow-tooltip:0 1px 4px rgba(0,0,0,0.33),0 4px 4px rgba(0,0,0,0.33);color-scheme:dark}.theme-dark dialog::-webkit-backdrop{--color-dialog-background:rgba(215,218,220,0.5019607843137255)}.theme-dark dialog::backdrop{--color-dialog-background:rgba(215,218,220,0.5019607843137255)}.theme-beta,.theme-light.theme-beta{--spacer-a-px:0.125rem;--spacer-button-lg-px:var(--spacer-md);--spacer-button-md-px:var(--spacer-md);--spacer-button-sm-px:var(--spacer-sm);--spacer-input-padding-left:var(--spacer-md);--spacer-input-padding-top:var(--spacer-2xs);--spacer-label-default:var(--spacer-md);--spacer-switch-input-active-pl:var(--spacer-xs);--size-banner-height:var(--size-rem40);--size-button-lg-h:var(--size-2xl);--size-button-md-h:2.5rem;--size-button-sm-h:var(--size-xl);--size-button-xs-h:var(--size-xl);--size-switch-input-h:var(--size-xl);--size-switch-input-w:var(--size-2xl);--line-a-focus:var(--line-md);--line-a-outline-moz:0px;--line-a-outline-wb:0px;--line-button-lg-border:var(--line-sm);--line-button-md-border:var(--line-sm);--line-button-sm-border:var(--line-sm);--line-button-xs-border:var(--line-sm);--line-button-border-activated:var(--line-lg);--line-input-border:var(--line-lg);--radius-accordion-size:0px;--font-10:normal undefined null/null var(--font-sans);--font-12:normal undefined null/null var(--font-sans);--font-14:normal undefined null/null var(--font-sans);--font-16:normal undefined null/null var(--font-sans);--font-18:normal undefined null/null var(--font-sans);--font-20:normal undefined null/null var(--font-sans);--font-24:normal undefined null/null var(--font-sans);--font-32:normal undefined null/null var(--font-sans);--font-48:normal undefined null/null var(--font-sans);--font-64:normal undefined null/null var(--font-sans);--font-title-h0:var(--font-64);--font-title-h1:var(--font-32);--font-title-h2:var(--font-24);--font-title-h3:var(--font-18);--font-title-h4:var(--font-16);--font-title-h5:var(--font-14);--font-title-h6:var(--font-12);--font-14-20-regular:normal 400 0.875rem/1.25rem var(--font-sans);--font-14-20-semibold:normal 600 0.875rem/1.25rem var(--font-sans);--font-16-20-regular:normal 400 1rem/1.25rem var(--font-sans);--font-12-16-regular:normal 400 0.75rem/1rem var(--font-sans);--font-12-16-semibold:normal 600 0.75rem/1rem var(--font-sans);--font-button-lg:var(--font-14-20-semibold);--font-button-md:var(--font-14-20-semibold);--font-button-sm:var(--font-12-16-semibold);--font-label-default:var(--font-12-16-regular);--misc-accordion-border:0;--misc-accordion-open-list-style-type:none;--misc-accordion-closed-list-style-type:none;--misc-divider-margin:0;--misc-label-text-transform:capitalize;--misc-label-letter-spacing:initial;--blur-sm:0.25rem;--blur-normal:0.5rem;--blur-md:0.75rem;--blur-lg:1rem;--blur-xl:1.5rem;--blur-2xl:2.5rem;--blur-3xl:4rem;--color-pizzaRed:#ef5350;--color-global-brand-orangered:#ff4500;--color-global-focus:#47b0db;--color-interactive-content-disabled:rgba(0,0,0,0.25098039215686274);--color-interactive-background-disabled:rgba(0,0,0,0.050980392156862744);--color-interactive-pressed:rgba(0,0,0,0.1607843137254902);--color-neutral-content:#2a3c42;--color-neutral-content-disabled:#d6d6d6;--color-neutral-content-weak:#576f76;--color-neutral-content-strong:#0f1a1c;--color-neutral-background:#fff;--color-neutral-background-selected:#eaedef;--color-neutral-background-weak:#f9fafa;--color-neutral-background-medium:#f8f8f8;--color-neutral-background-strong:#fff;--color-neutral-background-hover:#f2f4f5;--color-neutral-border:rgba(0,0,0,0.2);--color-neutral-border-medium:rgba(0,0,0,0.5019607843137255);--color-neutral-border-weak:rgba(0,0,0,0.10196078431372549);--color-neutral-border-strong:#0f1a1c;--color-primary:#0045ac;--color-primary-hover:#003584;--color-primary-visited:#8700b5;--color-primary-onBackground:#fff;--color-primary-onBackground-selected:#fff;--color-primary-background:#0045ac;--color-primary-background-hover:#003584;--color-primary-background-selected:#00255d;--color-secondary:#0f1a1c;--color-secondary-hover:#000;--color-secondary-weak:#576f76;--color-secondary-onBackground:#000;--color-secondary-background:#eaedef;--color-secondary-background-hover:#e2e7e9;--color-secondary-background-selected:#d2dadd;--color-danger-background:#eb001f;--color-danger-background-disabled:#ffccd2;--color-danger-background-hover:#a50016;--color-danger-content:#a50016;--color-danger-content-hover:#7e0011;--color-danger-content-default:#fff;--color-brand-background:#d93a00;--color-brand-onBackground:#fff;--color-brand-background-hover:#962900;--color-media-background:rgba(0,0,0,0.6);--color-media-onbackground:#fff;--color-media-background-hover:rgba(0,0,0,0.8);--color-media-onbackground-disabled:hsla(0,0%,100%,0.25098039215686274);--color-media-border-selected:#fff;--color-media-background-selected:rgba(0,0,0,0.8);--color-success-content:#0a6000;--color-success-hover:#084a00;--color-success-onBackground:#fff;--color-success-background:#0e8a00;--color-success-background-hover:#0a6000;--color-warning-content:#665505;--color-warning-content-hover:#504104;--color-warning-onBackground:#000;--color-warning-background:#dbaf00;--color-warning-background-hover:#8f7407;--color-upvote-content:#962900;--color-upvote-content-weak:var(--color-global-brand-orangered);--color-upvote-disabled:rgba(150,41,0,0.30196078431372547);--color-upvote-onBackground:#fff;--color-upvote-background:#d93a00;--color-upvote-background-hover:#962900;--color-upvote-background-disabled:rgba(217,58,0,0.30196078431372547);--color-downvote-content:#453bb5;--color-downvote-content-weak:#6a5cff;--color-downvote-disabled:rgba(69,59,181,0.30196078431372547);--color-downvote-onBackground:#fff;--color-downvote-background:#6a5cff;--color-downvote-background-hover:#453bb5;--color-downvote-background-disabled:rgba(106,92,255,0.30196078431372547);--color-brand-gradient-default:linear-gradient(180deg,#d93a00,#db3b00 30%,#962900);--color-brand-gradient-default-highlight:linear-gradient(258deg,rgba(219,63,0,0) 80%,#d93a00);--color-brand-gradient-hover:linear-gradient(180deg,#e23d00 15%,#cb3600 49%,#b43000);--color-brand-gradient-hover-highlight:linear-gradient(323deg,rgba(203,54,0,0) 65%,#cb3600);--color-brand-gradient-active:linear-gradient(180deg,#cd3700,#db3b00 68%,#d93a00);--color-brand-gradient-active-highlight:linear-gradient(83deg,rgba(219,63,0,0) 80%,#d93a00);--color-gradient-media:linear-gradient(180deg,transparent,rgba(0,0,0,0.5411764705882353) 60%,rgba(0,0,0,0.6));--color-gradient-media-strong:linear-gradient(180deg,transparent,rgba(0,0,0,0.8) 60%,rgba(0,0,0,0.9019607843137255));--color-transparent-background-hover:rgba(130,149,155,0.10196078431372549);--color-global-black:#000;--color-global-white:#fff;--color-global-orangered:#d93a00;--color-global-alienblue:#1870f4;--color-global-darkblue:#131f23;--color-tone-1:#131313;--color-tone-2:#434343;--color-tone-3:#acacac;--color-tone-4:#e4e4e4;--color-tone-5:#f2f2f2;--color-tone-6:#f8f8f8;--color-tone-7:#fff;--color-action-upvote:#d93a00;--color-action-downvote:#6a5cff;--color-alert-caution:#8f7407;--color-identity-admin:#d93a00;--color-identity-moderator:#0e8a00;--color-identity-self:#008675;--color-identity-coins:#dbaf00;--color-category-live:#d93a00;--color-category-nsfw:#e00096;--color-category-spoiler:var(--color-tone-1);--color-ui-canvas:var(--color-tone-5);--color-ui-modalbackground:var(--color-neutral-background-strong);--color-avatar-gradient:linear-gradient(0deg,#d2dadd,#fff 75%);--color-opacity-highlight:linear-gradient(rgba(0,37,93,0.10196078431372549),var(--color-tone-6));--color-opacity-08:rgba(19,19,19,0.0784313725490196);--color-opacity-50:rgba(0,0,0,0.5019607843137255);--color-scrim:rgba(0,0,0,0.6);--color-scrim-strong:rgba(0,0,0,0.8);--color-scrim-gradient:linear-gradient(180deg,transparent,rgba(0,0,0,0.5411764705882353) 60%,rgba(0,0,0,0.6));--color-online:#55bd46;--color-a-default:var(--color-primary);--color-a-hover:var(--color-primary-hover);--color-a-visited:var(--color-primary-visited);--color-banner-plain:var(--color-neutral-background-strong);--color-banner-plain-inverted:var(--color-neutral-content-strong);--color-banner-error:var(--color-danger-background);--color-banner-caution:var(--color-warning-background);--color-banner-success:var(--color-success-background);--color-banner-brand:var(--color-brand-background);--color-banner-plain-text:var(--color-neutral-content);--color-banner-plain-inverted-text:var(--color-neutral-background-weak);--color-banner-error-text:var(--color-danger-onBackground);--color-banner-caution-text:var(--color-warning-onBackground);--color-banner-caution-hover:var(--color-warning-background-hover);--color-banner-success-text:var(--color-success-onBackground);--color-banner-brand-text:var(--color-brand-onBackground);--color-button-overlay-focus:transparent;--color-button-overlay-active:transparent;--color-button-border-width:tomato;--color-button-border-width-activated:tomato;--color-button-primary-background-hover:var(--color-primary-background-hover);--color-button-primary-background-activated:var(--color-primary-background-selected);--color-button-primary-background-disabled:var(--color-interactive-background-disabled);--color-button-primary-border-hover:var(--color-primary-background);--color-button-primary-border-active:var(--color-primary-background-hover);--color-button-primary-text-disabled:var(--color-interactive-content-disabled);--color-button-primary-text-activated:var(--color-primary-onBackground-selected);--color-button-secondary-background:var(--color-secondary-background);--color-button-secondary-background-focus:var(--color-secondary-background);--color-button-secondary-background-hover:var(--color-secondary-background-hover);--color-button-secondary-background-disabled:var(--color-interactive-background-disabled);--color-button-secondary-background-activated:var(--color-secondary-background-selected);--color-button-secondary-border:transparent;--color-button-secondary-border-hover:var(--color-secondary-background);--color-button-secondary-border-active:var(--color-secondary-background-hover);--color-button-secondary-border-activated:transparent;--color-button-secondary-border-disabled:transparent;--color-button-secondary-text:var(--color-neutral-content-strong);--color-button-secondary-text-disabled:var(--color-interactive-content-disabled);--color-button-secondary-text-activated:var(--color-secondary-onBackground);--color-button-tertiary-background:transparent;--color-button-tertiary-background-focus:transparent;--color-button-tertiary-background-hover:var(--color-secondary-background-hover);--color-button-tertiary-background-disabled:transparent;--color-button-tertiary-background-activated:var(--color-neutral-content);--color-button-tertiary-border-hover:var(--color-secondary-background);--color-button-tertiary-border-active:var(--color-secondary-background-hover);--color-button-tertiary-text:var(--color-neutral-content-strong);--color-button-tertiary-text-disabled:var(--color-neutral-content-disabled);--color-button-tertiary-text-activated:var(--color-neutral-background);--color-button-plain-background-hover:var(--color-secondary-background-hover);--color-button-plain-background-disabled:transparent;--color-button-plain-background-activated:var(--color-secondary-background-selected);--color-button-plain-border-hover:var(--color-secondary-background);--color-button-plain-border-active:var(--color-secondary-background-hover);--color-button-plain-text:var(--color-neutral-content-strong);--color-button-plain-text-disabled:var(--color-interactive-content-disabled);--color-button-plain-text-activated:var(--color-secondary-onBackground);--color-button-primary-border-activated:var(--color-primary-background);--color-button-plain-inverted-background-activated:var(--color-neutral-content);--color-button-plain-inverted-text-activated:var(--color-neutral-background);--color-button-media-border-color-activated:var(--color-media-border-selected);--color-divider-default:var(--color-neutral-border);--color-input-default:var(--color-secondary-background);--color-input-hover:var(--color-secondary-background-hover);--color-input-border:transparent;--color-input-text:var(--color-neutral-content-strong);--color-input-helper-text:var(--color-neutral-content-weak);--color-label-default:var(--color-neutral-content-weak);--color-shimmer-background:rgba(0,0,0,0.03137254901960784);--color-shimmer-gradient-overlay:linear-gradient(90deg,transparent,rgba(0,0,0,0.0196078431372549) 20%,rgba(0,0,0,0.058823529411764705) 50%,rgba(0,0,0,0.03137254901960784) 70%,transparent);--color-switch-input-background-pressed-scrim:var(--color-interactive-pressed);--color-switch-input-background-handle:var(--color-global-white);--color-switch-input-background-handle-disabled:var(--color-secondary-background);--color-switch-input-background-default:var(--color-secondary-background);--color-switch-input-background-default-hover:var(--color-secondary-background-hover);--color-switch-input-background-default-disabled:var(--color-interactive-background-disabled);--color-switch-input-background-checked:var(--color-primary-background);--color-switch-input-background-checked-hover:var(--color-primary-background-hover);--color-switch-input-background-checked-disabled:var(--color-interactive-content-disabled);--color-tooltip-bg-neutral:var(--color-neutral-background-strong);--color-tooltip-text-neutral:var(--color-neutral-content);--color-tooltip-bg-inverted:var(--color-neutral-content);--color-tooltip-text-inverted:var(--color-neutral-background);--color-tooltip-bg-primary:var(--color-primary-background);--color-tooltip-text-primary:var(--color-primary-onBackground);--elevation-sm-inset:inset 0 0.0625rem 0.125rem 0 rgba(0,0,0,0.12941176470588237);--elevation-button-focus:var(--elevation-focus-ring);--elevation-switch-input-default-inset:var(--elevation-sm-inset)}@media (prefers-color-scheme:dark){:root:not(.theme-light).theme-beta,:root:not(.theme-light) .theme-beta{--color-pizzaRed:#c62828;--color-global-brand-orangered:#ff4500;--color-global-focus:#007fae;--color-interactive-content-disabled:hsla(0,0%,100%,0.25098039215686274);--color-interactive-background-disabled:hsla(0,0%,100%,0.050980392156862744);--color-interactive-pressed:hsla(0,0%,100%,0.1607843137254902);--color-neutral-content:#b8c5c9;--color-neutral-content-disabled:#303030;--color-neutral-content-weak:#82959b;--color-neutral-content-strong:#f2f4f5;--color-neutral-background:#0b1416;--color-neutral-background-selected:#1a282d;--color-neutral-background-weak:#04090a;--color-neutral-background-medium:#131313;--color-neutral-background-strong:#0f1a1c;--color-neutral-background-hover:#131f23;--color-neutral-border:hsla(0,0%,100%,0.2);--color-neutral-border-medium:hsla(0,0%,100%,0.5019607843137255);--color-neutral-border-weak:hsla(0,0%,100%,0.10196078431372549);--color-neutral-border-strong:#f2f4f5;--color-primary:#629fff;--color-primary-hover:#a7ccff;--color-primary-visited:#d55eff;--color-primary-background:#0045ac;--color-primary-background-hover:#1870f4;--color-primary-background-selected:#629fff;--color-primary-onBackground:#fff;--color-primary-onBackground-selected:#000;--color-secondary:#f2f4f5;--color-secondary-hover:#fff;--color-secondary-weak:#82959b;--color-secondary-onBackground:#fff;--color-secondary-background:#1a282d;--color-secondary-background-hover:#223237;--color-secondary-background-selected:#33464c;--color-danger-background:#a50016;--color-danger-background-disabled:#3a0008;--color-danger-background-hover:#eb001f;--color-danger-content:#ff6e80;--color-danger-content-hover:#ffadb8;--color-success-content:#55bd46;--color-success-hover:#a3e398;--color-success-onBackground:#fff;--color-success-background:#0a6000;--color-success-background-hover:#0e8a00;--color-warning-content:#dbaf00;--color-warning-content-hover:#fadb61;--color-warning-onBackground:#000;--color-warning-background:#dbaf00;--color-warning-background-hover:#fadb61;--color-upvote-content:#fe7c53;--color-upvote-content-weak:var(--color-global-brand-orangered);--color-upvote-disabled:rgba(254,124,83,0.30196078431372547);--color-upvote-onBackground:#fff;--color-upvote-background:#d93a00;--color-upvote-background-hover:#962900;--color-upvote-background-disabled:rgba(217,58,0,0.30196078431372547);--color-downvote-content:#988eff;--color-downvote-content-weak:#6a5cff;--color-downvote-disabled:rgba(152,142,255,0.30196078431372547);--color-downvote-onBackground:#fff;--color-downvote-background:#453bb5;--color-downvote-background-hover:#453bb5;--color-downvote-background-disabled:rgba(106,92,255,0.30196078431372547);--color-tone-1:#f2f2f2;--color-tone-2:#acacac;--color-tone-3:#434343;--color-tone-4:#303030;--color-tone-5:#1e1e1e;--color-tone-6:#131313;--color-tone-7:#080808;--color-ui-canvas:#080808;--color-ui-modalbackground:var(--color-neutral-background-strong);--color-avatar-gradient:linear-gradient(0deg,#2a3c42,#0b1416 75%);--color-transparent-background-hover:rgba(102,122,128,0.10196078431372549);--color-opacity-50:hsla(0,0%,94.9%,0.5019607843137255);--color-online:#55bd46;--color-button-primary-border-activated:transparent;--color-button-plain-inverted-activated-text:var(--color-neutral-background);--color-shimmer-background:hsla(0,0%,100%,0.03137254901960784);--color-shimmer-gradient-overlay:linear-gradient(90deg,hsla(0,0%,100%,0),hsla(0,0%,100%,0.0196078431372549) 20%,hsla(0,0%,100%,0.058823529411764705) 50%,hsla(0,0%,100%,0.03137254901960784) 70%,hsla(0,0%,100%,0))}}.theme-dark.theme-beta,.theme-dark .theme-beta{--color-pizzaRed:#c62828;--color-global-brand-orangered:#ff4500;--color-global-focus:#007fae;--color-interactive-content-disabled:hsla(0,0%,100%,0.25098039215686274);--color-interactive-background-disabled:hsla(0,0%,100%,0.050980392156862744);--color-interactive-pressed:hsla(0,0%,100%,0.1607843137254902);--color-neutral-content:#b8c5c9;--color-neutral-content-disabled:#303030;--color-neutral-content-weak:#82959b;--color-neutral-content-strong:#f2f4f5;--color-neutral-background:#0b1416;--color-neutral-background-selected:#1a282d;--color-neutral-background-weak:#04090a;--color-neutral-background-medium:#131313;--color-neutral-background-strong:#0f1a1c;--color-neutral-background-hover:#131f23;--color-neutral-border:hsla(0,0%,100%,0.2);--color-neutral-border-medium:hsla(0,0%,100%,0.5019607843137255);--color-neutral-border-weak:hsla(0,0%,100%,0.10196078431372549);--color-neutral-border-strong:#f2f4f5;--color-primary:#629fff;--color-primary-hover:#a7ccff;--color-primary-visited:#d55eff;--color-primary-background:#0045ac;--color-primary-background-hover:#1870f4;--color-primary-background-selected:#629fff;--color-primary-onBackground:#fff;--color-primary-onBackground-selected:#000;--color-secondary:#f2f4f5;--color-secondary-hover:#fff;--color-secondary-weak:#82959b;--color-secondary-onBackground:#fff;--color-secondary-background:#1a282d;--color-secondary-background-hover:#223237;--color-secondary-background-selected:#33464c;--color-danger-background:#a50016;--color-danger-background-disabled:#3a0008;--color-danger-background-hover:#eb001f;--color-danger-content:#ff6e80;--color-danger-content-hover:#ffadb8;--color-success-content:#55bd46;--color-success-hover:#a3e398;--color-success-onBackground:#fff;--color-success-background:#0a6000;--color-success-background-hover:#0e8a00;--color-warning-content:#dbaf00;--color-warning-content-hover:#fadb61;--color-warning-onBackground:#000;--color-warning-background:#dbaf00;--color-warning-background-hover:#fadb61;--color-upvote-content:#fe7c53;--color-upvote-content-weak:var(--color-global-brand-orangered);--color-upvote-disabled:rgba(254,124,83,0.30196078431372547);--color-upvote-onBackground:#fff;--color-upvote-background:#d93a00;--color-upvote-background-hover:#962900;--color-upvote-background-disabled:rgba(217,58,0,0.30196078431372547);--color-downvote-content:#988eff;--color-downvote-content-weak:#6a5cff;--color-downvote-disabled:rgba(152,142,255,0.30196078431372547);--color-downvote-onBackground:#fff;--color-downvote-background:#453bb5;--color-downvote-background-hover:#453bb5;--color-downvote-background-disabled:rgba(106,92,255,0.30196078431372547);--color-tone-1:#f2f2f2;--color-tone-2:#acacac;--color-tone-3:#434343;--color-tone-4:#303030;--color-tone-5:#1e1e1e;--color-tone-6:#131313;--color-tone-7:#080808;--color-ui-canvas:#080808;--color-ui-modalbackground:var(--color-neutral-background-strong);--color-avatar-gradient:linear-gradient(0deg,#2a3c42,#0b1416 75%);--color-transparent-background-hover:rgba(102,122,128,0.10196078431372549);--color-opacity-50:hsla(0,0%,94.9%,0.5019607843137255);--color-online:#55bd46;--color-button-primary-border-activated:transparent;--color-button-plain-inverted-activated-text:var(--color-neutral-background);--color-shimmer-background:hsla(0,0%,100%,0.03137254901960784);--color-shimmer-gradient-overlay:linear-gradient(90deg,hsla(0,0%,100%,0),hsla(0,0%,100%,0.0196078431372549) 20%,hsla(0,0%,100%,0.058823529411764705) 50%,hsla(0,0%,100%,0.03137254901960784) 70%,hsla(0,0%,100%,0))}

._1VP69d9lk-Wk9zokOaylL{--background:unset;--canvas:unset;background-color:var(--background);min-height:calc(100vh - 48px)}._1VP69d9lk-Wk9zokOaylL:after{content:" ";position:fixed;top:100%;left:0;right:0;height:200px;background-color:var(--canvas)}.KDkLHOpoLUZvoYQUBe9nF{min-height:calc(100vh - 56px)}
._25r3t_lrPF3M6zD2YkWvZU{height:100%;width:100%}._1ryinm9ofYAx_k9dpdCbpq{position:absolute;right:16px;top:16px}._14dkERGUnSwisNWFcFX-0T{height:20px;fill:grey;width:20px}._14dkERGUnSwisNWFcFX-0T._65PqClMblfoNGy-m9_49f{height:14px;fill:#878a8c;width:14px}
._1FR0eEUi22u9saLEyWWJGS{position:relative}._3YoS4yX_XBXWbj-eYFW6MS{-ms-flex-align:center;align-items:center;bottom:160px;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;height:8px;-ms-flex-pack:center;justify-content:center;left:0;position:absolute;right:0}._1mwHqJp51wXFI7rjTonkz5{background-color:#1a1a1b;border-radius:4px;height:4px;margin:0 4px;transition:margin .25s,height .25s,width .25s;width:4px}._2ol4vy2ml1IZ6lfT2n775g{height:8px;margin:0 2px;width:8px}._26qHHOV6EkP4whoc4ySt3l{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;height:100%;overflow:hidden;position:relative;width:100%}._2gs-hGAB6w3q4Gc8mSyG5Z{background-position:top;background-size:cover;cursor:pointer;height:100%}._2gs-hGAB6w3q4Gc8mSyG5Z.uAUBkt8dAygLJNIsiAmad{left:0;position:absolute;right:0;transition:opacity 1s;top:0}._2gs-hGAB6w3q4Gc8mSyG5Z._4S2XTVURHpoKNNEuKzJbH{-ms-flex-negative:0;flex-shrink:0;-ms-flex-positive:0;flex-grow:0;position:relative;transition:margin .25s}
._1DtVp1OCzoJt6rVu4kqyST{position:relative}._20m5B-2NHmUmXVUYC1gymo{-ms-flex-align:center;align-items:center;border-radius:60px;box-shadow:0 0 24px 0 rgba(0,0,0,.2);display:-ms-flexbox;display:flex;-ms-flex-flow:column nowrap;flex-flow:column nowrap;-ms-flex-pack:start;justify-content:flex-start;position:absolute}._20m5B-2NHmUmXVUYC1gymo._2jgq6Cm4n7c3NNl8VpFltS{height:555px;left:0;top:0;width:261px}._20m5B-2NHmUmXVUYC1gymo._2ocrsCliWP9UUmx5ZL374w{bottom:0;height:530px;right:0;width:266px}._1gqdyMEgD0pz6QBvVhgU7i._2jgq6Cm4n7c3NNl8VpFltS{height:476px;margin-top:41px;width:240px}._1gqdyMEgD0pz6QBvVhgU7i._2ocrsCliWP9UUmx5ZL374w{height:498px;margin-top:16px;width:232px}._3P_iHJEXRll3mWyuqNik3I{height:100%;left:1px;position:absolute}
._23C-3j-0TrSZn_NJT8fcwU{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row}._19_2-KUNWYbunHVuHaoY-a,.EzRsHBU9A06NEXZnsJyWI{font-size:12px;font-weight:500;line-height:16px;color:var(--newRedditTheme-metaText);text-decoration:none;text-transform:capitalize}.EzRsHBU9A06NEXZnsJyWI{font-weight:700;margin-right:16px}
._1uKZh7b1kZ-bLvlZ02RLL6{background-color:var(--newRedditTheme-field);box-sizing:border-box;-ms-flex-direction:column;flex-direction:column;height:100vh;-ms-flex-pack:justify;justify-content:space-between;margin-top:0;overflow:hidden;padding-bottom:80px;position:relative}._1uKZh7b1kZ-bLvlZ02RLL6,._1xH0LEH3NeL-Kz1FAMx9Vz{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;width:100%}._1xH0LEH3NeL-Kz1FAMx9Vz{-ms-flex-direction:row;flex-direction:row;margin:auto 0;padding-top:20px}._3UaPvIbppFSklSTg2aTFLl{-ms-flex:0 0 50%;flex:0 0 50%}._3UaPvIbppFSklSTg2aTFLl:first-child{margin-right:40px}._19dEFhHhbDgVJWuOq0KZlf{height:570px;margin-left:auto;width:440px}._2e0gx7j1Bc2qfAjI-3Tbio{height:426px;width:350px}._2e0gx7j1Bc2qfAjI-3Tbio.g5DNTyz0K4p8Qe1KemhqM{height:474px}.W6BMDJ-zjJbsEwxbpvU5r{--frontpagesignup-upsell-text-hover-color:inherit;color:var(--newRedditTheme-bodyText);fill:var(--newRedditTheme-bodyText)}.W6BMDJ-zjJbsEwxbpvU5r:hover{color:var(--frontpagesignup-upsell-text-hover-color);fill:var(--frontpagesignup-upsell-text-hover-color)}._1igwWwaemysS2mmPW8WZ2s{font-size:14px;font-weight:500;line-height:18px;display:block;text-align:center}._3PeYnzFZio-HxxDaqnOAE_{height:16px;margin:12px auto 0;width:16px}._1etyEGrcHpnkE1UMtQIjpV{bottom:20px;height:40px;-ms-flex-pack:center;justify-content:center;left:0;margin-top:auto;position:absolute;right:0}._3OBSZQIgZx2ksSzBQmYOeO{height:400px;width:400px}
._1vmueUAOJJg7fhS7wxztWa{fill:var(--newCommunityTheme-actionIcon)}
._21CrWSXdmd-ue61gDl6zRs,._1xT_z2uw_7yX0esEUZVFwf,._1NVucoiiTLKJiKzRTPVKaW{margin-right:10px}._21CrWSXdmd-ue61gDl6zRs{background-color:var(--newCommunityTheme-body);border-radius:2px}._1H6-wE3jxCdsIeXW5AMjj8{display:-ms-inline-flexbox;display:inline-flex;box-sizing:border-box;fill:#0079d3}._1H6-wE3jxCdsIeXW5AMjj8:focus,.-kceiAQn0jpWOpu7qZRjD:focus{outline-width:0}._1H6-wE3jxCdsIeXW5AMjj8:focus>.-kceiAQn0jpWOpu7qZRjD{outline:2px auto Highlight;outline:5px auto -webkit-focus-ring-color}.-kceiAQn0jpWOpu7qZRjD{display:-ms-inline-flexbox;display:inline-flex;-ms-flex-align:center;align-items:center}
._2jjk9b3mpveU6Vpam4kPBm{background:var(--newRedditTheme-line);border:none;display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;padding:16px}._2jjk9b3mpveU6Vpam4kPBm button{min-width:96px}._2jjk9b3mpveU6Vpam4kPBm ._1DUcff8CoMLomEzQZ1S6IX{margin-left:auto;display:-ms-flexbox;display:flex}._2jjk9b3mpveU6Vpam4kPBm ._2HCY4xCLt3RKVIgnkh0ZgW{color:var(--newRedditTheme-actionIcon);border-color:currentColor;margin:0 8px}._2jjk9b3mpveU6Vpam4kPBm .saAxhszfFnlBT8m48Quv9{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:unset;line-height:32px;text-transform:unset;color:var(--newRedditTheme-actionIcon)}._3dGLI85CRTmDAbSQrDiQZl{border:none;padding:16px}._2pIwiaNLf5jaTR1EK7Nx09{font-size:14px;font-weight:500;line-height:18px;color:var(--newCommunityTheme-bodyText)}
._1-nIsCaWhGBFN-L4ZHnbGp{background:#ff4500;border-radius:12px;box-shadow:0 0 0 2px var(--newCommunityTheme-body);box-sizing:border-box;color:#fff;font-size:10px;font-weight:700;height:16px;left:20px;line-height:16px;padding:0 4px;position:absolute;text-align:center;top:0;vertical-align:middle;min-width:16px;width:auto;z-index:1}._1-nIsCaWhGBFN-L4ZHnbGp._3FX9lCQKNdKXkfBiSWCjSb{height:8px;min-width:8px;margin-top:4px}
.FjkUHssa96HMV17_qcQt6{position:relative;max-height:150px;background-position:50%;background-size:cover;box-shadow:0 4px 21px var(--newRedditTheme-bodyTextAlpha20);border-radius:10px;margin-bottom:16px;font-family:IBMPlexSans,Arial,sans-serif;padding:16px;cursor:pointer}.FjkUHssa96HMV17_qcQt6,.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1{display:-ms-flexbox;display:flex}.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1{-ms-flex:1;flex:1;-ms-flex-direction:column;flex-direction:column}.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1 .ZtxCbLGmd-U6DH5-RsBJV{display:-ms-flexbox;display:flex;margin-bottom:8px}.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1 .ZtxCbLGmd-U6DH5-RsBJV ._2Iz2pxeBTmtn5cilveUdwj{font-family:Noto Sans,Arial,sans-serif;font-size:18px;font-weight:400;line-height:22px;font-family:inherit;font-weight:500;color:#fff}.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1 .ZtxCbLGmd-U6DH5-RsBJV ._3wZ9NKCStyQ9_XMz6jRbkL{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;height:34px;margin-right:5px}.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1 ._2GYO5AeH0SYqV0W_IYw7C_{display:-ms-flexbox;display:flex}.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1 ._2GYO5AeH0SYqV0W_IYw7C_ ._1Tw_Z3ZCizARHq8mDvXtJp{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px;white-space:pre-wrap;-ms-flex:1;flex:1;color:#fff}.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1 ._2GYO5AeH0SYqV0W_IYw7C_ ._3VFSVmukKEY-C06RJldU7n{width:48px;height:48px;background-position:50%;background-size:cover;border-radius:4px}.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1 ._45hSSzyMPM5pmBx74E25U{display:-ms-flexbox;display:flex;margin-top:12px}.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1 ._45hSSzyMPM5pmBx74E25U.aaIwLr1Mbi15Al1BCmB8w{margin-top:0}.FjkUHssa96HMV17_qcQt6 ._3xbx2cMOI83xtKSIZfzaeW,.FjkUHssa96HMV17_qcQt6 ._27ZWqn-n6gBKDTqLbt0uk1 ._45hSSzyMPM5pmBx74E25U ._1cOP2U6TmJgXE_lLuvdAk{color:#fff;margin-left:5px}.FjkUHssa96HMV17_qcQt6 ._3xbx2cMOI83xtKSIZfzaeW{position:absolute;right:12px}.FjkUHssa96HMV17_qcQt6 ._3xbx2cMOI83xtKSIZfzaeW ._3uR0NalufS44rp_5yMF15w{font-weight:600}.FjkUHssa96HMV17_qcQt6 ._3xbx2cMOI83xtKSIZfzaeW:hover{opacity:.9}.FjkUHssa96HMV17_qcQt6 ._3xbx2cMOI83xtKSIZfzaeW:hover:before{opacity:0}
._3vOO3WyD7yteL4Rr9E1i2y{text-decoration:underline}._34mO86zNIysmcISYIe8gVT{border-radius:10px;box-shadow:0 4px 21px var(--newRedditTheme-bodyTextAlpha20);color:#fff;padding:16px;margin-bottom:16px}.rh7yf_ejK6H75L6jZkb6C{-ms-flex-align:baseline;align-items:baseline;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-pack:justify;justify-content:space-between}.V_VLkmdSrXqz92-5vad5F{font-size:16px;font-weight:500;line-height:20px;margin-bottom:5px}._1vbdR0mal1nPuuTOZIemLg{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px}._34mO86zNIysmcISYIe8gVT .-Fi_Lr4OQ6XfCIiufmgxa{color:#fff}._34mO86zNIysmcISYIe8gVT .-Fi_Lr4OQ6XfCIiufmgxa:hover{opacity:.9}._34mO86zNIysmcISYIe8gVT .-Fi_Lr4OQ6XfCIiufmgxa:hover:before{opacity:0}._1a9VL63O5el1YN7RuPoDLy{display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row}._1a9VL63O5el1YN7RuPoDLy ._1mejKTw8yWGmudymV6GufX{padding:4px 20px}._1a9VL63O5el1YN7RuPoDLy ._1mR2YFl21PdJDX9T7ykA7c{background-color:#fff;color:#0079d3;margin-right:5px}._3QWgBcfZuqQ6TlxZa6uYkS{background:linear-gradient(90deg,#ec0623,#ff8717)}._3IIpKn1IlCXgko4sLMEie1{background:linear-gradient(90deg,#3690ea 12.05%,#94b3ff 87.85%)}._3IIpKn1IlCXgko4sLMEie1 .rh7yf_ejK6H75L6jZkb6C{margin-bottom:10px}.GLgkxGZkPymWBWeRISXBe{background:linear-gradient(90deg,#3690ea 12.05%,#94b3ff 87.85%)}.GLgkxGZkPymWBWeRISXBe .V_VLkmdSrXqz92-5vad5F{font-size:14px;font-weight:500;line-height:18px}.GLgkxGZkPymWBWeRISXBe ._1vbdR0mal1nPuuTOZIemLg{margin-bottom:15px}._2Ggqgl_RyXu2U-mPYZSaCk{display:-ms-flexbox;display:flex}._2C3YUpN8pGzseZOBK0tl0I{margin-right:auto}._2BTQI8_1TIwwfdecOP_j6o{color:var(--newRedditTheme-bodyText)}._2BTQI8_1TIwwfdecOP_j6o:hover:before{opacity:0}.-sXLpWAGj2HMFvzRvH_bC{font-size:16px;font-weight:500;line-height:20px;color:var(--newRedditTheme-bodyText);padding:15px 0;position:relative}.-sXLpWAGj2HMFvzRvH_bC span{background-color:var(--newRedditTheme-flair);border-radius:50%;height:30px;margin-right:10px;padding:7px 13px;width:30px}._3UO2hA0CsOqKl1bYybPZGs{color:var(--newRedditTheme-actionIcon);margin:0 5px}.SVn8TtBVFQ-GZUhog511q{display:-ms-flexbox;display:flex;color:#000;background:#fff}.SVn8TtBVFQ-GZUhog511q .V5Q75l1gWtGpBZEehJiGH{-ms-flex-align:center;align-items:center}.SVn8TtBVFQ-GZUhog511q .SIz6ozr7aqewYGVSLfSf6{-ms-flex:1;flex:1;margin-right:8px}.SVn8TtBVFQ-GZUhog511q ._2zetWw7f4W-0OWrUYJHPQ-{font-size:64px;width:64px}
._389RY3FytRs4F82-BLVEiq{content:"";border-left:8px solid transparent;border-right:8px solid transparent;height:0;position:absolute;right:45px;width:0;z-index:100}._3fRnnkCBwqAZG6nmxhTKHr{border-radius:4px;box-shadow:0 4px 4px rgba(0,0,0,.25);margin-top:8px;overflow-y:unset;overflow:unset;width:375px;z-index:100}._3fRnnkCBwqAZG6nmxhTKHr:before{border-bottom:8px solid var(--newRedditTheme-canvas);opacity:.5;top:-8px}._3fRnnkCBwqAZG6nmxhTKHr:after,._3fRnnkCBwqAZG6nmxhTKHr:before{content:"";border-left:8px solid transparent;border-right:8px solid transparent;height:0;position:absolute;right:45px;width:0;z-index:100}._3fRnnkCBwqAZG6nmxhTKHr:after{border-bottom:8px solid var(--newRedditTheme-body);top:-6px}._3oNU8Gzy2V3jDPhFfeEFbD{background-color:var(--newRedditTheme-body);border-radius:4px;position:relative;width:375px}.F0hrtz76LlopbY9X0wtDo{border-radius:4px;display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;padding:16px}.wdFbe8PT7DInxaiHo2Me1{font-size:14px;font-weight:500;line-height:18px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;margin-right:12px}._1581SeO-Xb1j1kfhIRrIyB,._1R0ZV71kh7uwDXo7fn1eDk{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;overflow:hidden}._1581SeO-Xb1j1kfhIRrIyB{border-right:1px solid var(--newRedditTheme-line);padding-right:8px}._27rjoZBkLhiqLLjBu-xU_p{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:600;color:var(--newRedditTheme-metaText)}._27rjoZBkLhiqLLjBu-xU_p._29xCmtH_l8UtRn8IP08VLB{color:var(--newRedditTheme-bodyText)}._27rjoZBkLhiqLLjBu-xU_p ._1mrhJHegVozrNeTH7r5svN{display:inline-block;font-family:IBMPlexSans,Arial,sans-serif;margin-left:4px;position:static;vertical-align:bottom}._2l1d6HSQ764u0JcvRSEJXD{margin-left:8px}._2l1d6HSQ764u0JcvRSEJXD:focus:not(:focus-visible){outline:none}._2MId4QR3fPm4RPlrSTZg_E{background-color:var(--newRedditTheme-body);overflow:hidden;overflow-y:auto;transition:max-height .3s ease-out}._3PWmWL3sMw23-xBHydcnPf{position:relative}._17HPdVVhdV3LWBjzHwGlhA{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;height:200px;-ms-flex-pack:center;justify-content:center}._2CY3n2AMoj0af7gQhj9dfI{font-size:22px;font-weight:500;line-height:26px;font-weight:600;margin-bottom:8px;margin-top:24px}.HxBuWRTAFa8y8bMiQKdSJ{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:18px;color:var(--newRedditTheme-metaText);text-align:center}._8INvnNiEMHRndJ0M-LiY{-ms-flex-align:center;align-items:center;background-color:var(--newRedditTheme-field);border-radius:0 0 4px 4px;display:-ms-flexbox;display:flex;height:49px;-ms-flex-pack:center;justify-content:center;padding:0 12px}.X1WC7m4hrFQNzINreBRsv{font-size:14px;font-weight:700;letter-spacing:.5px;line-height:32px;text-transform:uppercase;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--newRedditTheme-active)}.icon._3pDOQfbIbQuT4PBwPGp85E{color:var(--newRedditTheme-metaText)}.SBkEJxL8i3eNB9EZn7AAz{height:16px;width:16px}.SBkEJxL8i3eNB9EZn7AAz path{fill:var(--newRedditTheme-metaText)}._2prSjBmU3TS_Liup8DFR-2{margin:0 16px}._1OZgaZvEs6sdhMUCqaUCW_{text-align:center;position:relative;padding:15px}._1OZgaZvEs6sdhMUCqaUCW_:before{content:"";position:absolute;top:0;right:-1px;left:-1px;height:7px;background:linear-gradient(90deg,#ec0623,#ff8717);border-top-left-radius:10px;border-top-right-radius:10px}._1OZgaZvEs6sdhMUCqaUCW_ ._3fWRL_DhsIqXjpW4eXDwmR{float:right}._1OZgaZvEs6sdhMUCqaUCW_ ._3fWRL_DhsIqXjpW4eXDwmR ._2xK-Knp1-SUm_DxX4Ak1T0{fill:var(--newRedditTheme-actionIcon);height:12px;width:12px}._1OZgaZvEs6sdhMUCqaUCW_ ._3EmopbfaUR0bemuuUcEcko{font-size:18px;font-weight:500;line-height:22px;clear:both;margin-bottom:5px}._1OZgaZvEs6sdhMUCqaUCW_ ._3MtkPXIDbG9Hf6YeNOxAxv{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px;color:var(--newRedditTheme-metaText)}
._3mUSJN4kdLCGjq-K-JLJw{list-style-type:none}._3mUSJN4kdLCGjq-K-JLJw._2n4UrzwZ3VBdRmFUYAHF_9{background:var(--newRedditTheme-activeAlpha10)}._3mUSJN4kdLCGjq-K-JLJw._2n4UrzwZ3VBdRmFUYAHF_9._3ds5pVvIyBrh1GgQ2O7AFd{background:var(--newRedditTheme-activeAlpha20)}._3mUSJN4kdLCGjq-K-JLJw:hover ._3T3J7R8JnlSfiFdB5bxe5h._2n4UrzwZ3VBdRmFUYAHF_9{box-shadow:unset}._1tpiOc0IxpDU113wUs4zi1{display:-ms-flexbox;display:flex;padding:16px}._1tpiOc0IxpDU113wUs4zi1._3U799isaNx88b2pVv1S7m1{padding:12px 16px}._2WN4-UdVoyjpLQ8mpNTQA{padding-right:8px;position:relative}._12V0IULSx8mSJHxdpHwOGE{border-radius:50%;height:32px;width:32px;background-color:var(--newRedditTheme-actionIcon);display:block;object-fit:cover}._12V0IULSx8mSJHxdpHwOGE._3U799isaNx88b2pVv1S7m1{height:40px;width:40px}._1Bzw8F6BC4Vk8OzAgnU0z3{border-radius:50%;height:32px;width:32px;font-size:12px;font-weight:500;line-height:16px;-ms-flex-align:center;align-items:center;background-color:var(--newRedditTheme-bodyText);color:var(--newRedditTheme-body);display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center}._1Bzw8F6BC4Vk8OzAgnU0z3._3U799isaNx88b2pVv1S7m1{height:40px;width:40px}._3smo-GSstogGTGh6ArpwI0{background-color:var(--newRedditTheme-body);border:1px solid #edeff1;border-radius:50%;box-shadow:0 2px 4px rgba(0,0,0,.05);height:20px;left:12px;position:absolute;top:18px;width:20px}._3smo-GSstogGTGh6ArpwI0._3U799isaNx88b2pVv1S7m1{left:20px;top:26px}.icon.OzS9DxR-g3V71ZAeo2lbH{color:var(--newRedditTheme-active);font-size:12px;height:12px;left:4px;line-height:12px;position:absolute;top:4px;width:12px}._23rEnykeBXjpsB9b72y8_1{height:15px;left:2px;position:absolute;top:2px;width:15px}._23rEnykeBXjpsB9b72y8_1 path{fill:var(--newRedditTheme-active)}._1caKsZ5CCRPSfIgoh608Ej{font-size:18px;margin:0 4px}._1caKsZ5CCRPSfIgoh608Ej._3U799isaNx88b2pVv1S7m1{font-size:18px;font-weight:500;line-height:22px;margin:0;font-family:IBMPlexSans,Arial,sans-serif}._3mGSd8RyCZhF_eqyrV_Bvk{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;margin-bottom:4px}._3D7vaSdKwBK4pdvYmH0ib ._180jOSBDwwE60X5UR8zt3-{font-size:16px;line-height:20px;color:var(--newRedditTheme-bodyText);overflow-wrap:anywhere}._3D7vaSdKwBK4pdvYmH0ib ._180jOSBDwwE60X5UR8zt3-,._3D7vaSdKwBK4pdvYmH0ib ._180jOSBDwwE60X5UR8zt3-._2a8MIP8QlMF7KPqTup62Vt{font-family:Noto Sans,Arial,sans-serif;font-weight:400}._3D7vaSdKwBK4pdvYmH0ib ._180jOSBDwwE60X5UR8zt3-._2a8MIP8QlMF7KPqTup62Vt{font-size:14px;line-height:21px}._3D7vaSdKwBK4pdvYmH0ib ._180jOSBDwwE60X5UR8zt3-._3U799isaNx88b2pVv1S7m1{font-size:18px;font-weight:500;line-height:22px;font-family:IBMPlexSans,Arial,sans-serif}._3D7vaSdKwBK4pdvYmH0ib ._2fQXbzOYQuzqlwMzxgtBKH{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:21px;color:var(--newRedditTheme-metaText);line-height:19px}._3D7vaSdKwBK4pdvYmH0ib ._2fQXbzOYQuzqlwMzxgtBKH._3U799isaNx88b2pVv1S7m1{font-size:18px;font-weight:500;line-height:22px;font-family:IBMPlexSans,Arial,sans-serif}._3D7vaSdKwBK4pdvYmH0ib._3U799isaNx88b2pVv1S7m1{overflow:hidden;text-overflow:ellipsis;line-height:22px;max-height:44px;display:-webkit-inline-box;-webkit-line-clamp:2;white-space:normal;-webkit-box-orient:vertical}._8Q653FSGz7lD9Ux0AQsXY{-ms-flex-align:center;align-items:center;border-radius:4px;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;width:32px;margin-left:10px;-ms-flex:0 0 32px;flex:0 0 32px}._8Q653FSGz7lD9Ux0AQsXY.WHFiF_asC8mzlevTdJv26,._8Q653FSGz7lD9Ux0AQsXY:hover{background-color:var(--newRedditTheme-field)}.icon._2oVe02cXZA6mJa7WXHJFi5{color:var(--newRedditTheme-metaText)}._3Q_e75oXJ8meqWwAQS36l2{-ms-flex:1 0;flex:1 0}._2VDnxV3G5ZvEDq10Z-_fM9{font-size:14px;color:var(--newRedditTheme-metaText);word-break:break-word;line-height:18px;max-height:54px;-webkit-line-clamp:3}._2VDnxV3G5ZvEDq10Z-_fM9,._2VDnxV3G5ZvEDq10Z-_fM9._3U799isaNx88b2pVv1S7m1{font-family:Noto Sans,Arial,sans-serif;font-weight:400;overflow:hidden;text-overflow:ellipsis;display:-webkit-inline-box;white-space:normal;-webkit-box-orient:vertical}._2VDnxV3G5ZvEDq10Z-_fM9._3U799isaNx88b2pVv1S7m1{font-size:12px;line-height:16px;max-height:16px;-webkit-line-clamp:1;color:var(--newRedditTheme-bodyText)}._25ecrisK-bGTesa4kIqyHR{height:18px;margin-right:8px;width:18px}._25ecrisK-bGTesa4kIqyHR path{fill:#006cbf}._1wAIwQaxmGHWzaHv-8jex_{height:18px;margin-right:8px;width:18px;transform:scaleX(-1)}._1wAIwQaxmGHWzaHv-8jex_ path{fill:#006cbf}._3doOacPPJ-LU-aBSoLl9TV{margin-top:8px;height:36px;width:-webkit-fit-content;width:fit-content}._3doOacPPJ-LU-aBSoLl9TV._36xH7NkS9uRrlN87iMo6Bw{width:100%}._3doOacPPJ-LU-aBSoLl9TV._3ds5pVvIyBrh1GgQ2O7AFd{border:none}._3doOacPPJ-LU-aBSoLl9TV._2svu3lh5YfWQmYfACdB2J5{background:var(--newRedditTheme-body)}._3doOacPPJ-LU-aBSoLl9TV._2svu3lh5YfWQmYfACdB2J5._3ds5pVvIyBrh1GgQ2O7AFd{background:var(--newRedditTheme-activeAlpha20)}._3doOacPPJ-LU-aBSoLl9TV._3U799isaNx88b2pVv1S7m1{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:unset;line-height:16px;text-transform:unset;color:var(--newRedditTheme-bodyText);font-family:IBMPlexSans,Arial,sans-serif;height:24px;min-height:24px;padding:4px 22px}._3doOacPPJ-LU-aBSoLl9TV:hover{border-color:var(--newRedditTheme-activeAlpha10);background:var(--newRedditTheme-activeAlpha10)}._3doOacPPJ-LU-aBSoLl9TV:hover._3ds5pVvIyBrh1GgQ2O7AFd{border:none}._3doOacPPJ-LU-aBSoLl9TV ._3LbCSOW9yuZK_CHzTuR9M5{font-size:17px;height:17px;line-height:15px;padding-right:8px}._3doOacPPJ-LU-aBSoLl9TV ._102yZEdZMcXLlu2Ri0KD9O{padding-right:8px}._1cndvAxAFPMUr8IaWuw_we{-ms-flex-align:center;align-items:center;background-color:var(--newRedditTheme-body);border:1px solid var(--newCommunityTheme-line);border-radius:16px;display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;margin-bottom:8px;padding:12px;word-break:break-word}._1cndvAxAFPMUr8IaWuw_we._2n4UrzwZ3VBdRmFUYAHF_9{box-shadow:0 4px 8px rgba(0,0,0,.15)}._1cndvAxAFPMUr8IaWuw_we:last-child{margin-bottom:0}._2fsQOzhZpW9XNu1RXtgzqW{display:-ms-flexbox;display:flex;-ms-flex:1;flex:1;-ms-flex-pack:justify;justify-content:space-between}._2fsQOzhZpW9XNu1RXtgzqW.LypGzp3NJwjpkpsRn9Ocn{opacity:.5}._2XT3C7unUlQXgaiyeYfIYv{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex}._1SZwyv3jy4dBipT0yC1CcI{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;overflow:hidden;text-overflow:ellipsis;line-height:18px;max-height:36px;display:-webkit-inline-box;-webkit-line-clamp:2;white-space:normal;-webkit-box-orient:vertical;color:var(--newRedditTheme-bodyText);line-height:17px}._1LcCO3y9JhylZFlKsgvzHs{display:block}._2EmrjrpYxkgB5_ljritGbO{position:relative}.msJLWFmahK0W8JhaqYny9,._3CGVcVQDu97m9Oj_xs0n01{background-color:var(--newRedditTheme-actionIcon);border-radius:8px;height:40px;margin-left:12px;object-fit:cover;width:40px}.msJLWFmahK0W8JhaqYny9._3U799isaNx88b2pVv1S7m1{height:64px;width:64px;margin-right:16px}._2a0rc3KL05PEnGmVWcQI8W{background-color:var(--newRedditTheme-actionIcon);border-radius:8px;height:40px;margin-left:12px;object-fit:cover;width:40px;filter:brightness(25%)}._2a0rc3KL05PEnGmVWcQI8W._3U799isaNx88b2pVv1S7m1{height:64px;width:64px;margin-right:16px}._2q-yvZHWG3Xp2YECYCI09S{font-size:14px;font-weight:500;line-height:18px;color:#fff;left:20px;position:absolute;top:10px;z-index:1}._2q-yvZHWG3Xp2YECYCI09S._3U799isaNx88b2pVv1S7m1{left:32px;top:22px}._2PzKGDccrg-BWzhhzJaJTs{height:12px;margin-right:5px;width:12px}._2PzKGDccrg-BWzhhzJaJTs path{fill:var(--newRedditTheme-bodyText)}._1i_9WvxHOe7AlJZQ6w_-X9{margin-left:18px;margin-top:2px;z-index:100}._2UKt6pQu-os9uxZnfhPydP{background-color:var(--newRedditTheme-body);border-radius:4px}._1g8x_Z2KsTf65RBk7dRBZm{font-size:14px;font-weight:500;line-height:18px;color:var(--newRedditTheme-bodyText);display:block;padding:8px;text-align:left;width:100%}._1g8x_Z2KsTf65RBk7dRBZm:hover{opacity:.5}@keyframes _27pfB7o_o_4F4TdujFhrNO{0%{background-position:0 0}to{background-position:-200% 0}}._2iacm7sPgvO9z8gO1W7FoY{-ms-flex-align:center;align-items:center;border-bottom:thin solid var(--newRedditTheme-line);display:-ms-flexbox;display:flex;height:48px;padding:8px 16px}._2iacm7sPgvO9z8gO1W7FoY:last-child{border-bottom:none}._2_cDiTNVpitX7CtTmIambB{border-radius:100%;-ms-flex:0 0 auto;flex:0 0 auto;margin-right:8px;width:32px}._2_cDiTNVpitX7CtTmIambB,._2KpinIkIJ7VxNGQgUgzJCA{animation:_27pfB7o_o_4F4TdujFhrNO 1.5s ease infinite;background:linear-gradient(90deg,var(--newCommunityTheme-field),var(--newCommunityTheme-inactive),var(--newCommunityTheme-field));background-size:200%;display:block;height:32px}._2KpinIkIJ7VxNGQgUgzJCA{border-radius:4px;width:100%}._2lh6HxiG9gd6MKnaAag9Cu{font-size:12px;font-weight:500;line-height:16px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center}._2lh6HxiG9gd6MKnaAag9Cu ._2RPeGp2zLx2hBQTZWSUTQK{color:var(--newRedditTheme-bodyText);fill:var(--newRedditTheme-bodyText);height:12px;width:12px}._2lh6HxiG9gd6MKnaAag9Cu ._2bba9zuFqUwxMhGdswkU86{display:-ms-flexbox;display:flex;height:14px;margin-left:5px;color:var(--newRedditTheme-metaText)}
._3B_EfQMwEiEzc_9vEdVplz{background-color:var(--newRedditTheme-body);border-radius:4px;-ms-flex-direction:column;flex-direction:column;padding:20px;height:200px}._3B_EfQMwEiEzc_9vEdVplz,._3AcDG0KjCxs3H1UW_4ajNf{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center}._3AcDG0KjCxs3H1UW_4ajNf{margin-top:10px}.bfJNAfRJ7wvCVMJIHbVa-{border-right:1px solid var(--newRedditTheme-metaText);height:16px;margin:0 10px}._3B_EfQMwEiEzc_9vEdVplz._3eBLRjkIDT-8Hobfrj_UTz{height:unset;padding-bottom:32px}._3B_EfQMwEiEzc_9vEdVplz._2upiES-f8azWSz_UdoeHE7{background-color:var(--newRedditTheme-canvas);padding:80px}.mGm_bo7f-d7T6Ax_UEs_l{margin-top:12px;height:192px}.mGm_bo7f-d7T6Ax_UEs_l.JBKRJW6IC_gf5qQ_mqb4A{height:128px}.odMqhFpc4xkpus4jHz_9f{width:200px;height:192px;position:relative}.odMqhFpc4xkpus4jHz_9f ._13uS-SsNmI2cGGsq2rpP8O{position:absolute}.odMqhFpc4xkpus4jHz_9f ._13uS-SsNmI2cGGsq2rpP8O._29krHC0w9xxlGw1mBpwNHU{bottom:61px}.odMqhFpc4xkpus4jHz_9f ._13uS-SsNmI2cGGsq2rpP8O._3VkvX9EbwQAVQJ3qEl_wzw{bottom:0;right:0}.odMqhFpc4xkpus4jHz_9f ._3yAL94u5AxUY-JhhHIPNuU{position:absolute;top:-15px;left:67px}.odMqhFpc4xkpus4jHz_9f ._2TY8uYFieKTHl7jN_vmcYR{position:absolute;top:10px;left:99px}.odMqhFpc4xkpus4jHz_9f.JBKRJW6IC_gf5qQ_mqb4A{height:128px;width:133px}.odMqhFpc4xkpus4jHz_9f.JBKRJW6IC_gf5qQ_mqb4A ._13uS-SsNmI2cGGsq2rpP8O{width:66px;height:116px}.odMqhFpc4xkpus4jHz_9f.JBKRJW6IC_gf5qQ_mqb4A ._13uS-SsNmI2cGGsq2rpP8O._29krHC0w9xxlGw1mBpwNHU{bottom:38px}.odMqhFpc4xkpus4jHz_9f.JBKRJW6IC_gf5qQ_mqb4A ._3yAL94u5AxUY-JhhHIPNuU{width:57px;top:-1px;left:46px}.odMqhFpc4xkpus4jHz_9f.JBKRJW6IC_gf5qQ_mqb4A ._2TY8uYFieKTHl7jN_vmcYR{width:21px;top:13px;left:65px}.jaQ0krPJ6FkjLU-VDMGNq{height:192px;width:224px;position:relative}.jaQ0krPJ6FkjLU-VDMGNq ._1f1-1KlOtH3uQKPHzkGdDI{position:absolute;width:141px;left:0;bottom:0}.jaQ0krPJ6FkjLU-VDMGNq ._2mEU_pG_y9L4CaC7zihby0{position:absolute;width:60px}.jaQ0krPJ6FkjLU-VDMGNq ._2mEU_pG_y9L4CaC7zihby0._1kfecAwlZWu6be_WDfvh-P{top:60px;left:130px}.jaQ0krPJ6FkjLU-VDMGNq ._2mEU_pG_y9L4CaC7zihby0._4DkJv1On5ORUXrwzznhqE{top:18px;left:165px}.jaQ0krPJ6FkjLU-VDMGNq ._2mEU_pG_y9L4CaC7zihby0._1lJAHwdJYzqn-69JkG-HJQ{top:0;left:110px}.jaQ0krPJ6FkjLU-VDMGNq.JBKRJW6IC_gf5qQ_mqb4A{height:128px;width:150px}.jaQ0krPJ6FkjLU-VDMGNq.JBKRJW6IC_gf5qQ_mqb4A ._1f1-1KlOtH3uQKPHzkGdDI{width:95px}.jaQ0krPJ6FkjLU-VDMGNq.JBKRJW6IC_gf5qQ_mqb4A ._2mEU_pG_y9L4CaC7zihby0{width:40px}.jaQ0krPJ6FkjLU-VDMGNq.JBKRJW6IC_gf5qQ_mqb4A ._2mEU_pG_y9L4CaC7zihby0._1kfecAwlZWu6be_WDfvh-P{top:40px;left:84px}.jaQ0krPJ6FkjLU-VDMGNq.JBKRJW6IC_gf5qQ_mqb4A ._2mEU_pG_y9L4CaC7zihby0._4DkJv1On5ORUXrwzznhqE{top:12px;left:107px}.jaQ0krPJ6FkjLU-VDMGNq.JBKRJW6IC_gf5qQ_mqb4A ._2mEU_pG_y9L4CaC7zihby0._1lJAHwdJYzqn-69JkG-HJQ{top:0;left:71px}._1_kVxSQ5_eQNTfI-Y89mu4{font-style:normal;font-weight:700;font-size:14px;line-height:18px;height:40px;font-family:IBMPlexSans;color:#fff;background:#0079d3;border-radius:999px;margin-right:8px;margin-top:32px;-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center}._1_kVxSQ5_eQNTfI-Y89mu4 span{padding:10px}._3uw_OsQCi8zOpS3fha4JEF{height:270px}._1L4nSUqK39ZB-E1-MXtBve{height:110px}._36brOzjH6sE_rgnTt-hcL1{font-size:22px;font-weight:500;line-height:26px;color:var(--newRedditTheme-bodyText);font-weight:600;margin-bottom:8px;margin-top:24px}._36brOzjH6sE_rgnTt-hcL1.JBKRJW6IC_gf5qQ_mqb4A{font-family:IBMPlexSans;font-size:18px;font-weight:400;line-height:22px;font-weight:500}.Ae79bDDbZ2U_G-wqwA71z{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:18px;color:var(--newRedditTheme-metaText);text-align:center;margin:0 40px}.Ae79bDDbZ2U_G-wqwA71z ._9DV1fqkU31oi8pfSQxzjw{color:var(--newRedditTheme-linkText);margin-left:4px}._23NDu_VaLgaSWVzKHs-Gfa{height:20px;width:20px}._23NDu_VaLgaSWVzKHs-Gfa path{fill:var(--newRedditTheme-metaText)}
._1UtFUrE2ijAe5ba5uPgcfQ{background:rgba(0,0,0,.4);height:100%;left:0;position:fixed;top:0;width:100%;z-index:110}._34uo64r1j-TcpBGXAQcZJ1{background:#fff;border-radius:4px;box-shadow:1px 7px 20px 2px rgba(0,0,0,.4);height:650px;left:50%;overflow:hidden;pointer-events:all;position:fixed;top:50%;transform:translate(-50%,-50%);width:850px;z-index:111}._34uo64r1j-TcpBGXAQcZJ1.FBb4FZ4ng7CvLYrT6LBdp{background:none;box-shadow:none;height:650px}._34uo64r1j-TcpBGXAQcZJ1._3CQoZKhSqrJrbOGJxp03DS{height:327px;width:483px}._34uo64r1j-TcpBGXAQcZJ1._3CQoZKhSqrJrbOGJxp03DS._2CwLGmlfoqlHFJcOwm0RS-{height:300px}._34uo64r1j-TcpBGXAQcZJ1._1ALB_4jSDt6vPeELvg9lKL{height:280px;width:511px}._34uo64r1j-TcpBGXAQcZJ1._1ALB_4jSDt6vPeELvg9lKL._2CwLGmlfoqlHFJcOwm0RS-{height:251px}._34uo64r1j-TcpBGXAQcZJ1._2CwLGmlfoqlHFJcOwm0RS-{max-width:343px;width:calc(100% - 16px)}@media (min-width:768px){._34uo64r1j-TcpBGXAQcZJ1._2CwLGmlfoqlHFJcOwm0RS-{max-width:450px}}._34uo64r1j-TcpBGXAQcZJ1._13CJU7HQst3ucS6l2fTwdh{border-radius:12px;height:640px;width:400px}._34uo64r1j-TcpBGXAQcZJ1._15Lh8Q9iPGbXdxumHm8cT9{height:auto;left:unset;top:46px;transform:translate(0);right:75px;width:auto}@media (min-width:1180px){._34uo64r1j-TcpBGXAQcZJ1._15Lh8Q9iPGbXdxumHm8cT9{right:90px}}._1UtFUrE2ijAe5ba5uPgcfQ._15Lh8Q9iPGbXdxumHm8cT9{background:none;pointer-events:none}._1UtFUrE2ijAe5ba5uPgcfQ._233XfOVq91N_ugGQDBb_OT{visibility:hidden}
._3kFZWXar5EkIAbiKLZxwKw{width:404px;overflow:auto;box-sizing:border-box;display:-ms-flexbox;display:flex}
@keyframes _231us7lszsy_R3tzl2GqL1{0%{transform:scale(.5)}to{transform:scale(1)}}@keyframes eC2A2qBG6f2mU9XPlMMcZ{0%{transform:scale(1)}to{transform:scale(4)}}@keyframes _3ktYxYLY8M4ue26GyBBjpt{0%{opacity:1}to{opacity:0}}._3b88NBdFAQ04N7cULqQvPh{pointer-events:none;animation:_3ktYxYLY8M4ue26GyBBjpt .2s ease-in 1.3s;animation-fill-mode:forwards}._2W0vYckM4OsrrANQqi_sir{background:none;border:none;box-shadow:none}._3xD0e6RJGug4SSLnVIPeh2{position:relative;animation:_231us7lszsy_R3tzl2GqL1 .6s ease-out,eC2A2qBG6f2mU9XPlMMcZ .4s ease-in 1.1s;animation-fill-mode:forwards}._2KBRcm-P0k4_mVHu1UroF6{position:absolute;top:50%;left:50%;background-position:50%;background-size:contain}._3xKR2QByGO_30UN1TJJ9qF{width:350px;height:350px;margin-left:-175px;margin-top:-175px}.Ju8wOr8Uag5VUdjYF6E_m{width:200px;height:200px;margin-left:-100px;margin-top:-100px}._28LAx64oVvQTCvxl2mvkX4{width:256px;height:256px;margin-left:-128px;margin-top:-128px}
._3RwBfA8Nrz_fZLCoxbAAmA{color:var(--newCommunityTheme-metaText);padding-bottom:4px}._2fnA79IIdtL-mNZYnvBalc{-ms-flex-align:baseline;align-items:baseline}._3O97w7RY6RBkLbc3u-Mg4u{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column}._3O97w7RY6RBkLbc3u-Mg4u>div{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:21px;color:var(--newCommunityTheme-bodyText);padding:2px 0}._2rgXACgxMtUDCuKcGDK6tL{width:200px}._3Ren-BGfEFUtj5MNFV9jGZ{width:100px}._3SVP64qu6nV3rRil6Mkvmk{overflow:scroll}._3MZjFI9WV4spd-w0yXdEAG{min-width:0;max-width:none}._2eEY2Q9pfXNNh2P9nh8cn4{font-size:14px;font-weight:700;letter-spacing:.5px;line-height:32px;text-transform:uppercase;padding:0 56px}._1RrzHtukV58ONGeHXBNR7t{height:16px}._1qRgDlLw5wytfgHvP96-gS{max-width:100%}
._1RWqLcP0XUFojNUc0Mf0Yc{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;position:absolute;bottom:0;padding:2px 5px;background:var(--newRedditTheme-body);box-shadow:0 3px 6px rgba(0,0,0,.1);border-radius:16px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;color:var(--newRedditTheme-bodyText)}
.x0hiXHicn7r3BG9m1FJH4,._1vXXD2qKLnHetdKvisFzBD{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row}.x0hiXHicn7r3BG9m1FJH4{border-right:1px solid var(--newCommunityTheme-line);margin-right:8px;padding-right:8px}.x0hiXHicn7r3BG9m1FJH4._2t7TYn6HwRZQwKXG47kpQR{border-right:none;padding-right:0}._3dZnYgFFpifT-M_Vs2FAq6{border-radius:2px;color:var(--newCommunityTheme-navIcon);height:32px;padding:0;position:relative;width:32px}._3dZnYgFFpifT-M_Vs2FAq6:focus,._3dZnYgFFpifT-M_Vs2FAq6:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}._3dZnYgFFpifT-M_Vs2FAq6~._3dZnYgFFpifT-M_Vs2FAq6{margin-left:8px}._3dZnYgFFpifT-M_Vs2FAq6 .icon{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0}._3wyl6g2grDztg8KpnqxWiE{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;width:20px;height:100%;margin-left:4px}._1o57g3XSOeqm_QEQu824EP{bottom:0;height:20px;left:0;margin:auto;position:absolute;right:0;top:0;width:20px}._1o57g3XSOeqm_QEQu824EP path:first-child{fill:#00ccc0}._1o57g3XSOeqm_QEQu824EP path:nth-child(3){fill:none}._1o57g3XSOeqm_QEQu824EP path:nth-child(5){fill:#fff}._1o57g3XSOeqm_QEQu824EP.F6FHwO9Q2Pva6rdcMPWrm path:first-child{fill:none}._1o57g3XSOeqm_QEQu824EP.F6FHwO9Q2Pva6rdcMPWrm circle:nth-child(2),._1o57g3XSOeqm_QEQu824EP.F6FHwO9Q2Pva6rdcMPWrm path:nth-child(4){fill:#d8dadc}._1o57g3XSOeqm_QEQu824EP.F6FHwO9Q2Pva6rdcMPWrm path:nth-child(5){fill:none}._3kwk6KUitnGpZ2JJUx_bOj{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center}.d7xjehjoXyiaQBuluGH0R{width:20px;height:20px}.no2pS2p1GomZL7au3GeF{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center}._3JYbu1qs_Na8zfP23tSqyA{width:20px;height:20px}._39XwvEX05Vwji7kFcISFuV{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;position:relative}.-X88ACLia0m_vNacl1E1S{position:absolute;width:8px;height:8px;background-color:#ff4500;right:4px;top:4px;border-radius:100%}
._3CG2U_hX3HI-ibl5v2RCq1{fill:var(--newRedditTheme-navIcon);height:20px;margin-top:-10px;pointer-events:none;position:absolute;right:8px;top:50%;width:20px}._3jiriKeNer8y0-1r6oWIFM{border:1px solid transparent;border-radius:4px;box-sizing:border-box;height:36px;position:relative;min-width:72px}._3jiriKeNer8y0-1r6oWIFM._24x5wRDxU1y38uXQXvLE4m{border-radius:4px 4px 0 0}._3jiriKeNer8y0-1r6oWIFM._3rS8YTDjcT7fs0k9W4rxDG:focus,._3jiriKeNer8y0-1r6oWIFM._3rS8YTDjcT7fs0k9W4rxDG:hover,._3jiriKeNer8y0-1r6oWIFM._24x5wRDxU1y38uXQXvLE4m{border-color:var(--newRedditTheme-line)}._3jiriKeNer8y0-1r6oWIFM._3NgME2HFZvM-tgAE3s5hXS button{cursor:default}@media (min-width:995px){._3jiriKeNer8y0-1r6oWIFM{width:270px}}._11HXvp3b_PzyK6RcoEr4bJ{height:40px}._1GieMuLljOrqnVpRAwz7VP{display:none;font-size:14px;font-weight:500;line-height:18px}@media (min-width:995px){._1GieMuLljOrqnVpRAwz7VP{display:inline}}.icon.eZQ5o2PrhR59wkAtPbxMU{color:var(--newRedditTheme-bodyText);margin-top:-10px}._1r2uMQFZw5Hg53NkK6rsKv,._363_tmUTkPtgihAQcXPsQv,._1jKtP65jnxLmoGCSqxAgkZ,._3fvJBCH6c6P0NvMwoqK9MJ,._1hCoGzhwFdfF2vGbt8IjSy,.E6V2eHU4CpJuLWzneTk0Z.E6V2eHU4CpJuLWzneTk0Z,.XUd7bCU9SM6ycr6f242KD,._3kzPDKtqN0MnLhOsSJVKHZ,.icon.JisrPypso_3RK4iDgDdke,.icon.eZQ5o2PrhR59wkAtPbxMU,.icon._2L4XuYlbElLC5REx1XpdG_,.icon._2ulegyMhoTE_WCFyBC-IBx,.icon._3fvJBCH6c6P0NvMwoqK9MJ{font-size:20px;height:20px;left:10px;margin-top:-10px;max-height:20px;max-width:20px;position:absolute;top:50%;width:20px}._1r2uMQFZw5Hg53NkK6rsKv,.E6V2eHU4CpJuLWzneTk0Z.E6V2eHU4CpJuLWzneTk0Z{border-radius:4px}._1VemFsujoJ-6RR82VRSPeM{color:#75d377}.TMMvbwyeh9yuHKmQWHrE3{background-color:var(--newRedditTheme-body);border-top-width:1px;border:1px solid var(--newRedditTheme-line);border-top:0 solid var(--newRedditTheme-line);border-radius:0 0 4px 4px;box-sizing:border-box;color:var(--newRedditTheme-bodyText);left:-1px;margin-top:-1px;max-height:482px;overflow-x:hidden;overflow-y:scroll;position:absolute;right:0;top:100%;width:270px}.TMMvbwyeh9yuHKmQWHrE3._2C3hDQLC8D1ZRSBAx93g1c{padding-bottom:16px}.icon.JisrPypso_3RK4iDgDdke{color:#ddbd37}.icon._2ulegyMhoTE_WCFyBC-IBx{color:#ff4500}.icon._2L4XuYlbElLC5REx1XpdG_{color:#75d377}._3mvXSuBIpYAdAsBJSB-1G5 ._2T11xMsmkdwP6G_mY6eUBW{fill:var(--newRedditTheme-actionIcon);height:20px;margin-top:-4px;width:20px}._3mvXSuBIpYAdAsBJSB-1G5:hover ._2T11xMsmkdwP6G_mY6eUBW{fill:var(--newRedditTheme-button)}.icon._2FVCfsIPxXtl6S-c69sXO4{cursor:pointer;color:var(--newRedditTheme-navIcon);height:16px;margin-top:-10px;position:absolute;right:36px;top:50%;width:16px}.icon._2FVCfsIPxXtl6S-c69sXO4._371yhrlWAj7dxOsk1PWqG4{cursor:default;opacity:.2}@media (max-width:1250px){.icon._2FVCfsIPxXtl6S-c69sXO4{display:none}}.h-jI8r2f9ozTNqu_2TBeY{background-color:var(--newRedditTheme-body);bottom:0;border-radius:4px;box-sizing:border-box;color:var(--newRedditTheme-bodyText);height:100%;left:0;line-height:34px;overflow:hidden;padding-left:40px;padding-right:56px;position:absolute;text-align:left;text-overflow:ellipsis;top:0;white-space:nowrap;width:100%}.h-jI8r2f9ozTNqu_2TBeY:focus{border-color:var(--newRedditTheme-line);outline:none}@media (max-width:995px){.h-jI8r2f9ozTNqu_2TBeY{padding:0}}._1hCoGzhwFdfF2vGbt8IjSy{background-color:var(--newRedditTheme-actionIcon);border-radius:50%}._363_tmUTkPtgihAQcXPsQv{margin-top:-9px}._29Am3nlgySiqDV_UaDXD69{height:20px}._3kzPDKtqN0MnLhOsSJVKHZ{max-height:22px;max-width:22px;width:22px;height:22px}.XUd7bCU9SM6ycr6f242KD{left:16px}
._26MVepkxZHzpNv1cuAA4JA{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row}._26MVepkxZHzpNv1cuAA4JA._7Xbismt11Yj8tq6BaRWFr{background-color:var(--newCommunityTheme-menuButtonBackground-hover)}.oiDWziAp_Bua6rb7oQKXs{width:100%}.cq0sTeCPC4GI78UNPdClD.cq0sTeCPC4GI78UNPdClD{-ms-flex-positive:0;flex-grow:0;height:20px;max-height:20px;max-width:20px;width:20px}._1nBP1OfpQDgTmzRFqaVult{-ms-flex-positive:1;flex-grow:1;font-size:14px;line-height:18px;margin-left:8px;max-width:208px;overflow:hidden;text-align:left;text-overflow:ellipsis;white-space:nowrap}._1nBP1OfpQDgTmzRFqaVult._3JpLC8c1ezEsYuuoANyZgr{-ms-flex-positive:unset;flex-grow:unset}._1nBP1OfpQDgTmzRFqaVult+._15QIjcY6qqsms0FXyEsVe9{left:5px;margin:0;position:relative}
._1Ok0AiXwAeYl2SsUBaxgPC{color:var(--newRedditTheme-actionIcon);font-size:10px;font-weight:500;line-height:16px;text-transform:uppercase}
._3n88GuUHAnxPu6a--3e0sz{height:16px;width:160px}._3n88GuUHAnxPu6a--3e0sz,._1TJuQGHgWvq2fnkVcPN7d0{background-color:var(--newRedditTheme-line)}._1TJuQGHgWvq2fnkVcPN7d0{height:20px;margin-top:16px;width:100%}
._3fbofimxVp_hpVM6I1TGMS,._1pjbWqnK8P0fDmz8PgLxXY{box-sizing:border-box;color:var(--newRedditTheme-actionIcon);display:block;height:40px;width:100%}._3fbofimxVp_hpVM6I1TGMS{border:0;cursor:pointer}._3fbofimxVp_hpVM6I1TGMS:active,._3fbofimxVp_hpVM6I1TGMS:focus,._3fbofimxVp_hpVM6I1TGMS:hover{fill:var(--newCommunityTheme-bodyText);color:var(--newCommunityTheme-bodyText);outline:none}._3fbofimxVp_hpVM6I1TGMS:hover{background:var(--newCommunityTheme-menuButtonBackground-hover)}._3fbofimxVp_hpVM6I1TGMS:active{background:var(--newCommunityTheme-menuButtonBackground-active)}._3fbofimxVp_hpVM6I1TGMS:focus{background:var(--newCommunityTheme-menuButtonBackground-focus)}.NiNJXib52w4C8FUidB5af{box-sizing:border-box;color:var(--newRedditTheme-actionIcon);display:block;height:40px;width:100%;border:0;cursor:pointer;font-size:14px;font-weight:500;line-height:18px;-ms-flex-align:center;align-items:center;color:var(--newCommunityTheme-bodyText);display:-ms-flexbox;display:flex;padding-right:16px;padding-left:52px}.NiNJXib52w4C8FUidB5af:active,.NiNJXib52w4C8FUidB5af:focus,.NiNJXib52w4C8FUidB5af:hover{fill:var(--newCommunityTheme-bodyText);color:var(--newCommunityTheme-bodyText);outline:none}.NiNJXib52w4C8FUidB5af:hover{background:var(--newCommunityTheme-menuButtonBackground-hover)}.NiNJXib52w4C8FUidB5af:active{background:var(--newCommunityTheme-menuButtonBackground-active)}.NiNJXib52w4C8FUidB5af:focus{background:var(--newCommunityTheme-menuButtonBackground-focus)}.nBh6t8H3UNZpI1Ce9s6yQ{box-sizing:border-box;color:var(--newRedditTheme-actionIcon);display:block;height:40px;width:100%;border:0;cursor:pointer;font-size:14px;font-weight:500;line-height:18px;-ms-flex-align:center;align-items:center;color:var(--newCommunityTheme-bodyText);display:-ms-flexbox;display:flex;padding-right:16px;padding-left:52px;-ms-flex-pack:justify;justify-content:space-between}.nBh6t8H3UNZpI1Ce9s6yQ:active,.nBh6t8H3UNZpI1Ce9s6yQ:focus,.nBh6t8H3UNZpI1Ce9s6yQ:hover{fill:var(--newCommunityTheme-bodyText);color:var(--newCommunityTheme-bodyText);outline:none}.nBh6t8H3UNZpI1Ce9s6yQ:hover{background:var(--newCommunityTheme-menuButtonBackground-hover)}.nBh6t8H3UNZpI1Ce9s6yQ:active{background:var(--newCommunityTheme-menuButtonBackground-active)}.nBh6t8H3UNZpI1Ce9s6yQ:focus{background:var(--newCommunityTheme-menuButtonBackground-focus)}.f8nXLisWxOYzMMl1uIAP3{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;height:100%;padding:0 20px}.f8nXLisWxOYzMMl1uIAP3 ._225mt8Dkk7IyfYILsMLk9t{-ms-flex:0 0;flex:0 0;font-size:20px;height:20px;margin-right:12px;min-width:20px;width:20px}.f8nXLisWxOYzMMl1uIAP3 .yloKeyD8bfd8UJ_Gi9rsR{-ms-flex:1 1 100%;flex:1 1 100%;font-size:14px;font-weight:500;line-height:18px;text-align:left;width:100%;text-overflow:ellipsis;white-space:nowrap;overflow:hidden}.f8nXLisWxOYzMMl1uIAP3:focus{outline:none}._3MAMvvyd5hQy71OUfBGRkm{fill:var(--newRedditTheme-bodyText);-ms-flex:0 0 12px;flex:0 0 12px;height:12px;width:12px}._3DRWid86ywqQiIYSK1e5mN{transform:rotate(0deg);transition:transform .3s ease-out}._3DRWid86ywqQiIYSK1e5mN._1AFIV6eh63D9Ab_ml6uJ5j{transform:rotate(180deg)}._3SDj_IT6ZaqCbKfC4eTjb2{border-bottom:1px solid var(--newRedditTheme-line);margin-bottom:12px;padding-bottom:12px}._3SDj_IT6ZaqCbKfC4eTjb2.R2-Y-K1ZaSHnYA0gp7-nb{border-bottom:0;margin-bottom:0;padding-bottom:0}._3SDj_IT6ZaqCbKfC4eTjb2.sJncFX1AQ0-0SzCGc9V5L{display:none}._3SDj_IT6ZaqCbKfC4eTjb2.sJncFX1AQ0-0SzCGc9V5L._27B2PE8qRdRlQHbzPBidG6{display:block}._2ChaQYEC5d_hjd-mltzvQK{border:0;cursor:pointer}._2ChaQYEC5d_hjd-mltzvQK:active,._2ChaQYEC5d_hjd-mltzvQK:focus,._2ChaQYEC5d_hjd-mltzvQK:hover{fill:var(--newCommunityTheme-bodyText);color:var(--newCommunityTheme-bodyText);outline:none}._2ChaQYEC5d_hjd-mltzvQK:hover{background:var(--newCommunityTheme-menuButtonBackground-hover)}._2ChaQYEC5d_hjd-mltzvQK:active{background:var(--newCommunityTheme-menuButtonBackground-active)}._2ChaQYEC5d_hjd-mltzvQK:focus{background:var(--newCommunityTheme-menuButtonBackground-focus)}._2XCnMY85ivEZUL6cAgK0nV{box-sizing:border-box;color:var(--newRedditTheme-actionIcon);display:block;height:40px;width:100%;-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;height:unset;min-height:40px;padding:12px 20px}._2XCnMY85ivEZUL6cAgK0nV ._ttuvLVH4k74IkCGNFJSt{font-size:12px;font-weight:400;line-height:16px}._225mt8Dkk7IyfYILsMLk9t{-ms-flex:0 0;flex:0 0;font-size:20px;height:20px;margin-right:12px;min-width:20px;width:20px}._3i89oiIrBc-3aoYCzDu8Dy{fill:var(--newRedditTheme-bodyText);-ms-flex:0 0 12px;flex:0 0 12px;height:20px;margin-right:8px;width:20px}.VeDtdPVW3ue8oUfGWbxqu{border:0;cursor:pointer;color:var(--newRedditTheme-actionIcon);display:-ms-flexbox;display:flex;padding:11px 0 11px 40px}.VeDtdPVW3ue8oUfGWbxqu:active,.VeDtdPVW3ue8oUfGWbxqu:focus,.VeDtdPVW3ue8oUfGWbxqu:hover{fill:var(--newCommunityTheme-bodyText);color:var(--newCommunityTheme-bodyText);outline:none}.VeDtdPVW3ue8oUfGWbxqu:hover{background:var(--newCommunityTheme-menuButtonBackground-hover)}.VeDtdPVW3ue8oUfGWbxqu:active{background:var(--newCommunityTheme-menuButtonBackground-active)}.VeDtdPVW3ue8oUfGWbxqu:focus{background:var(--newCommunityTheme-menuButtonBackground-focus)}.VeDtdPVW3ue8oUfGWbxqu:hover{background:none}
.GCltVwsXPu5lE-gs4Nucu{color:var(--newCommunityTheme-bodyText)}._3z4bYCMDgBrJ-Be0By6hNr{color:#787c7e}._3zu1R6cDitNjrJaFA1VPXj{color:var(--newCommunityTheme-bodyText);height:52px}._6PPJ3peMr-B90dx0MQDhB{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column}._6PPJ3peMr-B90dx0MQDhB .msJd1mFtK7HCAm9dasMIn{font-size:12px;font-weight:400;line-height:16px}
._2CQ2c7khtd-m7uslH6Mz7J{display:block;height:40px;overflow:hidden;padding:11px 12px;position:relative;text-overflow:ellipsis;white-space:nowrap}._10IrsfRFg99DXaIMnqu-vj{margin-left:52px;margin-right:20px}._2KD6rqR9FU8VQKN4P42INe{display:block;overflow:hidden;position:relative;text-overflow:ellipsis;white-space:nowrap}._2KD6rqR9FU8VQKN4P42INe,.Yxq-GFO2Z9y82pMFEMLAf{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:18px;color:var(--newRedditTheme-bodyText);padding:8px 4px}.Yxq-GFO2Z9y82pMFEMLAf{height:unset}
._37tmRmxaFMjRRrvwcY2JmY{background-color:var(--newRedditTheme-field);border:1px solid var(--newRedditTheme-line);color:var(--newRedditTheme-bodyText);height:30px;margin:16px 16px 0;outline:none;padding:0 6px;box-sizing:border-box;width:calc(100% - 32px)}._37tmRmxaFMjRRrvwcY2JmY:focus,._37tmRmxaFMjRRrvwcY2JmY:hover{background-color:var(--newRedditTheme-body);border:1px solid var(--newRedditTheme-button)}._2MgAHlPDdKvXiG-Qbz5cbC{padding:8px 24px;position:relative}._2XRPX11qL4-HxWPuHAzOW5{padding:16px 24px 8px}._1ee4j8lY-1iIi8GkJdJ5RD{float:right;height:16px}
._3KaTO_3YaHK3SMocnu8jV9{margin-right:16px;overflow:hidden;transition:margin .6s;white-space:nowrap}._1Bt_cwKVUG30M9eNB-9rU4{border-left:1px solid var(--newCommunityTheme-line);height:48px;margin-right:20px}.d2l2sN1D4PNVkzMmwALA2{height:56px}._32Xa3voy05uAFz3ZnopP_S{height:48px}._32Xa3voy05uAFz3ZnopP_S,._1C67uwkUf95iJOZ63vDJOZ{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex}._1C67uwkUf95iJOZ63vDJOZ{height:56px}
._2ukk2zBUtkijjIv8uGpGK,._2ukk2zBUtkijjIv8uGpGK:after{height:0;position:absolute;width:0}._21mjMOHMLOJXm_uLG6jmFe[data-popper-placement^=top]>._2ukk2zBUtkijjIv8uGpGK{border-left:5px solid transparent;border-right:5px solid transparent;border-top:4px solid var(--newCommunityTheme-body);bottom:-4px}._21mjMOHMLOJXm_uLG6jmFe[data-popper-placement^=bottom]>._2ukk2zBUtkijjIv8uGpGK{border-bottom:4px solid var(--newCommunityTheme-body);border-left:5px solid transparent;border-right:5px solid transparent;top:-4px}._21mjMOHMLOJXm_uLG6jmFe[data-popper-placement^=left]>._2ukk2zBUtkijjIv8uGpGK{border-bottom:5px solid transparent;border-left:4px solid var(--newCommunityTheme-body);border-top:5px solid transparent;right:-4px}._21mjMOHMLOJXm_uLG6jmFe[data-popper-placement^=right]>._2ukk2zBUtkijjIv8uGpGK{border-bottom:5px solid transparent;border-right:4px solid var(--newCommunityTheme-body);border-top:5px solid transparent;left:-4px}._21mjMOHMLOJXm_uLG6jmFe{font-size:12px;font-weight:500;line-height:16px;border-radius:8px;background:var(--newCommunityTheme-body);color:var(--newCommunityTheme-bodyText);box-shadow:0 2px 12px rgba(0,0,0,.15);opacity:0;transition:opacity 0s step-end;white-space:pre-wrap;z-index:20}._21mjMOHMLOJXm_uLG6jmFe.bxlw8_5wUYitxHKlcuDhP{opacity:1;transition-duration:.5s}
._1PvH4m9c5gT9_kN2ABo2zG{border-radius:2px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;margin:0 8px;color:var(--newCommunityTheme-navIcon);height:32px;padding:0;position:relative;width:32px}._1PvH4m9c5gT9_kN2ABo2zG:focus,._1PvH4m9c5gT9_kN2ABo2zG:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}._1PvH4m9c5gT9_kN2ABo2zG .icon{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0}._3o_sZYSm7bb0JtNcA6cbSw{width:20px;height:100%;margin-left:4px}._3o_sZYSm7bb0JtNcA6cbSw,._3r9BIkFwDCS3l0qK9Tn7rI{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center}._3r9BIkFwDCS3l0qK9Tn7rI{text-align:start;background-image:linear-gradient(89.94deg,#ec0623,#ff8717);color:#fff;max-width:105px;padding:6px;border-radius:8px;font-weight:700;font-size:14px;line-height:17px}
._1oBkxkI9Ae3Qs71WqfDicM{background-color:#1d2535;box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-pack:justify;justify-content:space-between;padding:0 16px;width:100%}._1oBkxkI9Ae3Qs71WqfDicM,._3zEcZZkpP9hBtkGINx6zWf{-ms-flex-align:center;align-items:center}._3zEcZZkpP9hBtkGINx6zWf{display:-ms-inline-flexbox;display:inline-flex}._1ZrnhKss6v3Ggw08tDbTXH{height:32px;margin-right:8px;width:32px}._1rivc6IIexuAqsRVeptXuq{height:18px;fill:#fff}
._1t5i5bNwZeJ7FuUXZ9rM-p:active .jEUbSHJJx8vISKpWirlfx,._1t5i5bNwZeJ7FuUXZ9rM-p:focus .jEUbSHJJx8vISKpWirlfx,._1t5i5bNwZeJ7FuUXZ9rM-p:hover .jEUbSHJJx8vISKpWirlfx{background:none}._1t5i5bNwZeJ7FuUXZ9rM-p .jEUbSHJJx8vISKpWirlfx:focus,._1t5i5bNwZeJ7FuUXZ9rM-p:focus{outline-width:0}._1t5i5bNwZeJ7FuUXZ9rM-p:focus>.jEUbSHJJx8vISKpWirlfx{outline:2px auto Highlight;outline:5px auto -webkit-focus-ring-color}._1t5i5bNwZeJ7FuUXZ9rM-p:focus,._1t5i5bNwZeJ7FuUXZ9rM-p:focus>.jEUbSHJJx8vISKpWirlfx,.jEUbSHJJx8vISKpWirlfx:focus{outline:none}.jEUbSHJJx8vISKpWirlfx{box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;height:32px;padding-right:16px;padding-left:12px;border-radius:9999px;color:var(--newRedditTheme-bodyText);cursor:pointer;white-space:nowrap;border:none;font-size:12px;font-weight:400;line-height:16px;font-size:13px}._2Q7wEg_pr4EKVIc6XvJibh{text-align:center}._1F-AgkBVxGxQsEfI3oVkVa{margin-right:4px}
._1CJrQqx8R1geiDbJFRZlgJ{background-color:transparent!important}._1qlK0UklDPcZgA7_wDEzl-{border-radius:50%;max-width:100%;max-height:100%}
.PH-V9ggsF2mi5JTDmDqdR{border-radius:2px}.PH-V9ggsF2mi5JTDmDqdR:focus,.PH-V9ggsF2mi5JTDmDqdR:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}.FOioVk_DUTmZIKKa82Mm1{box-sizing:border-box;height:32px;width:32px;fill:var(--newCommunityTheme-navIcon);position:relative}.FOioVk_DUTmZIKKa82Mm1._2DgzqfpTotjWrh91uFswuC{background-color:var(--newCommunityTheme-line)}
._2zZ-KGHbWWqrwGlHWXR90y~._2zZ-KGHbWWqrwGlHWXR90y{margin-left:8px}._1aj2BqXAeeo2bHwArcJ5AT{height:16px;width:16px;fill:var(--newCommunityTheme-navIcon)}._14ugEJZOmgrUDXYeFSSv9w{height:16px;width:16px;display:inline-block}._14ugEJZOmgrUDXYeFSSv9w._3ge8uSGq8pAK2qqs45Vzde{fill:#ff4500}._1x6pySZ2CoUnAfsFhGe7J1{border-radius:2px;-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;padding:8px;position:relative}._1x6pySZ2CoUnAfsFhGe7J1:focus,._1x6pySZ2CoUnAfsFhGe7J1:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}._2zZ-KGHbWWqrwGlHWXR90y,._1x6pySZ2CoUnAfsFhGe7J1{height:32px}._1x6pySZ2CoUnAfsFhGe7J1{padding:0;width:32px}._20HfCAFz3ot1MW1o29ZoGZ{display:none}@media (min-width:600px){._20HfCAFz3ot1MW1o29ZoGZ{display:-ms-flexbox;display:flex}}._1pA8z73SZ1olP5KMKFN4_Z{margin-left:8px}._1luaIaEVRAlXWIwqbCOj2a{margin-top:-8px}._1V77mEI1g_5ZlCh_c2-Yab{height:16px;width:16px;fill:var(--newCommunityTheme-navIcon)}._1V77mEI1g_5ZlCh_c2-Yab._2Wgcbg0LNUiJf4L2fVQJ7O{fill:#ff4500}._2mR_VyuaB50nsX1FR6XERF{height:16px;width:16px;fill:var(--newCommunityTheme-navIcon)}._3uVYL9qgX3QSEa_F4F-DPv{color:var(--newCommunityTheme-navIcon);position:absolute;top:0;bottom:0;left:0;right:0;margin:auto}._3yBCXICbzc12nPbAnZeJ54,.jDNUjGbnBI3MbjQP-vMxG ._3yBCXICbzc12nPbAnZeJ54{background:transparent;border:0;border-radius:16px;position:absolute;right:15px;top:63px}.jDNUjGbnBI3MbjQP-vMxG.jDNUjGbnBI3MbjQP-vMxG{background-color:rgba(26,26,27,.6)}.gTjw2SU9vOhjAAj_FayzC{cursor:pointer}
._3uJguwDAW5Ra1r4aegBvBq{z-index:100;background-color:var(--newRedditTheme-body);border-radius:4px;width:375px;box-shadow:0 4px 4px rgba(0,0,0,.25);border:1px solid var(--newCommunityTheme-line)}._3uJguwDAW5Ra1r4aegBvBq._1TfMsQUAiVAqjXRo7s3R_t{opacity:1}
._1Tdh9XCXmEOaXAlloLqrmH{position:relative}._3OMmYPy8XZymvnsxBSK3c0{z-index:99;background-color:var(--newRedditTheme-body);border-radius:10px;width:310px;box-shadow:0 4px 29px rgba(0,0,0,.25);border:1px solid var(--newCommunityTheme-line)}._3OMmYPy8XZymvnsxBSK3c0._1Ssw-NK4SzV_ZrK0hsAQZj{opacity:1}._3OMmYPy8XZymvnsxBSK3c0>._3Dl1lNOXSRFghRireQprSr:after,._3OMmYPy8XZymvnsxBSK3c0>._3Dl1lNOXSRFghRireQprSr:before{border-bottom-color:#ff4500}
._1_-T-UyaTFWSKiU5qkmH4p{position:relative;padding:5px 12px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;min-width:100px;white-space:nowrap}._3BW2xh05Xd6fPp8ewmG_zt{opacity:0;width:15px;position:absolute;animation:_3EsU62vzG6DnMyeCR6qmsN 1s;animation-iteration-count:infinite;animation-direction:alternate;animation-timing-function:ease-in}._2ayMLd0-DF3iBdcNu4Jyw9{width:25px;height:25px;display:inline-block;padding:0 5px 0 0}@keyframes _3EsU62vzG6DnMyeCR6qmsN{0%{opacity:0}to{opacity:1}}._2XTOJxs8_NUxZs7xO_yqD4{top:55%;left:-6%}.DSsYeuIxRQ_6mpLKn7Znw{top:-28%;left:30%;animation-delay:-.8s}.egE_sRX5MzRyi9eJWBBvR{bottom:17%;right:-6%;animation-delay:-.6s}
._3hna43Sh0DTnoV7v2NNc2r{position:relative;background-image:linear-gradient(67.9deg,#5349da 11.74%,#b44ac0 88.14%);padding:5px 12px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;min-width:100px;white-space:nowrap;color:var(--newRedditTheme-lightText);font:inherit;font-weight:500;font-size:14px}._3VX6GfMQ01Q_1wsiZnQ2UN{opacity:0;width:15px;position:absolute;animation:_2IZWjcaeEX-WJFI5gdPVK 1s;animation-iteration-count:infinite;animation-direction:alternate;animation-timing-function:ease-in}@keyframes _2IZWjcaeEX-WJFI5gdPVK{0%{opacity:0}to{opacity:1}}.Y2DEjcFyO7_glQ5xOX4oz{top:55%;left:-6%}._1D5RCB-D8nMhwHbA6m6tDq{top:-28%;left:30%;animation-delay:-.8s}.Iupw9Lt8-wmCtxCgp5_m8{bottom:17%;right:-6%;animation-delay:-.6s}
._2lPBwpVCWIEI428aTPAwZx{fill:var(--newRedditTheme-actionIcon);height:12px;width:12px}._1_Rq-E5LCS_6JTARElGK12{height:12px;position:absolute;right:12px;top:12px;width:12px}._2IHh1GBfUxJVQQX0dJvAry{background-color:var(--newRedditTheme-body);border-radius:4px;border:1px solid var(--newRedditTheme-line);box-shadow:0 1px 4px 0 rgba(0,0,0,.1);padding:16px 12px;position:fixed;right:4px;top:46px;width:260px;z-index:100}._2IHh1GBfUxJVQQX0dJvAry:before{background-color:#169df0;border-radius:3px;border-color:var(--newRedditTheme-line);border-style:solid;border-width:2px 0 0 2px;content:"";height:12px;position:absolute;right:47px;top:-8px;transform:rotate(45deg);width:12px}@media (min-width:1210px){._2IHh1GBfUxJVQQX0dJvAry:before{right:193px}}._1l7oRxdMdQQ7NG2BqRCukJ{background-color:#169df0;border-radius:4px 4px 0 0;height:8px;left:0;position:absolute;right:0;top:0}._3tEYeY-LfC8l7tb0sWeImJ{font-weight:500;line-height:18px}._42_eHTHzRRdWB7Fg8R_QS,._3tEYeY-LfC8l7tb0sWeImJ{font-size:14px;color:var(--newRedditTheme-bodyText)}._42_eHTHzRRdWB7Fg8R_QS{line-height:21px}._33SFF8h93OHkDyAJ59D1nc,._42_eHTHzRRdWB7Fg8R_QS{font-family:Noto Sans,Arial,sans-serif;font-weight:400}._33SFF8h93OHkDyAJ59D1nc{font-size:12px;line-height:18px;color:var(--newRedditTheme-metaText);margin:8px 0 12px}._9wv2Od0X3vE5kIG9M0Ic{display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;width:100%;gap:4px}._193xt0mDvkWqbClnP3Aj6T{-ms-flex-preferred-size:0;flex-basis:0;-ms-flex-positive:1;flex-grow:1}.BwIqd_kQSoiSr3qEDtdp_{margin-left:4px}
._2qW2MlTCwrBhUAXSCWhbPD{display:none}
.nSJCQrnLY07CzwT8tTsNO{border-radius:4px;border:1px solid var(--newCommunityTheme-line);box-shadow:0 1px 4px 0 rgba(0,0,0,.1);padding:16px 12px;right:4px;top:46px;width:280px}.nSJCQrnLY07CzwT8tTsNO,.nSJCQrnLY07CzwT8tTsNO:before{background-color:var(--newCommunityTheme-body);position:absolute}.nSJCQrnLY07CzwT8tTsNO:before{border-radius:3px;border-color:var(--newCommunityTheme-line);border-style:solid;border-width:2px 0 0 2px;content:"";height:12px;right:19px;top:-8px;transform:rotate(45deg);width:12px}.csebgIdGwT3fBJ8kUT2aQ{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase}.rsZg2IAMPbcDGNPnNIBy_,.csebgIdGwT3fBJ8kUT2aQ{color:var(--newCommunityTheme-bodyText)}.rsZg2IAMPbcDGNPnNIBy_{font-size:14px;font-weight:500;line-height:18px}._3m-DocsNGlVUjAtAm7ZZLi{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:18px;color:var(--newCommunityTheme-metaText);margin:8px 0 12px}._3tJL-r-lrTcB_GkrrlZxEN{width:112px}
._12xlue8dQ1odPw1J81FIGQ{display:inline-block;vertical-align:middle}
._3Cv40_kOluVBAL091sOCxD{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}._2BlCG_Fre5CwjrmCj-tn1q{-ms-flex-align:center;align-items:center;background:#ff4500;border-radius:4px;box-sizing:border-box;color:var(--newCommunityTheme-body);display:-ms-flexbox;display:flex;fill:var(--newCommunityTheme-body);font-size:12px;gap:4px;-ms-flex-pack:justify;justify-content:space-between;padding:4px 8px;z-index:1}._2BlCG_Fre5CwjrmCj-tn1q,._2BlCG_Fre5CwjrmCj-tn1q:before{position:absolute;top:-1px;left:-1px;bottom:-1px;right:-1px}@media (max-width:1209px){._2BlCG_Fre5CwjrmCj-tn1q,._2BlCG_Fre5CwjrmCj-tn1q:before{top:-5px;bottom:-5px}}._2BlCG_Fre5CwjrmCj-tn1q:before{content:"";background:var(--newCommunityTheme-body);opacity:0}:hover>._2BlCG_Fre5CwjrmCj-tn1q:before{opacity:.08}:focus>._2BlCG_Fre5CwjrmCj-tn1q:before{opacity:.16}:active>._2BlCG_Fre5CwjrmCj-tn1q:before{opacity:.24}.H1fHPW-543ZCV3rP9cBCL{max-height:100%}._1KluuoHO1AUSycMrFg-Pes{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-positive:1;flex-grow:1;gap:4px;min-width:0}@media (max-width:1209px){._1KluuoHO1AUSycMrFg-Pes{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}}._1TDlO7WPuAmg6Bs3kOLrH9,.oLMif5Jj6X17CKHWVOYBZ{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.oLMif5Jj6X17CKHWVOYBZ{font-weight:500}
._1YWXCINvcuU7nk0ED-bta8{box-sizing:border-box;color:var(--newRedditTheme-bodyText);cursor:pointer;display:block;fill:var(--newRedditTheme-actionIcon);padding:10px 16px 10px 48px;position:relative}._1YWXCINvcuU7nk0ED-bta8:focus,._1YWXCINvcuU7nk0ED-bta8:hover{background-color:var(--newRedditTheme-button);color:var(--newRedditTheme-body);fill:var(--newRedditTheme-body);outline:none}._1YWXCINvcuU7nk0ED-bta8:focus ._1HGeWoy6faY2UWkCD7cYoW,._1YWXCINvcuU7nk0ED-bta8:hover ._1HGeWoy6faY2UWkCD7cYoW{color:var(--newRedditTheme-body)}.icon._1Jtes5zRWNpwobWM4O2Unx{display:inline-block;height:12px;vertical-align:middle;width:12px;font-size:12px;margin-left:8px}._1HGeWoy6faY2UWkCD7cYoW{font-size:12px;font-weight:400;line-height:16px;color:var(--newRedditTheme-metaText)}._2KotRmn9DgdA58Ikji2mnV{box-sizing:border-box;color:var(--newRedditTheme-bodyText);cursor:pointer;display:block;fill:var(--newRedditTheme-actionIcon);padding:10px 16px 10px 48px;position:relative;-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;text-align:left;width:100%}._2KotRmn9DgdA58Ikji2mnV:focus,._2KotRmn9DgdA58Ikji2mnV:hover{background-color:var(--newRedditTheme-button);fill:var(--newRedditTheme-body);outline:none}._2KotRmn9DgdA58Ikji2mnV:focus,._2KotRmn9DgdA58Ikji2mnV:focus ._1HGeWoy6faY2UWkCD7cYoW,._2KotRmn9DgdA58Ikji2mnV:hover,._2KotRmn9DgdA58Ikji2mnV:hover ._1HGeWoy6faY2UWkCD7cYoW{color:var(--newRedditTheme-body)}._2KotRmn9DgdA58Ikji2mnV .vLtBjS_8SMsuZByMrcgJH{box-sizing:border-box;left:-4px;position:absolute;width:100%}._2BQPq3iyS8t6kKtFmtkB30,._2BQPq3iyS8t6kKtFmtkB30._3RofgwJEAbXD6OnLxEZ8Kg{height:20px;left:16px;position:absolute;top:10px;width:20px}._2BQPq3iyS8t6kKtFmtkB30._3RofgwJEAbXD6OnLxEZ8Kg{fill:#ff4500}.vzhy90YD0qH7ZDJi7xMGw{font-size:14px;font-weight:500;line-height:18px;display:inline-block;vertical-align:middle}
._6opQAE7SUXi-Fy7P3vItL._6opQAE7SUXi-Fy7P3vItL{display:-ms-inline-flexbox;display:inline-flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:justify;justify-content:space-between;width:100%}._6qTe2HfpYA9trfOatbi74{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;background:linear-gradient(67.9deg,#5349da 11.74%,#b44ac0 88.14%);border-radius:999px;padding:3px 9px 3px 5px;color:#fff;width:-webkit-fit-content;width:fit-content;position:relative}._1lcNm4na-FCLir4IeIpM7w{width:18px;height:18px;bottom:-2px;margin-right:2px}._2thIi4nb9dgSv10ECKVHL4{opacity:0;width:10px;position:absolute;animation:w8i-7IiMlCG-ncHyRHzxw 1s;animation-iteration-count:6;animation-direction:alternate;animation-timing-function:ease-in}@keyframes w8i-7IiMlCG-ncHyRHzxw{0%{opacity:0}to{opacity:1}}._2XE_ejqL9tZ617JilWAoev{top:-20%;left:20%}.RPtjfCh_RZnh_Lh-sTACB{top:-30%;right:20%;animation-delay:-.8s}.o03hgL0CTE9PaKw9A2nHD{bottom:-20%;left:30%;animation-delay:-.6s}._16-T-fB2mGMlxyfbZjQvUG{bottom:-5%;right:0;animation-delay:-.2s}
._1xqG70qc6pOtmdrQRLOqLA._1xqG70qc6pOtmdrQRLOqLA{display:-ms-inline-flexbox;display:inline-flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:justify;justify-content:space-between;width:100%}._3_q3LTg22ze3wzCdYIyppX{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;background:linear-gradient(90deg,#ec0623,#ff8717);border-radius:999px;padding:3px 9px;color:#fff;width:-webkit-fit-content;width:fit-content;position:relative}
._1yPJhJHbop3b8ymORnDlBK{position:relative;height:210px;background-color:var(--newRedditTheme-line);margin:0 10px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;overflow:hidden;-ms-flex-pack:center;justify-content:center;cursor:pointer;-ms-flex-direction:column;flex-direction:column;border-radius:10px}._1yPJhJHbop3b8ymORnDlBK ._3g1xz9MOUzi-gIHyX1hC81{position:absolute;top:8px;right:8px;background-color:hsla(0,0%,100%,.5);padding:5px 0;border-radius:50%;z-index:2;outline:none;border:none}._1yPJhJHbop3b8ymORnDlBK ._3g1xz9MOUzi-gIHyX1hC81 ._1Rt6re1Drdoq1Ln4u6i1OS{width:25px;height:12px}._1yPJhJHbop3b8ymORnDlBK ._1X-eWVnYVCwPvAP6w20Ahb{width:100%}._1yPJhJHbop3b8ymORnDlBK ._1UTlx4irdeqqCLgD9M1iJg{font-size:12px;line-height:16px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:justify;justify-content:space-between;padding:10px;position:absolute;background-color:rgba(0,0,0,.4);font-weight:700;bottom:0;left:0;color:var(--newCommunityTheme-lightText);right:0}._1yPJhJHbop3b8ymORnDlBK ._1UTlx4irdeqqCLgD9M1iJg .IJhhlBRCIGMd5rHgYGsv_{background:var(--newCommunityTheme-body);padding:6px 12px;border-radius:15px;color:var(--newCommunityTheme-bodyText);font-size:12px}
._2gT-SgcGRQsJc7cLAzWT3r{padding-right:40px}._26v6JOihbU7MuezKAlj4JI{padding:0 12px}.u_VVgOsrqJsUNbQ80sEby{display:-ms-inline-flexbox;display:inline-flex;vertical-align:middle;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;font-size:21px!important}._3eGd1zitdF6RmAyLpSDjG6{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
._2pXW42IYsGP59qZnjAnkAx{font-size:12px;font-weight:500;line-height:16px;color:#a8aaab;margin-left:8px}.DFKWwVItcycZV1bKUOyay{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row}.DFKWwVItcycZV1bKUOyay ._3x3dhQasGAuYcXVQ02QUzy{color:var(--newRedditTheme-actionIcon)}.Rz5N3cHNgTGZsIQJqBfgk{font-size:12px;font-weight:500;line-height:16px;color:#a8aaab}._1pHyKCBktIf_9WFW9jjM3P{display:none}@media (min-width:1210px){._1pHyKCBktIf_9WFW9jjM3P{display:block}}._3KfbpxpA8Esu_3UHTmIvfw{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;margin-left:8px;text-align:left;width:32px}._3KfbpxpA8Esu_3UHTmIvfw._22SL37yETIW414yUiZj27w{margin-left:0;width:inherit}._3KfbpxpA8Esu_3UHTmIvfw._2OFo5eaD2V6ZcJsYBuYned{width:auto}@media (min-width:1210px){._3KfbpxpA8Esu_3UHTmIvfw._2OFo5eaD2V6ZcJsYBuYned{width:175px}}._1zZ3VDhRC38fXLLvVCHOwK{background-color:var(--newRedditTheme-body);display:-ms-flexbox;display:flex;height:40px;margin-top:4px;margin-bottom:4px;width:100%}._1zZ3VDhRC38fXLLvVCHOwK._3Axd0OX2sZP0PEIHdeocc3{padding-left:12px}._3m4MQxMy4WfgIkMhHh-UAg{font-size:14px;font-weight:500;line-height:18px;display:inline-block;vertical-align:middle}.icon.LyE1zRbUJlGravH4LHRfD{font-size:12px;line-height:1;height:12px;margin:-2px -6px 0 0}.icon._2wYneOcJEB6o4mj1NedmsR{color:#ff4500;font-size:12px;margin-right:2px;vertical-align:middle}._50RxI-5rW1xzwoC42vhzM{display:inline-block;fill:var(--newRedditTheme-actionIcon);height:20px;vertical-align:middle;width:20px}.-z42jjKOFdAdFhdJ8mmI4.-z42jjKOFdAdFhdJ8mmI4{border-radius:4px;float:left;max-height:24px;max-width:24px;height:24px;width:24px}.-z42jjKOFdAdFhdJ8mmI4.-z42jjKOFdAdFhdJ8mmI4._2XkHtsPtFuTExJyk9JQUAp{border-radius:50%}._1zyV-XmoYeSNGWjfZiXbPc{margin-right:5px}._3-lF5kPDkSGfnVUW_GtvUV{color:var(--newRedditTheme-actionIcon)}._2Az3JCV8DZZ1S6CU8cR-bl,.gRVZlDl2ZHFThtPLjYYzD{height:20px;left:16px;position:absolute;top:10px;width:20px}._18X7KoiaLuKbuLqg4zE8BH{border:1px solid transparent;border-radius:4px;padding:2px 0;position:relative;min-height:32px}._18X7KoiaLuKbuLqg4zE8BH._22SL37yETIW414yUiZj27w{-ms-flex-pack:center;justify-content:center}._18X7KoiaLuKbuLqg4zE8BH._3F3oKTToidUQ0CbMS1cccX,._18X7KoiaLuKbuLqg4zE8BH:focus,._18X7KoiaLuKbuLqg4zE8BH:hover{border-color:var(--newRedditTheme-line);outline:none}._18X7KoiaLuKbuLqg4zE8BH._3F3oKTToidUQ0CbMS1cccX{border-radius:4px 4px 0 0}._18X7KoiaLuKbuLqg4zE8BH._2XkHtsPtFuTExJyk9JQUAp{border:none}.icon.pztXT07fzqRz6IEE6thRV{font-size:12px;height:12px;line-height:12px;margin-left:4px;width:12px}._1HSQGYlfPWzs40LP4_oFi5._1HSQGYlfPWzs40LP4_oFi5{border-radius:0 0 4px 4px;border:1px solid var(--newRedditTheme-line);border-top:none;box-shadow:none;margin-top:-2px;max-height:80%;overflow-y:auto;overflow-x:hidden;padding-top:6px;position:fixed;width:211px;z-index:80}._1HSQGYlfPWzs40LP4_oFi5._1HSQGYlfPWzs40LP4_oFi5._2XkHtsPtFuTExJyk9JQUAp{border-radius:4px;border-top:1px solid var(--newRedditTheme-line);-ms-flex-pack:end;justify-content:flex-end;margin-top:4px;padding-bottom:8px;padding-top:8px;width:252px}._2BMnTatQ5gjKGK5OWROgaG{font-size:12px;font-weight:500;line-height:16px;color:var(--newRedditTheme-bodyText);display:block;white-space:nowrap}._7cxLZzQcuE-aYbch5G9oN{border-top:1px solid var(--newRedditTheme-line);margin:0 16px}._18Q1kN_hFY6M09dHaoehBF{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;color:var(--newRedditTheme-actionIcon);margin:8px 0 4px 12px}.pszNQQxC761u1dbJ3aR-C{display:-ms-flexbox;display:flex}
._1hLh4ExbW_Gl2pkGABn5Fq ._3qX-j7T3VyXW0TBXQ7qkHK{padding:8px 16px;width:100%;font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:unset;line-height:17px;text-transform:unset}._1hLh4ExbW_Gl2pkGABn5Fq ._3qX-j7T3VyXW0TBXQ7qkHK._2FhXjIw1NMLaXYPWvrnUCg{background-color:#ff4500;margin-bottom:10px}._1hLh4ExbW_Gl2pkGABn5Fq ._3qX-j7T3VyXW0TBXQ7qkHK._3Nbznnag8RXkaF5nEep0Pk{color:var(--newRedditTheme-metaText)}._1hLh4ExbW_Gl2pkGABn5Fq ._3qX-j7T3VyXW0TBXQ7qkHK:active,._1hLh4ExbW_Gl2pkGABn5Fq ._3qX-j7T3VyXW0TBXQ7qkHK:focus{outline:none}._1hLh4ExbW_Gl2pkGABn5Fq._3brHkn8WaQ5H2a1LCn89uk{border:none;border-top:1px solid var(--newRedditTheme-widgetColors-lineColor);padding:16px 0 0}._24bis7_J1W0ONK7UsGGBZy{border-radius:16px;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-pack:justify;justify-content:space-between;min-height:214px;padding:20px 16px 10px;width:375px}._24bis7_J1W0ONK7UsGGBZy._3bv61QiJPtGfHcXPpyOpkc{background-color:var(--newRedditTheme-body);border:1px solid var(--newRedditTheme-line);box-shadow:0 2px 20px 0 rgba(0,0,0,.3);box-sizing:border-box;min-height:76px;position:fixed;z-index:100}._2O5VCGnV4yRDRvGGGyH5T0{margin:0;text-align:center}._28EAA6q-RnTJAGjzmgV3Ei{-ms-flex-align:start;align-items:flex-start;-ms-flex-direction:column;flex-direction:column}._1mjvXY5U1vwpsbbNYGJjul{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:18px;margin-top:16px}._1a2XFA9WQOHGxunCZN6IjZ{padding:24px;width:100%}.-JVIMQjsj_SPFhYYAQvsI{-ms-flex-align:center;align-items:center;background-color:#f6f7f8;border-radius:50%;display:-ms-flexbox;display:flex;height:60px;-ms-flex-pack:center;justify-content:center;margin:10px 0 4px;width:60px}.-JVIMQjsj_SPFhYYAQvsI>svg{height:55px;width:41px}._3-s4mChdgxSWHNGzBUc0N4{display:inline-block;height:20px;position:relative;width:20px}._1-mT11KLeK0Cj3V_xKgaTx{color:#d4d7d9;position:absolute}._3e3gGI61xrpfMpllnZxDrm{font-size:18px;font-weight:500;line-height:22px}.MYXaqAXi91ALzJTXm9rjA{font-size:20px;font-weight:500;line-height:24px}.rTLLrliYnsQtx0zfqWuwt{font-size:22px;font-weight:500;line-height:26px}._2WW7LagVCdXCoAI0ts8mJr{font-size:16px;font-weight:500;line-height:20px;background-color:rgba(237,239,241,.5);border-radius:8px;box-sizing:border-box;display:inline-block;margin:16px 0;padding:10px 28px;width:265px;word-break:break-word}
._2I12Htze2UzJmmfnrgYJOn ._1jAt0x8BSB9mgoXbsDuKJ6{color:#121212;font-size:18px;margin:5px 5px 5px 7px;font-weight:400;height:20px;line-height:20px;vertical-align:middle;width:20px}._2I12Htze2UzJmmfnrgYJOn ._1jAt0x8BSB9mgoXbsDuKJ6 :before{font-size:18px}._2I12Htze2UzJmmfnrgYJOn ._24UNt1hkbrZxLzs5vkvuDh{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;position:relative;background-color:#edeff1;border-radius:50px;padding:0;height:32px;min-width:32px}._2I12Htze2UzJmmfnrgYJOn ._24UNt1hkbrZxLzs5vkvuDh:focus,._2I12Htze2UzJmmfnrgYJOn ._24UNt1hkbrZxLzs5vkvuDh:hover{background-color:#d4d7d9;outline:none}._2I12Htze2UzJmmfnrgYJOn._1dBtowHdRHcGyLbVEaOL8t ._1jAt0x8BSB9mgoXbsDuKJ6{color:#fff}._2I12Htze2UzJmmfnrgYJOn._1dBtowHdRHcGyLbVEaOL8t ._24UNt1hkbrZxLzs5vkvuDh{background-color:#303030}._2I12Htze2UzJmmfnrgYJOn._1dBtowHdRHcGyLbVEaOL8t ._24UNt1hkbrZxLzs5vkvuDh:focus,._2I12Htze2UzJmmfnrgYJOn._1dBtowHdRHcGyLbVEaOL8t ._24UNt1hkbrZxLzs5vkvuDh:hover{background-color:#464748}._2I12Htze2UzJmmfnrgYJOn ._1vP7zMn-UGF6u5e-GPHAvN{margin-right:12px;font-size:14px;font-weight:500}
@media (min-width:1180px){a._3Wg53T10KuuPmyWOMWsY2F,button._3Wg53T10KuuPmyWOMWsY2F{width:120px}}._234aKY_LemFWuSTYVoshHn{height:16px;margin-right:8px;width:16px}._2qcLS5et_OlJluP0WWDdsJ{-ms-flex-align:center;align-items:center;display:-ms-inline-flexbox;display:inline-flex;color:var(--newCommunityTheme-button);fill:var(--newCommunityTheme-button);-ms-flex-direction:row;flex-direction:row;font-size:12px;line-height:16px;width:120px}@media (min-width:1180px){.U3FRqDA_Qhr4icbaNXSuf button{width:70px}}._1JBkpB_FOZMZ7IPr3FyNfH{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-direction:row;flex-direction:row;display:none}@media (min-width:616px){._1JBkpB_FOZMZ7IPr3FyNfH{display:-ms-flexbox;display:flex}}._31lJpVPojF0SAR5usRZ36h{display:none}@media (min-width:1310px){._31lJpVPojF0SAR5usRZ36h{display:block}}._19oWd7e3z7-ztUGzdIoCR7{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-direction:row;flex-direction:row}.Z_HUY3BUsGOBOtdmH94ZS{margin-left:4px}@media (min-width:1180px){.Z_HUY3BUsGOBOtdmH94ZS{margin-left:16px}}._3Z5rfDuvQDBNfBgpXdnt_b{display:-ms-inline-flexbox;display:inline-flex;position:absolute}._1vXK1WOmrEh97U366xznqT,._2QpF1Fkq_rr2nvPL1no0nN{margin-right:8px}
._30BbATRhFv3V83DHNDjJAO,._2GyPfdsi-MbQFyHRECo9GO{-ms-flex-align:center;align-items:center;display:-ms-inline-flexbox;display:inline-flex;-ms-flex-direction:row;flex-direction:row}._2GyPfdsi-MbQFyHRECo9GO{height:48px}.lNoTgmppXfHyXXS-3aRDj{height:56px}._2vkeRJojnV7cb9pMlPHy7d{-ms-flex-align:center;align-items:center;display:-ms-inline-flexbox;display:inline-flex;box-sizing:border-box;-ms-flex-direction:row;flex-direction:row;-ms-flex-positive:1;flex-grow:1;padding:0 20px}._2vkeRJojnV7cb9pMlPHy7d.a35Fm2MurU14xdNybLiZp{background-color:var(--newCommunityTheme-body);border-bottom:1px solid var(--newCommunityTheme-line)}._31IHoBZ9we7EzLMdkTaIR2{height:100%}.Y4MkVr6trrdypfZVUkpIA{-ms-flex-align:center;align-items:center;display:-ms-inline-flexbox;display:inline-flex;box-sizing:border-box;-ms-flex-direction:row;flex-direction:row;-ms-flex-positive:1;flex-grow:1;padding:0 20px;max-width:100vw}.Y4MkVr6trrdypfZVUkpIA,.Y4MkVr6trrdypfZVUkpIA.a35Fm2MurU14xdNybLiZp{background-color:var(--newCommunityTheme-body);border-bottom:1px solid var(--newCommunityTheme-line)}@media (min-width:560px){.Y4MkVr6trrdypfZVUkpIA{-ms-flex:1 1 100%;flex:1 1 100%}}._1iqnOY2Y57wmetu8MAjiId{-ms-flex-positive:1;flex-grow:1;margin:0 auto;max-width:690px}._1iqnOY2Y57wmetu8MAjiId._17gDYx5g5X6q--Lcmc9IvO{max-width:390px}._2dlTXDaX9JuL0bekTwhV18{fill:var(--newCommunityTheme-navIcon);-ms-flex-positive:1;flex-grow:1;margin-left:16px;margin-right:16px;width:auto;height:auto}._1O4jTk-dZ-VIxsCuYB6OR8{height:32px;padding:8px 8px 8px 0;width:32px}._32hLJ8_m9mplK6bwNXysk8{height:36px}._1bWuGs_1sq4Pqy099x_yy-{display:none;height:18px;margin-right:20px;width:auto}@media (min-width:1070px){._1bWuGs_1sq4Pqy099x_yy-{display:block}}._3dnbqz69WJTFCss8wl7Wlk{-ms-flex-align:center;align-items:center;display:-ms-inline-flexbox;display:inline-flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-positive:1;flex-grow:1}._23q1waDr4n_2fR5A7zcZzb{display:none}@media (min-width:788px){._23q1waDr4n_2fR5A7zcZzb{display:-ms-flexbox;display:flex}}._2u8LqkbMtzd0lpblMFbJq5{-ms-flex-align:center;align-items:center;display:-ms-inline-flexbox;display:inline-flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-positive:0;flex-grow:0}._1tvdSTbdxaK-BnUbzUIqIY{color:var(--newCommunityTheme-bodyText)}._1tvdSTbdxaK-BnUbzUIqIY._1z0T-r2uyIYQr2tLUWs4M2{padding-left:284px}._2egmn5KNYpLrH0zPS0gihA{bottom:-1px;left:0;position:absolute;top:0;z-index:1}
._2oM1YqCxIwkvwyeZamWwhW{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;margin:0;padding:0 2px}._25IkBM0rRUqWX5ZojEMAFQ{line-height:15px;margin:0 1px;text-align:center;width:32px}._783RL1AYIib59nxLCXhgv{margin-right:8px}
._1LHxa-yaHJwrPK8kuyv_Y4{width:100%}._1LHxa-yaHJwrPK8kuyv_Y4:hover ._31L3r0EWsU0weoMZvEJcUA{display:none}._1LHxa-yaHJwrPK8kuyv_Y4 ._31L3r0EWsU0weoMZvEJcUA,._1LHxa-yaHJwrPK8kuyv_Y4:hover ._11Zy7Yp4S1ZArNqhUQ0jZW{display:block}._1LHxa-yaHJwrPK8kuyv_Y4 ._11Zy7Yp4S1ZArNqhUQ0jZW{display:none}
.K4Eem3pMbRbAYioOfqN5E{-ms-flex-align:center;align-items:center;box-sizing:border-box;display:-ms-flexbox;display:flex;height:100%;margin:auto;max-width:1128px;padding:0 12px 0 32px;width:100%}@media (min-width:960px){.K4Eem3pMbRbAYioOfqN5E{padding:0 32px}}.K4Eem3pMbRbAYioOfqN5E._1_ihtgX_FgdbtB-rbz84r6{max-width:none}.-DOLBAFWXMQX1Q3ErGO8I{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex:1;flex:1;max-width:calc(100% - 324px);width:100%}.icon._33YMDoIltkTaZemWTS7Yki{color:#d7dadc;font-size:16px;margin-right:8px}.P9Qd6oTCWgLr3ackKg0I5{font-size:14px;font-weight:500;line-height:18px;display:-ms-inline-flexbox;display:inline-flex;min-width:0}.P9Qd6oTCWgLr3ackKg0I5 ._1iZHnGYX-Wc90AM6BQQemg{display:-ms-flexbox;display:flex;max-width:100%}.SHwEfOV-Wq0AnI-uha8Ci{font-size:14px;font-weight:500;line-height:18px;display:-ms-inline-flexbox;display:inline-flex;min-width:0;color:#d7dadc}.SHwEfOV-Wq0AnI-uha8Ci ._1iZHnGYX-Wc90AM6BQQemg{display:-ms-flexbox;display:flex;max-width:100%}._15Igkrvvp7jIfVHt0eKzFd:before{margin-right:8px}._15Igkrvvp7jIfVHt0eKzFd:after,._15Igkrvvp7jIfVHt0eKzFd:before{border-right:1px solid #343536;content:"";display:inline-block;height:16px;vertical-align:text-bottom;width:0}._15Igkrvvp7jIfVHt0eKzFd:after{margin:0 8px}._15Igkrvvp7jIfVHt0eKzFd .voteButton:focus{background-color:#343536}._25ONQRwoX20oeRXFl_FZXt{display:-ms-flexbox;display:flex;-ms-flex-pack:end;justify-content:flex-end;margin-left:12px;width:312px;font-size:12px;font-weight:700;line-height:16px}._25ONQRwoX20oeRXFl_FZXt ._2W8hDtix416kR_AGDshJ1q{width:auto;margin-right:12px;padding:0 25px;transition:opacity .15s cubic-bezier(.53,0,.57,1.01);opacity:0}._25ONQRwoX20oeRXFl_FZXt ._2W8hDtix416kR_AGDshJ1q._3hDL4MmXN5ibsBRoePashZ{opacity:1}button._2Mq93X6GCESH9CsQ6XVqOS{color:#d7dadc}.xP-T4vxk4aKEQTlxxGner{color:#d7dadc;font-size:12px;font-weight:400}._34HwaRmVoDiPrSaCPUqpjx{padding:0;max-width:1080px;-ms-flex-pack:justify;justify-content:space-between}._34HwaRmVoDiPrSaCPUqpjx,._34HwaRmVoDiPrSaCPUqpjx .-DOLBAFWXMQX1Q3ErGO8I{height:100%}._34HwaRmVoDiPrSaCPUqpjx ._2W8hDtix416kR_AGDshJ1q{margin-right:0}._34HwaRmVoDiPrSaCPUqpjx ._33YMDoIltkTaZemWTS7Yki,._34HwaRmVoDiPrSaCPUqpjx .xP-T4vxk4aKEQTlxxGner{color:var(--newCommunityTheme-bodyText)}._34HwaRmVoDiPrSaCPUqpjx ._3LZZ1LMv49fbgZrji_1D8u{width:20px;margin:0 4px 0 8px}._34HwaRmVoDiPrSaCPUqpjx ._15Igkrvvp7jIfVHt0eKzFd{height:100%}._34HwaRmVoDiPrSaCPUqpjx ._15Igkrvvp7jIfVHt0eKzFd:after,._34HwaRmVoDiPrSaCPUqpjx ._15Igkrvvp7jIfVHt0eKzFd:before{border-color:var(--newCommunityTheme-line);height:100%}
._2Dj4y3V6eat21HkRlbaeqL{border-bottom:1px solid rgba(0,0,0,.2);margin-bottom:15px}._2FBcfa5LIJrKSNuRAA7WWa{padding:0 0 8px}._2gHNfZLuOuUSh3Ppfyc0JX{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:18px;padding:4px 24px 22px 0}._2XQ3s48lqlzodYPpT2s-Iu{background-color:var(--newRedditTheme-button);height:40px}
.FRrbwuHy8Zmlubp3nowLZ{display:-ms-flexbox;display:flex;-ms-flex-pack:end;justify-content:end;padding:16px 20px 0;position:relative}._3hELZctjzdizaWjW1al9DZ{-ms-flex-item-align:end;-ms-grid-row-align:end;align-self:end;-ms-flex:1;flex:1;height:16px}._2oY_N7NWiAv9m_mFIRdwVX{border-radius:2px;cursor:pointer;height:20px;padding:0 4px 0 8px;width:20px}._3B-ny-D97ZKwdUyXAaWF19{color:var(--newRedditTheme-actionIcon)}._20fGT0XJD3MvX9yBsVeKMn{color:var(--newCommunityTheme-bodyText)}._20fGT0XJD3MvX9yBsVeKMn ._2oY_N7NWiAv9m_mFIRdwVX:hover{background-color:var(--newCommunityTheme-line)}._20fGT0XJD3MvX9yBsVeKMn ._3B-ny-D97ZKwdUyXAaWF19{fill:var(--newCommunityTheme-navIcon)}.BtYn3oMRXzNwmNMkolecQ{padding:20px 24px 40px}._3k3RwDkEsbX50bb-DBvuWj{-ms-flex:1;flex:1;overflow-y:auto}
.trdUvQxqQHHqQKOUBcgnr{--Toaster-indicatorColor:initial;-ms-flex-align:center;align-items:center;background:var(--newCommunityTheme-body);border:1px solid var(--newCommunityTheme-actionIcon);border-radius:4px;box-shadow:0 2px 15px 0 rgba(0,0,0,.3);box-sizing:border-box;display:-ms-flexbox;display:flex;margin-bottom:12px;min-height:52px;padding-left:8px;position:relative;transition:padding .3s;width:476px}@media (max-width:480px){.trdUvQxqQHHqQKOUBcgnr{width:300px}}.trdUvQxqQHHqQKOUBcgnr:before{background-color:var(--Toaster-indicatorColor);border:1px solid var(--Toaster-indicatorColor);border-radius:4px 0 0 4px;content:"";height:100%;left:0;margin:-1px;position:absolute;top:0;width:8px}
._7JH6kQpO-bx66b9ajIZrz{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:21px;color:var(--newCommunityTheme-bodyText);-ms-flex:1;flex:1;margin:0 12px;overflow-wrap:anywhere}._7JH6kQpO-bx66b9ajIZrz:first-letter{text-transform:uppercase}
._2Jt0Cjod2bIVz4VEgb6ZNn{height:25px;margin:0 0 3px 12px;width:24px}._1BkkYahLrqvrnZoHHBH9pU{margin:0 12px}._3F4cPSBsBgzFOcnpe466x-,._33UT9FofKPRVp4gDnLAM-6,._5OZRCtpmuaH0Is4CZ7GpZ,._-43TYgcIz7mHcgQHam-CV,.tClrg2w16xkW4hmCj8nTo{height:25px;margin:0 0 3px 12px;width:24px}.tClrg2w16xkW4hmCj8nTo{fill:#46d160}.ZI0D2mGVpaunJEvFji7pm{fill:#ffb000}.ZI0D2mGVpaunJEvFji7pm,.vvMBwTMgHpgz4UTQ4H_nJ{height:25px;margin:0 0 3px 12px;width:24px}.vvMBwTMgHpgz4UTQ4H_nJ{fill:#ea0027}._3q-XSJ2vokDQrvdG6mR__k{-ms-flex-align:center;align-items:center;bottom:0;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;left:0;margin:auto;position:fixed;right:0;width:0;z-index:200}._3q-XSJ2vokDQrvdG6mR__k,._3q-XSJ2vokDQrvdG6mR__k .EjdBJNEwygtHMKiHd3Bnv._29WPjLJ0vRIyLIUC_lQ4a8{-ms-flex-direction:column;flex-direction:column}._3q-XSJ2vokDQrvdG6mR__k .EjdBJNEwygtHMKiHd3Bnv._29WPjLJ0vRIyLIUC_lQ4a8{padding-top:16px;padding-right:8px}._3q-XSJ2vokDQrvdG6mR__k .EjdBJNEwygtHMKiHd3Bnv._29WPjLJ0vRIyLIUC_lQ4a8 .CloseIcon{top:calc(50% - 8px)}._3q-XSJ2vokDQrvdG6mR__k .EjdBJNEwygtHMKiHd3Bnv._29WPjLJ0vRIyLIUC_lQ4a8 ._2-rGW3UtrT-pD45pofU3tx{box-sizing:border-box;-ms-flex-direction:row-reverse;flex-direction:row-reverse;padding-top:16px;padding-bottom:8px;width:100%}._3q-XSJ2vokDQrvdG6mR__k .EjdBJNEwygtHMKiHd3Bnv._29WPjLJ0vRIyLIUC_lQ4a8 ._2-rGW3UtrT-pD45pofU3tx>button{-ms-flex:1;flex:1;margin-left:8px}._3q-XSJ2vokDQrvdG6mR__k .EjdBJNEwygtHMKiHd3Bnv._29WPjLJ0vRIyLIUC_lQ4a8 ._21oJwLzDt5kLN6scufKBab{-ms-flex-align:start;align-items:flex-start}._21oJwLzDt5kLN6scufKBab{-ms-flex-positive:1;flex-grow:1}._2-rGW3UtrT-pD45pofU3tx,._21oJwLzDt5kLN6scufKBab{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex}._2-rGW3UtrT-pD45pofU3tx{margin-right:8px;white-space:nowrap}.EjdBJNEwygtHMKiHd3Bnv:before{transition:width .3s}.EjdBJNEwygtHMKiHd3Bnv .CloseIcon{cursor:pointer;fill:var(--newCommunityTheme-body);height:16px;left:4px;opacity:0;position:absolute;transition:opacity .3s;width:16px}.EjdBJNEwygtHMKiHd3Bnv:hover{padding-left:24px}.EjdBJNEwygtHMKiHd3Bnv:hover:before{width:24px}.EjdBJNEwygtHMKiHd3Bnv:hover .CloseIcon{opacity:1}
.zrXDKcys3Vl7vt1f6ef4V{color:var(--newCommunityTheme-linkText)}
._1tI68pPnLBjR1iHcL7vsee{margin:0 12px}._3RhWPJfjpsEoBw52x0fQp2{width:700px}.n4AaEF3hCCYK665NCiJr8{-ms-flex-direction:column;flex-direction:column}._3vKcvhm0JtGJa_zEd1cO2w{display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-align:center;align-items:center;margin:6px 0}.DbXewCiis2PwiAq2jiL5k{display:inline-block;margin-bottom:6px}.DbXewCiis2PwiAq2jiL5k:last-child{margin-bottom:0}._2BNSty-Ld4uppTeWGfEe8r{display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;-ms-flex-align:center;align-items:center;margin:12px 0;min-width:50%}
._37JeV292IJA7_x1qej_-2H{font-size:22px;font-weight:500;line-height:26px}.p13k-tsMcatGBlVpJBZmw{font-size:20px;font-weight:500;line-height:24px}._1nHvvYpmn7q9eWDAGzKcce{font-size:18px;font-weight:500;line-height:22px}._1-rwUWsB5F8WmYI8F66dai{font-size:16px;font-weight:500;line-height:20px}._22RKdGqihAj6MFumW6DuRV{font-size:14px;font-weight:500;line-height:18px}._4xqrI_N1UdqsK9E1RSisG{font-size:12px;font-weight:500;line-height:16px}._2HJOIn4SJm4z1NeCv_hNFu{font-size:14px;line-height:21px}._2HJOIn4SJm4z1NeCv_hNFu,._3ImIPX9rfoPmUrZ1R8KGqS{font-family:Noto Sans,Arial,sans-serif;font-weight:400}._3ImIPX9rfoPmUrZ1R8KGqS{font-size:12px;line-height:18px}._3uShGanwyVFBaTiPMFzfAC{font-weight:700}._3uShGanwyVFBaTiPMFzfAC,._2nyJGeaFJbXTqTh9OGwxfu{font-size:12px;line-height:16px}._2nyJGeaFJbXTqTh9OGwxfu{font-weight:400;color:var(--newCommunityTheme-metaText)}._3BIqvjJkJKZfH4vtC11dGF{font-size:10px;font-weight:400;line-height:12pt}
._3Cb-J_TUgYhl23GF1E8ueS{-ms-flex-align:center;align-items:center;background:var(--newCommunityTheme-body);border:1px solid var(--newCommunityTheme-actionIcon);border-radius:4px;box-shadow:0 2px 15px 0 rgba(0,0,0,.3);box-sizing:border-box;display:-ms-flexbox;display:flex;margin-bottom:12px;height:143px;position:relative;width:484px}._3noiB6ClBZxqX-VfENVYha{height:100%;width:auto}._2uE5iMLmEfZ_HNjn85c1NP{color:var(--newCommunityTheme-bodyText);box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex:1 1 auto;flex:1 1 auto;height:100%;-ms-flex-pack:justify;justify-content:space-between;padding:16px}._2dvmXQB_w1cCQdCLjHGb0F{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;opacity:.5;height:12px;text-transform:uppercase}._2JcKYVeW6FIeewNVpxApr6{margin:0;width:120px}._1kI4teIozhxDil2omCIIs5{cursor:pointer;fill:var(--newCommunityTheme-button);height:14px;opacity:.3;position:absolute;right:5px;top:5px;width:14px}._1kI4teIozhxDil2omCIIs5:hover{opacity:.8}
.NODQrxMsajJv0SMw0Glss{height:25px;margin:0 0 3px 12px;width:24px;background-size:100%;background-repeat:no-repeat}._-660JDG_NhSvu-lby-LYB{margin:0 12px}._3jUV8naze01hV-7EqsBdjm{width:700px}
.GfthJQJvWCHdUoMi6YjYa{font-size:12px;font-weight:500;line-height:16px;z-index:80}
._1uQwMnfXrOfzkL_CFxH6fd,.vOGtEDdh1mVbkqinhg3Ov{text-decoration:underline}._3el1HrJryfAxBUzu4HsIhE{padding-left:8px;position:fixed;width:100%;-ms-flex-align:center;align-items:center;color:#fff;display:-ms-flexbox;display:flex}._3el1HrJryfAxBUzu4HsIhE._2s1xq3Ji1Oj7oZtdSqWznV,._3el1HrJryfAxBUzu4HsIhE._36j6vvbAY0wIrxbyXuNQhn,._3el1HrJryfAxBUzu4HsIhE._1ivoPEQV9lryC0mH-f_uGY{background-color:#ea0027;display:block;top:0;height:25px}._1oAzKCYwbVOQ-AbuRZfMg2{-ms-flex:0 1 60px;flex:0 1 60px;height:60px}._6aklZuhHMm1XJcsi8dEeP._6aklZuhHMm1XJcsi8dEeP{fill:#fff}
.OEQgz7Lkj--3zFaLL7BUF{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;gap:12px;padding:0 12px;height:34px;background-color:#121212;color:#fff;transition:height .3s ease}.OEQgz7Lkj--3zFaLL7BUF._1HWVXJoazfrENIGlRprCVp{background-color:#00a268}.OEQgz7Lkj--3zFaLL7BUF ._3BcAFuYpz37S0WFvgyWCUN{width:20px;height:20px}.OEQgz7Lkj--3zFaLL7BUF ._2hQKVL2Pm4yfkiqifapnBp{-ms-flex:auto;flex:auto;font-size:14px}.OEQgz7Lkj--3zFaLL7BUF ._1E59q-NCGBwN0Aq_bPsPKb{width:28px;height:28px;line-height:28px;text-align:center;border-radius:2px;cursor:pointer}.OEQgz7Lkj--3zFaLL7BUF ._1E59q-NCGBwN0Aq_bPsPKb:hover{background-color:hsla(0,0%,100%,.2)}.OEQgz7Lkj--3zFaLL7BUF._2elztvdigLcbcRyu_4wcFW{height:0;overflow:hidden}
.cx1ohrUAq6ARaXTX2u8YN{margin-top:0}.cx1ohrUAq6ARaXTX2u8YN._378Md-M6pOqwzEiV3lAwYk,.cx1ohrUAq6ARaXTX2u8YN._2P-zXcOfggYIWnL3EfXUHP,.cx1ohrUAq6ARaXTX2u8YN._3o7sV2ySJ76-f1ktwzclmi{margin-top:25px}.cx1ohrUAq6ARaXTX2u8YN._1OVuPhC0s89CZodD5qWMWP{margin-top:0}.cx1ohrUAq6ARaXTX2u8YN._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,.cx1ohrUAq6ARaXTX2u8YN._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,.cx1ohrUAq6ARaXTX2u8YN._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi{margin-top:25px}.cx1ohrUAq6ARaXTX2u8YN._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl{margin-top:0}.cx1ohrUAq6ARaXTX2u8YN._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,.cx1ohrUAq6ARaXTX2u8YN._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,.cx1ohrUAq6ARaXTX2u8YN._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi{margin-top:25px}._2DJXORCrmcNpPTSq0LqL6i{background-color:rgba(28,28,28,.9);bottom:0;height:100%;left:0;position:fixed;right:0;width:100%;z-index:50}._2DJXORCrmcNpPTSq0LqL6i._26pbaCw90eAC80WRqUfICJ{--comments-overlay-background:inherit;--comments-overlay-offset:0}._2DJXORCrmcNpPTSq0LqL6i._26pbaCw90eAC80WRqUfICJ:after{background:var(--comments-overlay-background);bottom:0;content:"";height:100%;left:0;margin:0 auto;max-width:1280px;position:fixed;right:var(--comments-overlay-offset);top:0;width:calc(100% - 160px - var(--comments-overlay-offset))}._2DJXORCrmcNpPTSq0LqL6i._2zCdbqYzIDmabv-Dk_ILKk:after{max-width:1600px;width:calc(100% - 60px)}._2mIbM_6nl-2OnOGEbEMRXa{bottom:0;height:100%;left:0;position:fixed;-webkit-backface-visibility:hidden;backface-visibility:hidden;right:0;top:0;width:100%;z-index:50}._2mIbM_6nl-2OnOGEbEMRXa:focus{outline:none}._1nxEQl5D2Bx2jxDILRHemb{transition:margin-top .3s ease;padding-top:48px}._1nxEQl5D2Bx2jxDILRHemb._378Md-M6pOqwzEiV3lAwYk,._1nxEQl5D2Bx2jxDILRHemb._2P-zXcOfggYIWnL3EfXUHP,._1nxEQl5D2Bx2jxDILRHemb._3o7sV2ySJ76-f1ktwzclmi{padding-top:73px}._1nxEQl5D2Bx2jxDILRHemb._1OVuPhC0s89CZodD5qWMWP{padding-top:82px}._1nxEQl5D2Bx2jxDILRHemb._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,._1nxEQl5D2Bx2jxDILRHemb._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,._1nxEQl5D2Bx2jxDILRHemb._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi{padding-top:73px}._1nxEQl5D2Bx2jxDILRHemb._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl{padding-top:90px}._1nxEQl5D2Bx2jxDILRHemb._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,._1nxEQl5D2Bx2jxDILRHemb._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,._1nxEQl5D2Bx2jxDILRHemb._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi{padding-top:81px}._1nxEQl5D2Bx2jxDILRHemb._3x1dyL19KnZ4kI6i9TlRp4{padding-left:270px}._1nxEQl5D2Bx2jxDILRHemb._33N4WmnRV24-NLLnXKccj3{padding-top:0}._1nxEQl5D2Bx2jxDILRHemb .zoWOQnp55WuhEugRSwfw1{background-color:var(--newRedditTheme-body);bottom:0;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;left:0;overflow:hidden;position:fixed;width:270px;z-index:4}._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2{position:relative}._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._1OVuPhC0s89CZodD5qWMWP,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._378Md-M6pOqwzEiV3lAwYk,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._2P-zXcOfggYIWnL3EfXUHP,._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2._3o7sV2ySJ76-f1ktwzclmi{padding-top:-1px}._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2 .ListingLayout-backgroundContainer:before{display:none}._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2 .ListingLayout-outerContainer{background-color:var(--newRedditTheme-canvas)}._1nxEQl5D2Bx2jxDILRHemb._2aHCVoJEFfwy05xpKqUif2 .zoWOQnp55WuhEugRSwfw1{position:absolute;top:0}._1nxEQl5D2Bx2jxDILRHemb._1kFzDy0hQVq-CvguZsCcmV{transition-property:none}._3obgdFz00GvpqpuX8QCsNK{background:#030303;box-sizing:border-box;height:48px;left:0;margin:0 auto;max-width:1280px;position:-webkit-sticky;position:sticky;right:0;top:0;transition:top .3s ease;width:calc(100% - 160px);z-index:70}._3obgdFz00GvpqpuX8QCsNK:focus{outline:none}._3obgdFz00GvpqpuX8QCsNK._2zCdbqYzIDmabv-Dk_ILKk{max-width:1600px;width:calc(100% - 60px)}._1k5guql3KcBJzH7i7UCr7Y{height:56px}._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1{top:48px}._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._378Md-M6pOqwzEiV3lAwYk,._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._2P-zXcOfggYIWnL3EfXUHP,._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._3o7sV2ySJ76-f1ktwzclmi,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._378Md-M6pOqwzEiV3lAwYk,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._2P-zXcOfggYIWnL3EfXUHP,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._3o7sV2ySJ76-f1ktwzclmi,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._378Md-M6pOqwzEiV3lAwYk,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._2P-zXcOfggYIWnL3EfXUHP,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._3o7sV2ySJ76-f1ktwzclmi{top:73px}._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._1OVuPhC0s89CZodD5qWMWP,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._1OVuPhC0s89CZodD5qWMWP,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._1OVuPhC0s89CZodD5qWMWP{top:82px}._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi{top:73px}._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl{top:90px}._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,._2DJXORCrmcNpPTSq0LqL6i._2DJXORCrmcNpPTSq0LqL6i._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,._2mIbM_6nl-2OnOGEbEMRXa._2mIbM_6nl-2OnOGEbEMRXa._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,.zoWOQnp55WuhEugRSwfw1.zoWOQnp55WuhEugRSwfw1._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi{top:81px}._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe,._2AJ0ZwpZtFJ10GdcU0CUew{top:56px}._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._378Md-M6pOqwzEiV3lAwYk,._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._2P-zXcOfggYIWnL3EfXUHP,._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._3o7sV2ySJ76-f1ktwzclmi,._2AJ0ZwpZtFJ10GdcU0CUew._378Md-M6pOqwzEiV3lAwYk,._2AJ0ZwpZtFJ10GdcU0CUew._2P-zXcOfggYIWnL3EfXUHP,._2AJ0ZwpZtFJ10GdcU0CUew._3o7sV2ySJ76-f1ktwzclmi{top:81px}._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._1OVuPhC0s89CZodD5qWMWP,._2AJ0ZwpZtFJ10GdcU0CUew._1OVuPhC0s89CZodD5qWMWP{top:90px}._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi,._2AJ0ZwpZtFJ10GdcU0CUew._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,._2AJ0ZwpZtFJ10GdcU0CUew._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,._2AJ0ZwpZtFJ10GdcU0CUew._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi{top:81px}._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl,._2AJ0ZwpZtFJ10GdcU0CUew._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl{top:98px}._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,._2SL_DAWw1V6pxZysgrdeBe._2SL_DAWw1V6pxZysgrdeBe._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi,._2AJ0ZwpZtFJ10GdcU0CUew._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,._2AJ0ZwpZtFJ10GdcU0CUew._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,._2AJ0ZwpZtFJ10GdcU0CUew._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi{top:89px}._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv{top:354px}._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._378Md-M6pOqwzEiV3lAwYk,._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._2P-zXcOfggYIWnL3EfXUHP,._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._3o7sV2ySJ76-f1ktwzclmi{top:379px}._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._1OVuPhC0s89CZodD5qWMWP{top:388px}._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi{top:379px}._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl{top:396px}._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,._1ht98h5gXjzYhFyRZgB0Pv._1ht98h5gXjzYhFyRZgB0Pv._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi{top:387px}._14-8KVF3BKuTNsLNWcOG2X{height:0}._14-8KVF3BKuTNsLNWcOG2X._25N7Qd1z8aRQYtQhjEFyTC{height:90px}._29IbETWb5VVDcfk_-GumWz{height:100%;overflow-y:auto;position:relative;-webkit-overflow-scrolling:touch;width:100%;will-change:transform;contain:layout style size}._29IbETWb5VVDcfk_-GumWz._34Bl1Of1839ZWJXR8IY0Ym{will-change:unset}._13Vg6OZEIy5AcJ_DOw6jK0{left:0;position:absolute;top:0}._1C1Dn0NhEGQkEA9tDGKKSH{position:fixed;right:0;left:0;z-index:79;top:48px}._1C1Dn0NhEGQkEA9tDGKKSH._378Md-M6pOqwzEiV3lAwYk,._1C1Dn0NhEGQkEA9tDGKKSH._2P-zXcOfggYIWnL3EfXUHP,._1C1Dn0NhEGQkEA9tDGKKSH._3o7sV2ySJ76-f1ktwzclmi{top:73px}._1C1Dn0NhEGQkEA9tDGKKSH._1OVuPhC0s89CZodD5qWMWP{top:48px}._1C1Dn0NhEGQkEA9tDGKKSH._1OVuPhC0s89CZodD5qWMWP._378Md-M6pOqwzEiV3lAwYk,._1C1Dn0NhEGQkEA9tDGKKSH._1OVuPhC0s89CZodD5qWMWP._2P-zXcOfggYIWnL3EfXUHP,._1C1Dn0NhEGQkEA9tDGKKSH._1OVuPhC0s89CZodD5qWMWP._3o7sV2ySJ76-f1ktwzclmi{top:73px}._1C1Dn0NhEGQkEA9tDGKKSH._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl{top:56px}._1C1Dn0NhEGQkEA9tDGKKSH._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._378Md-M6pOqwzEiV3lAwYk,._1C1Dn0NhEGQkEA9tDGKKSH._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._2P-zXcOfggYIWnL3EfXUHP,._1C1Dn0NhEGQkEA9tDGKKSH._1OVuPhC0s89CZodD5qWMWP._32g3BKfzA1V3Y0eaczZbYl._3o7sV2ySJ76-f1ktwzclmi{top:81px}
.hciOr5UGrnYrZxB11tX9s{outline:none}
._27RfkQ1Fuxjg5UzNJqCtC-{padding:8px 8px 8px 0;height:32px;width:32px}._1j_hHS0lKR-ok52j1iYlId{height:18px;width:auto}.XGVEYXuPeFqHqAf2DqHaM{padding:0 16px}._1GdKQyDUWvhTFBDr0FsAkj{height:48px}._1GdKQyDUWvhTFBDr0FsAkj,.pb476LMY7Ob_RBN7pZ3kN{-ms-flex-align:center;align-items:center;background-color:var(--newCommunityTheme-body);border-bottom:1px solid var(--newCommunityTheme-line);box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;margin-left:auto;position:relative;z-index:99}.pb476LMY7Ob_RBN7pZ3kN{height:48px;height:56px}
.UaNg246yNIpwcq_Uhe6vC{height:60px;width:60px}.EXdERxzjUGqvBK511L1Eq{background-color:var(--newRedditTheme-canvas);position:absolute;top:0;bottom:0;left:0;right:0;z-index:0}.EXdERxzjUGqvBK511L1Eq,._3dyrEHC8cc6dIOTUPQmv1S{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center}._3dyrEHC8cc6dIOTUPQmv1S{color:var(--newRedditTheme-bodyText);padding:20px;position:relative;text-align:center;z-index:99}._1PdcLVyQbMPVKRikIspqb_{font-size:18px;font-weight:500;line-height:22px;margin-bottom:8px;margin-top:20px}._1YhiRkum1oGZUdm5i1mHFJ{font-size:12px;font-weight:400;line-height:16px;margin-bottom:40px}._1gTZDLeeF0VPQsS6Iz5boy{height:auto;width:100%}._3sveU8lpcXyGOpDXsXc9xg,._2wX-WzezrtDmDaxm8BR4zz,._3zW_PbmBAhs9ARwV_Yl9BR{padding:0 40px;position:absolute}@media (max-width:479px){._3sveU8lpcXyGOpDXsXc9xg,._2wX-WzezrtDmDaxm8BR4zz,._3zW_PbmBAhs9ARwV_Yl9BR{display:none}}@media (max-height:600px){._3sveU8lpcXyGOpDXsXc9xg,._2wX-WzezrtDmDaxm8BR4zz,._3zW_PbmBAhs9ARwV_Yl9BR{display:none}}._3zW_PbmBAhs9ARwV_Yl9BR{top:88px}._2NU2A-ZU5J-cxP78RF0oeb{top:96px}._3sveU8lpcXyGOpDXsXc9xg{bottom:0;max-width:960px}
.S53DUJItOf0GhJnniZ_fP{font-size:14px;font-weight:500;line-height:18px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;color:var(--newRedditTheme-titleText)}._21fWc_5nZQR--Hc7UhjtY9{margin-right:8px}
._2wxsLGNmMLx6sEMLJyn2o9{min-height:100%;overflow:hidden;position:relative;-ms-flex:none;flex:none;--pseudo-before-background:unset}._2wxsLGNmMLx6sEMLJyn2o9:before{content:" ";position:fixed;width:100%;height:100%;top:0;left:0;will-change:transform;background:var(--pseudo-before-background)}
._1OVBBWLtHoSPfGCRaPzpTf{min-width:0;width:100%}._1OVBBWLtHoSPfGCRaPzpTf.PaJBYLqPf_Gie2aZntVQ7{-ms-flex:1 1 100%;flex:1 1 100%}@media (min-width:960px){._1OVBBWLtHoSPfGCRaPzpTf{width:100%}._1OVBBWLtHoSPfGCRaPzpTf._3nSp9cdBpqL13CqjdMr2L_{width:640px}._1OVBBWLtHoSPfGCRaPzpTf._2udhMC-jldHp_EpAuBeSR1{max-width:740px}._1OVBBWLtHoSPfGCRaPzpTf._1Tc65kRFm7a8piCXHVL4L4{width:864px}}@media (min-width:676px){._1OVBBWLtHoSPfGCRaPzpTf._25-JsrYQ-pXWBM8eqpxeN7{width:100%}._1OVBBWLtHoSPfGCRaPzpTf._25-JsrYQ-pXWBM8eqpxeN7._3nSp9cdBpqL13CqjdMr2L_{width:640px}._1OVBBWLtHoSPfGCRaPzpTf._25-JsrYQ-pXWBM8eqpxeN7._2udhMC-jldHp_EpAuBeSR1{max-width:740px}._1OVBBWLtHoSPfGCRaPzpTf._25-JsrYQ-pXWBM8eqpxeN7._1Tc65kRFm7a8piCXHVL4L4{width:864px}}._1OVBBWLtHoSPfGCRaPzpTf._2OVNlZuUd8L9v0yVECZ2iA:only-child{margin-right:336px}
._3aAvvioBKBNnlJqKytAVAd{display:block;font-size:16px;height:32px;padding:8px;margin:-20px 0 8px}._3aVffPeM6Nkqs7D0RJ5FBs{display:inline-block;background-color:#fff;border-radius:24px;padding:8px}._3aAvvioBKBNnlJqKytAVAd ._17MxNCYEMmDof9NnT6ffxl{font-size:16px}._2VB8YvVdvxx0h0VGYVrpBX{font-weight:600}._3aAvvioBKBNnlJqKytAVAd ._2Aw3HO2EUDcP7F481ZxyYl{font-size:24px}.uhMLc-O1VODjzminrp8py{margin:2px}
._31N0dvxfpsO6Ur5AKx4O5d{box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-pack:center;justify-content:center;margin:0 auto;max-width:1248px}@media (min-width:640px){._31N0dvxfpsO6Ur5AKx4O5d{padding:20px 24px}}._3Kd8DQpBIbsr5E1JcrMFTY{display:none;-ms-flex:0 0 312px;flex:0 0 312px;width:312px}@media (min-width:960px){._3Kd8DQpBIbsr5E1JcrMFTY._1tvThPWQpORoc2taKebHxs{display:block}}@media (min-width:1460px){._3Kd8DQpBIbsr5E1JcrMFTY.K1OCXipJxqOt01sOdQXEx{display:block}}.qYj03fU5CXf5t2Fc5iSvg{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;min-height:calc(100vh - 48px)}._35NDNOyTzBcywfeEavUt6p{min-height:calc(100vh - 56px)}._3ozFtOe6WpJEMUtxDOIvtU{z-index:3}.q4a8asWOWdfdniAbgNhMh{-ms-flex:0 0 auto;flex:0 0 auto;position:relative;top:0;left:0;right:0;padding:0;background-color:var(--newCommunityTheme-body)}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/Reddit.911524dea63800915309_.css.map*/</style>
        <link as="script" href="https://www.redditstatic.com/desktop2x/runtime~Reddit.06fbd78943f321491899.js" key="https://www.redditstatic.com/desktop2x/runtime~Reddit.06fbd78943f321491899.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/vendors~CommentsPage~ModerationPages~Reddit~reddit-components-ClassicPost~reddit-components-CompactP~d737df3e.31f8d07ab88edabff736.js" key="https://www.redditstatic.com/desktop2x/vendors~CommentsPage~ModerationPages~Reddit~reddit-components-ClassicPost~reddit-components-CompactP~d737df3e.31f8d07ab88edabff736.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/vendors~CommentsPage~Governance~ModListing~ModerationPages~Reddit~Subreddit.f468f4fbfe44aa5cfabf.js" key="https://www.redditstatic.com/desktop2x/vendors~CommentsPage~Governance~ModListing~ModerationPages~Reddit~Subreddit.f468f4fbfe44aa5cfabf.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/vendors~Chat~Governance~Reddit.6921f706c26009a1fbb3.js" key="https://www.redditstatic.com/desktop2x/vendors~Chat~Governance~Reddit.6921f706c26009a1fbb3.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/vendors~Reddit.fc8d4c49cc97b168c869.js" key="https://www.redditstatic.com/desktop2x/vendors~Reddit.fc8d4c49cc97b168c869.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/CommentsPage~Governance~Reddit~ReportFlow~Subreddit~reddit-components-BlankPost~reddit-components-Cl~5351df81.9f55115c90a0961eb901.js" key="https://www.redditstatic.com/desktop2x/CommentsPage~Governance~Reddit~ReportFlow~Subreddit~reddit-components-BlankPost~reddit-components-Cl~5351df81.9f55115c90a0961eb901.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/Governance~Reddit~Subreddit~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compo~bd4baca2.f2e1cfa53fed5821c00e.js" key="https://www.redditstatic.com/desktop2x/Governance~Reddit~Subreddit~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compo~bd4baca2.f2e1cfa53fed5821c00e.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/Reddit~StandalonePostPage~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compone~9b425435.1be10e42f8dcef625f90.js" key="https://www.redditstatic.com/desktop2x/Reddit~StandalonePostPage~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compone~9b425435.1be10e42f8dcef625f90.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/Reddit~RichTextEditor~reddit-components-MediumPost~reddit-components-NotificationUnit-Button~removal~87f825ba.1f6f4cdd3ba5ffd0749d.js" key="https://www.redditstatic.com/desktop2x/Reddit~RichTextEditor~reddit-components-MediumPost~reddit-components-NotificationUnit-Button~removal~87f825ba.1f6f4cdd3ba5ffd0749d.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/Governance~ModListing~Reddit~ReportFlow.92dc6832eb65b153b9f8.js" key="https://www.redditstatic.com/desktop2x/Governance~ModListing~Reddit~ReportFlow.92dc6832eb65b153b9f8.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/Chat~Governance~Reddit.daa21bfdc4bf6b1b0d2d.js" key="https://www.redditstatic.com/desktop2x/Chat~Governance~Reddit.daa21bfdc4bf6b1b0d2d.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/Governance~Reddit~SubredditForkingCTA.b7769f2f45dab828f630.js" key="https://www.redditstatic.com/desktop2x/Governance~Reddit~SubredditForkingCTA.b7769f2f45dab828f630.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/Governance~ModListing~Reddit.20ff93da9585bdd58793.js" key="https://www.redditstatic.com/desktop2x/Governance~ModListing~Reddit.20ff93da9585bdd58793.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/ModListing~Reddit~StandalonePostPage.bd37319a4f78703e6421.js" key="https://www.redditstatic.com/desktop2x/ModListing~Reddit~StandalonePostPage.bd37319a4f78703e6421.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/Governance~Reddit.ed393a9e80733c2bca28.js" key="https://www.redditstatic.com/desktop2x/Governance~Reddit.ed393a9e80733c2bca28.js" rel="preload"><link as="script" href="https://www.redditstatic.com/desktop2x/Reddit.e0ee6b3e4f217f451152.js" key="https://www.redditstatic.com/desktop2x/Reddit.e0ee6b3e4f217f451152.js" rel="preload">
        <link rel="apple-touch-icon" sizes="57x57" href="https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-57x57.png"><link rel="apple-touch-icon" sizes="60x60" href="https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-60x60.png"><link rel="apple-touch-icon" sizes="72x72" href="https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-72x72.png"><link rel="apple-touch-icon" sizes="76x76" href="https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-76x76.png"><link rel="apple-touch-icon" sizes="114x114" href="https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-114x114.png"><link rel="apple-touch-icon" sizes="120x120" href="https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-120x120.png"><link rel="apple-touch-icon" sizes="144x144" href="https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-144x144.png"><link rel="apple-touch-icon" sizes="152x152" href="https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-152x152.png"><link rel="apple-touch-icon" sizes="180x180" href="https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-180x180.png"><link rel="icon" type="image/png" sizes="192x192" href="https://www.redditstatic.com/desktop2x/img/favicon/android-icon-192x192.png"><link rel="icon" type="image/png" sizes="32x32" href="https://www.redditstatic.com/desktop2x/img/favicon/favicon-32x32.png"><link rel="icon" type="image/png" sizes="96x96" href="https://www.redditstatic.com/desktop2x/img/favicon/favicon-96x96.png"><link rel="icon" type="image/png" sizes="16x16" href="https://www.redditstatic.com/desktop2x/img/favicon/favicon-16x16.png"><link rel="manifest" href="https://www.redditstatic.com/desktop2x/img/favicon/manifest.json?v=2"><meta name="msapplication-TileColor" content="#ffffff"><meta name="msapplication-TileImage" content="https://www.redditstatic.com/desktop2x/img/favicon/ms-icon-144x144.png"><meta name="theme-color" content="#FFFFFF" data-reactroot="">
        <meta name="jsapi">
  
      <title>reddit.com: search results - photo</title><meta name="robots" content="noindex"><meta name="description" content="r/androidapps: A subreddit dedicated to Android apps."><meta property="og:ttl" content="600"><meta property="og:site_name" content="reddit"><meta property="twitter:site" content="@reddit"><meta property="twitter:card" content="summary">
      
    <script charset="utf-8" src="https://www.redditstatic.com/desktop2x/SearchResults.67903249620c41190639.js"></script><style class="" data-href="chunkCSS/CollectionCommentsPage~CommentsPage~CountryPage~FramedGild~GildModal~GovernanceReleaseNotesModal~Hap~a5d6a3b8.10dbe47c974d014d6ce6_.css">._20iR16Ub7Vl1C-DCuvSdMB{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-align:center;align-items:center;padding:4px 8px;z-index:1;-ms-grid-column-align:center;justify-items:center;position:absolute;height:24px;left:8px;top:8px;background:rgba(0,0,0,.57);border-radius:99px;color:#fff}._20iR16Ub7Vl1C-DCuvSdMB:hover{background:rgba(0,0,0,.65)}._1zWeP05d23MUl79DcPqjpV{margin-right:4px}
._1Wd26c2ichqUxeZVJStEJT{position:absolute;top:50%;left:50%;margin-top:-44px;margin-left:-44px;height:88px;width:88px;z-index:10}
.eI6Ep6BNFA5DZjPWNVb4O{fill:#fff;height:50px;width:50px}
._2XQ3ZY6qCbEm9_WtvLLFru{height:50px;width:50px;opacity:.95;transition:all .1s linear}.vLH0XV-l8Y4mNGUvw4HHy{position:absolute;top:50%;left:50%;margin-left:-30px;margin-top:-30px;z-index:11}.vLH0XV-l8Y4mNGUvw4HHy:hover ._2XQ3ZY6qCbEm9_WtvLLFru{opacity:1}.vLH0XV-l8Y4mNGUvw4HHy:active ._2XQ3ZY6qCbEm9_WtvLLFru{transform:scale(.9)}
._1chxf6wi6yizUXVYKuz67P{position:absolute;left:0;top:0;width:100%;height:100%;filter:blur(20px) brightness(.8)}
._3YDPJHFl8YQG4TIAGQwHwK{position:absolute;height:100%;left:0;right:0;bottom:0;background:linear-gradient(180deg,transparent,rgba(0,0,0,.5))}
._2MDmJfq0z5K-d2xH--GnRU{border-radius:50%;bottom:0;height:16px;top:0;transition:opacity .2s ease-out;width:16px}._3fnsfWuIyofBJBBCbeOZzM,._2MDmJfq0z5K-d2xH--GnRU{background:#0079d3;position:absolute}._3fnsfWuIyofBJBBCbeOZzM{width:100%;top:6px;height:4px;border-radius:2px}.AZ2rAoFxu6aiCBbBq02Sr{position:absolute;bottom:20px;left:0;display:-ms-flexbox;display:flex;-ms-flex-flow:column nowrap;flex-flow:column nowrap;visibility:hidden}.V26VfIGfGxnmQGCoWYGY7{height:54px;width:96px;background:#000;border:1px solid #545452}._2PInUKITfsesytaTfWfG42{-ms-flex-item-align:center;-ms-grid-row-align:center;align-self:center;margin-top:5px;padding:0 5px;height:20px;background:rgba(0,0,0,.6);border-radius:4px;font-family:Helvetica;font-size:12px;line-height:20px;color:#fff}._3-Dc7BBLD7JWsyF3pV-rsH{position:relative;-ms-flex-positive:1;flex-grow:1;margin:auto 8px;height:16px;cursor:pointer}._3-Dc7BBLD7JWsyF3pV-rsH:active .AZ2rAoFxu6aiCBbBq02Sr,._3-Dc7BBLD7JWsyF3pV-rsH:hover .AZ2rAoFxu6aiCBbBq02Sr{visibility:visible;display:-ms-flexbox;display:flex}._2uVDwsKlmWPhYjwe_hYwKZ{height:100%}._4UI_04IgDx06P4biEkiF3{position:absolute;top:6px;height:4px;border-radius:2px}._4UI_04IgDx06P4biEkiF3,._4UI_04IgDx06P4biEkiF3._2uPlpBWBrO4n82P3YvBGF_{width:100%}._2uPlpBWBrO4n82P3YvBGF_{background:#fff;opacity:.2}.l8jnP9bxmZRCAmhfPBTa1{background:#fff;opacity:.5}._169ZVSyFxp9z4y1H0OYA7w{background:#fff;opacity:.7}._3LxsYVQvMOr6phpuWaScdt{background:#0079d3}.YTPNvBfuKbdKUEJL6hPJT{background:#ea0027}
.sm5fCodJsfJ3dJgv8LoJU{width:36px;height:36px}.sm5fCodJsfJ3dJgv8LoJU,._1JylLL_Ux6Orq3W6Gpj0I5{display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;-ms-flex-align:center;align-items:center}._1JylLL_Ux6Orq3W6Gpj0I5{height:24px;width:24px}.sm5fCodJsfJ3dJgv8LoJU:hover ._1JylLL_Ux6Orq3W6Gpj0I5{background:#fd471e;border-radius:12px}
._1BLNYd_poiSXsApjISxu_9{font-size:12px;font-weight:500;line-height:16px;position:absolute;visibility:hidden;height:auto;width:auto;bottom:50%;margin-bottom:20px;padding:8px;background:#000;border-radius:4px;color:#fff;white-space:nowrap}._7xWC34a6DkOCXgS96vOSO{position:relative}._7xWC34a6DkOCXgS96vOSO ._2BgDJndeb40Gp_YvmIR_81:hover ._1BLNYd_poiSXsApjISxu_9,.using-keys ._7xWC34a6DkOCXgS96vOSO ._2BgDJndeb40Gp_YvmIR_81:focus-within ._1BLNYd_poiSXsApjISxu_9{visibility:visible}._7xWC34a6DkOCXgS96vOSO ._2BgDJndeb40Gp_YvmIR_81:hover:after,.using-keys ._7xWC34a6DkOCXgS96vOSO ._2BgDJndeb40Gp_YvmIR_81:focus-within:after{content:"";position:absolute;left:50%;bottom:50%;transform:translate(-50%,3px);margin-bottom:20px;border:solid;border-color:#000 transparent;border-width:3px 3px 0}
._3IYkqm44eWg992tFnELzuW{height:96px;width:24px;border-radius:4px;background-color:rgba(0,0,0,.6);cursor:pointer;position:relative;left:50%;transform:translateX(-50%)}._1iy-RNoDbjuTYxfwaLdPRO{width:4px;border-radius:2px;position:absolute;margin:0 auto;left:0;right:0}.gzyVgIvE9b8wMmHefFf6i{background-color:hsla(0,0%,100%,.5);top:8px;bottom:8px;margin:6px auto}._2mdWr-OXgnLh-fdDgEEb6E{background-color:#0079d3;height:100%;bottom:0}._2mdWr-OXgnLh-fdDgEEb6E._2GyJbEWZL04QA2bbVtv_Qu{background-color:#ea0027}._320cReGqgLhY1pPA-fM8Z7{position:absolute;left:-4px;top:-6px;margin-left:auto;margin-right:auto;width:12px;height:12px;background-color:#fff;border-radius:50%;box-shadow:0 0 6px 0 rgba(0,0,0,.5)}
._2rtFq5-gNnsnqTzEcTSmVx,._3MU1RfVON0x2Jtnz9Zq3FA,._1mDDkogVo82R5-IFxvyPRX{position:relative;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;height:100%;margin:0;outline:none;z-index:4}._3KjMjt45Pg4_LoShJNFMEf svg,._2c7UOdkceyJz77qZPoGPAL svg,._3uhleNVV7YkJm0tszcz4z9 svg,._3ly5pJnuzH6jga1JGXpOXD svg,.fqsG3oqeIwcEC-HTRf23d svg,._2Zt53GmI1y_S0N7pA0jMc0 svg,._2W9KLflUho3xU7KURAaHwH svg{display:block;height:18px;width:18px;fill-opacity:.95;cursor:pointer;transition:all .2s linear}._3KjMjt45Pg4_LoShJNFMEf svg:hover,._2c7UOdkceyJz77qZPoGPAL svg:hover,._3uhleNVV7YkJm0tszcz4z9 svg:hover,._3ly5pJnuzH6jga1JGXpOXD svg:hover,.fqsG3oqeIwcEC-HTRf23d svg:hover,._2Zt53GmI1y_S0N7pA0jMc0 svg:hover,._2W9KLflUho3xU7KURAaHwH svg:hover{fill-opacity:1}._3KjMjt45Pg4_LoShJNFMEf svg:active,._2c7UOdkceyJz77qZPoGPAL svg:active,._3uhleNVV7YkJm0tszcz4z9 svg:active,._3ly5pJnuzH6jga1JGXpOXD svg:active,.fqsG3oqeIwcEC-HTRf23d svg:active,._2Zt53GmI1y_S0N7pA0jMc0 svg:active,._2W9KLflUho3xU7KURAaHwH svg:active{transform:scale(.9)}._2Zt53GmI1y_S0N7pA0jMc0{margin-left:4px;margin-right:0}._2Zt53GmI1y_S0N7pA0jMc0 svg{height:auto;width:auto}._1z-qg2gzYKkI37gkYYJCi0{color:#fff;font-family:verdana;font-size:12px;font-variant-numeric:tabular-nums;white-space:nowrap;margin:0 1em}._1s8L9kNAgwvsmhnrpHl4Ef{-ms-flex:0 0 40px;flex:0 0 40px;height:24px;border-radius:12px;padding:6px 0;margin:auto 0;background-color:#ea0027;font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-align:center;text-transform:uppercase;letter-spacing:.25px;color:#fff;cursor:pointer}._3YQsKErciDXsBNWhb0bzul{position:relative;-ms-flex-positive:1;flex-grow:1;margin:auto;width:100%;height:auto}._2W9KLflUho3xU7KURAaHwH ._3nTkqMMtsoqxVmhplDRef3{display:block;position:absolute;margin:0;height:96px;width:24px;bottom:100%;opacity:0;visibility:hidden;transition:visibility 0s ease-out .2s,opacity .2s ease-out}._2W9KLflUho3xU7KURAaHwH ._3nTkqMMtsoqxVmhplDRef3:before{position:absolute;content:"";height:100%;width:36px;top:0;left:50%;transform:translateX(-50%)}._2W9KLflUho3xU7KURAaHwH:active ._3nTkqMMtsoqxVmhplDRef3,._2W9KLflUho3xU7KURAaHwH:hover ._3nTkqMMtsoqxVmhplDRef3{opacity:1;visibility:visible;transition-delay:0s}._3KjMjt45Pg4_LoShJNFMEf button[aria-expanded=true] .X3KvZpgZg_2f0etJY2Ba7{transform:rotate(45deg)}._3KjMjt45Pg4_LoShJNFMEf button[aria-expanded=true] .X3KvZpgZg_2f0etJY2Ba7:active{transform:rotate(45deg) scale(.9)}._3KjMjt45Pg4_LoShJNFMEf ._1s7GuSZPqjgn0QP60a6asr{position:absolute;display:block;padding:5px;height:auto;width:auto;bottom:0;left:50%;transform:translate(-50%,-32px)}.gUpEQXQu8G8UvISmBIPsj{position:absolute;display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;-ms-flex-align:end;align-items:flex-end;height:36px;bottom:0;left:0;right:0;-webkit-user-select:none;-ms-user-select:none;user-select:none;padding:8px}.gUpEQXQu8G8UvISmBIPsj._35yCa6dYJNzUGsRDLtEoWU{-ms-flex-pack:end;justify-content:flex-end}.gUpEQXQu8G8UvISmBIPsj>*{transition:opacity .2s cubic-bezier(.4,0,.2,1)}.gUpEQXQu8G8UvISmBIPsj._1RZSSlyqzokrcxh0ESwE2e>:not(._2W9KLflUho3xU7KURAaHwH){opacity:0}._15cvJJTKClcHJuPN2mcpY4{width:36px;height:36px;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;-ms-flex-align:center;align-items:center}
._2XC4hSYLNzvTJ9n8Qx5t2E{opacity:0;visibility:hidden;transition:visibility 0s ease-out .2s,opacity .2s ease-out}._2XC4hSYLNzvTJ9n8Qx5t2E.KE4seaOPBFBF1jhkJyWzD{opacity:1;visibility:visible;transition-delay:0s}.C_R5GVVZDJEPfB_2ZVw_j{position:relative;border-radius:4px;background-color:rgba(0,0,0,.6)}._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z,._2BOpKj2--T_MqNo_ZMRxNG .bAXkjkzl_SYFOHtU-04DK,._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z,._3IZDbV1r5OQ2PtnsjF02A .bAXkjkzl_SYFOHtU-04DK{cursor:pointer;display:-ms-flexbox;display:flex;opacity:.5;text-align:left;white-space:nowrap}._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z svg,._2BOpKj2--T_MqNo_ZMRxNG .bAXkjkzl_SYFOHtU-04DK svg,._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z svg,._3IZDbV1r5OQ2PtnsjF02A .bAXkjkzl_SYFOHtU-04DK svg{height:12px;width:12px;margin:4px 0 0 2px;visibility:hidden}._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z ._2NY4rl5z4S5VUOfEs8PdJ_,._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z ._1n_g7VROCpBaLnT_3bzFIL,._2BOpKj2--T_MqNo_ZMRxNG .bAXkjkzl_SYFOHtU-04DK ._2NY4rl5z4S5VUOfEs8PdJ_,._2BOpKj2--T_MqNo_ZMRxNG .bAXkjkzl_SYFOHtU-04DK ._1n_g7VROCpBaLnT_3bzFIL,._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z ._2NY4rl5z4S5VUOfEs8PdJ_,._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z ._1n_g7VROCpBaLnT_3bzFIL,._3IZDbV1r5OQ2PtnsjF02A .bAXkjkzl_SYFOHtU-04DK ._2NY4rl5z4S5VUOfEs8PdJ_,._3IZDbV1r5OQ2PtnsjF02A .bAXkjkzl_SYFOHtU-04DK ._1n_g7VROCpBaLnT_3bzFIL{display:block;width:100%;margin:2px 2px 2px 5px;color:#fff;font-size:12px;line-height:16px}._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z .UyJedjQe5dUxEFYt6pF_G,._2BOpKj2--T_MqNo_ZMRxNG .bAXkjkzl_SYFOHtU-04DK .UyJedjQe5dUxEFYt6pF_G,._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z .UyJedjQe5dUxEFYt6pF_G,._3IZDbV1r5OQ2PtnsjF02A .bAXkjkzl_SYFOHtU-04DK .UyJedjQe5dUxEFYt6pF_G{font-weight:700;color:#0079d3}._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z:focus,._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z:hover,._2BOpKj2--T_MqNo_ZMRxNG .bAXkjkzl_SYFOHtU-04DK:focus,._2BOpKj2--T_MqNo_ZMRxNG .bAXkjkzl_SYFOHtU-04DK:hover,._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z:focus,._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z:hover,._3IZDbV1r5OQ2PtnsjF02A .bAXkjkzl_SYFOHtU-04DK:focus,._3IZDbV1r5OQ2PtnsjF02A .bAXkjkzl_SYFOHtU-04DK:hover{opacity:.75}._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z[aria-checked=true],._2BOpKj2--T_MqNo_ZMRxNG .bAXkjkzl_SYFOHtU-04DK[aria-checked=true],._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z[aria-checked=true],._3IZDbV1r5OQ2PtnsjF02A .bAXkjkzl_SYFOHtU-04DK[aria-checked=true]{opacity:1}._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z[aria-checked=true] svg,._2BOpKj2--T_MqNo_ZMRxNG .bAXkjkzl_SYFOHtU-04DK[aria-checked=true] svg,._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z[aria-checked=true] svg,._3IZDbV1r5OQ2PtnsjF02A .bAXkjkzl_SYFOHtU-04DK[aria-checked=true] svg{visibility:visible}._2BOpKj2--T_MqNo_ZMRxNG ._3FgC5gbpQJUntY23YtQ89Z,._3IZDbV1r5OQ2PtnsjF02A ._3FgC5gbpQJUntY23YtQ89Z{border-bottom:1px solid #030303;padding-bottom:3px}
._2g633AWSIbFBLBxPXC882A{position:absolute;top:40%;left:5%;right:5%;z-index:10;padding:12px;text-align:center;white-space:normal}._2g633AWSIbFBLBxPXC882A p{color:#fff;padding:4px}
._1x0QJr7iXMkiGpOnQbAvYN{fill:#fff;height:50px;width:50px}
._11XLCF2uLCEj35_lDddpNT{fill:#fff;height:50px;width:50px}
.Ui8OEQfWnkN9BO2o-qSXV{fill:#fff;height:50px;width:50px}
.o2NVVhdZrQ3VeGMHO8aA0{fill:#fff;height:50px;width:50px}
._3DFi9BDKHWFWnty75sJhyJ{fill:#fff;height:50px;width:50px}
._1PkP2GybP9Bh6mN4gmbPN4{fill:#fff;height:50px;width:50px}
._1EfHCA6m0dIgLYzGW2aor1{fill:#fff;height:50px;width:50px}
.G2_89gx6TwcALtRI4k7hc{fill:#fff;height:50px;width:50px}
._2kG3YOJULmYUC8YtVtNO9J{fill:#fff;height:50px;width:50px}
._1NxifIlpri3Af8fEoxkaUr{fill:#fff;height:50px;width:50px}
._2X_GdgwreX3clU-MfCHx-Y{fill:#fff;height:50px;width:50px}
.egx9Z9oH6-wpjLKKhAEoM{fill:#fff;height:50px;width:50px}
._2FH_xFiDZCFtYKBJAmSpeD:hover{text-decoration:none}._3uyGw8SwblJ37jvDUd-0Z_{font-size:12px;font-weight:700;letter-spacing:.5px;line-height:24px;text-transform:uppercase;-ms-flex-align:center;align-items:center;color:#fff;text-align:center;margin-left:10px}._3uyGw8SwblJ37jvDUd-0Z_,._267SSeon8aryjeoh4UclX8{display:-ms-flexbox;display:flex}._267SSeon8aryjeoh4UclX8{-ms-flex-pack:inherit;justify-content:inherit;margin-top:20px}
._3N5UJK0Os17icJ33e54tfY{fill:#fff;height:50px;width:50px}
._241TIL5Gnyx3yLobU95FlI{height:auto;width:auto;opacity:.95;transition:all .1s linear}._241TIL5Gnyx3yLobU95FlI:hover{opacity:1}._3G7xHJZQMrQlpjhNDQI2fe{position:absolute;display:-ms-flexbox;display:flex;height:100%;width:100%;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;background:rgba(0,0,0,.4);opacity:1;transition:all .2s ease-in-out;cursor:pointer}._3G7xHJZQMrQlpjhNDQI2fe:active ._241TIL5Gnyx3yLobU95FlI{transform:scale(.9)}.qDCxOHuaGNjcgDp5-rvJr{font-size:12px;font-weight:700;letter-spacing:.5px;line-height:24px;text-transform:uppercase;margin-left:10px;color:#fff;text-align:center}._2KpvSaYm8FNb5KzZzf4-TO,.qDCxOHuaGNjcgDp5-rvJr{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center}._2KpvSaYm8FNb5KzZzf4-TO{-ms-flex-pack:center;justify-content:center}
._2UrTEvz_DRsDezLCxNpGnZ{max-width:100%;max-height:100%;position:relative}._2UrTEvz_DRsDezLCxNpGnZ.ziid7jHsA37M8sq6Set2x{visibility:hidden}
._3UEq__yL-82zX4EyuluREz{position:absolute;top:0;bottom:0;left:0;right:0}
._3QOPLw8PZipW3i8kDxod81{height:100%;-webkit-user-select:none;-ms-user-select:none;user-select:none;cursor:default;white-space:nowrap;overflow:hidden}._3QOPLw8PZipW3i8kDxod81:after{display:block;content:"";padding-top:56.25%;pointer-events:none}._1znUHTb50VqdFqfWmai1ts{height:100vh;width:100vw;position:absolute;top:0;right:0;bottom:0;left:0;transform:none;background-color:#000}._3QOPLw8PZipW3i8kDxod81:not(.using-keys) [tabindex],._3QOPLw8PZipW3i8kDxod81:not(.using-keys) button{outline:none}._6p8buRs-LijHSXx1H4MGe::-webkit-media-controls-enclosure{display:none!important}.zRGpGBNtA_hojI_RK9ouQ{-webkit-user-select:none;-ms-user-select:none;user-select:none;width:100%;height:auto;position:absolute;top:50%;transform:translateY(-50%);left:0;z-index:0;overflow:hidden;object-fit:contain}._6p8buRs-LijHSXx1H4MGe{max-width:100vw;max-height:100vh;height:auto;left:50%;margin:0 auto;top:50%;transform:translate(-50%,-50%)}._6p8buRs-LijHSXx1H4MGe,._1EQJpXY7ExS04odI1YBBlj{background-position:50%;background-repeat:no-repeat;background-size:contain;position:absolute;-webkit-video-playable-inline:true;width:100%}._1EQJpXY7ExS04odI1YBBlj{z-index:0;height:100%;top:0;left:0}._14LIEiRn-naKqUT7DJ8vwV{background-position:50%;background-repeat:no-repeat;background-size:contain}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/CollectionCommentsPage~CommentsPage~CountryPage~FramedGild~GildModal~GovernanceReleaseNotesModal~Hap~a5d6a3b8.10dbe47c974d014d6ce6_.css.map*/</style><style class="" data-href="chunkCSS/CollectionCommentsPage~CommentsPage~CountryPage~FramedGild~GildModal~GovernanceReleaseNotesModal~Hap~cb450973.574222e94257c4de6a11_.css">._3dhFVFchWAAFXfLFTa94n9{display:block;height:0;margin-bottom:-1em;overflow:hidden}._1NSbknF8ucHV2abfCZw2Z1{display:contents}._1NSbknF8ucHV2abfCZw2Z1._1Q2mF3u7v9hBVu_4bkC7R4{display:none}._3ozFpM1W8BRdrzkr_ssGxZ{overflow:hidden}._18_METUBD2i2iqGBz4ofw1._18_METUBD2i2iqGBz4ofw1{width:auto;height:176px}._3jrT7JqZwfGWyxKf4SYuRj{-ms-flex-align:center;align-items:center;bottom:0;display:-ms-flexbox;display:flex;height:100%;-ms-flex-pack:center;justify-content:center;left:0;pointer-events:none;position:absolute;right:0;top:0;width:100%;z-index:50}._2bcjL-4RRFQN5OUQMrcioo{background:none;border:1px solid #fff;color:#fff;padding:10px 20px;position:absolute;text-transform:uppercase}
._3K6DCjWs2dQ93YYZDOHjib{display:block;position:relative}
._3Oa0THmZ3f5iZXAQ0hBJ0k{position:relative;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center}._3Oa0THmZ3f5iZXAQ0hBJ0k.WjuR4W-BBrvdtABBeKUMx{-ms-flex-pack:left;justify-content:left}._2_tDEnGMLxpM6uOa2kaDB3{display:block;max-width:100%;position:relative;background-color:var(--newCommunityTheme-post)}._2_tDEnGMLxpM6uOa2kaDB3._1XWObl-3b9tPy64oaG6fax{margin:0 auto}._2_tDEnGMLxpM6uOa2kaDB3._3oBPn1sFwq76ZAxXgwRhhn{filter:blur(60px);width:100%;height:100%}._2_tDEnGMLxpM6uOa2kaDB3.vgwLfcw0MneE2ejmdh_l9{max-width:240px;max-height:240px;min-width:20px;min-height:20px;object-fit:cover;border-radius:4px}._3hUbl08LBz2mbXjy0iYhOS{font-size:12px;font-weight:700;letter-spacing:.5px;line-height:24px;text-transform:uppercase;background-color:rgba(80,85,87,.8);border-radius:4px;bottom:16px;color:#fff;line-height:32px;position:absolute;text-align:center;text-decoration:none;width:320px;left:50%;transform:translate(-50%)}._3m20hIKOhTTeMgPnfMbVNN{position:relative}
._2iaYXFpGyyEGq1rp02cl5w{filter:blur(20px) brightness(.8);height:100%;left:0;position:absolute;top:0;transform:scale(1.3);width:100%}.m3aNC6yp8RrNM_-a0rrfa{position:relative;background:var(--newCommunityTheme-activeTinted05);max-height:512px}.m3aNC6yp8RrNM_-a0rrfa._1fptM9wVD8i598KW_RjLWO{max-height:none}@media (max-width:calc(960px - 1px)){.m3aNC6yp8RrNM_-a0rrfa._3PIKVMCKdveCEcyiKr43sU{max-height:652px}}._3gBRFDB5C34UWyxEe_U6mD{pointer-events:none;width:100%}._3JgI-GOrkmyIeDeyzXdyUD{position:absolute;top:0;left:0;bottom:0;right:0}._3JgI-GOrkmyIeDeyzXdyUD._2CSlKHjH7lsjx0IpjORx14{background:var(--newCommunityTheme-body)}._3JgI-GOrkmyIeDeyzXdyUD._1fptM9wVD8i598KW_RjLWO{position:relative}
._3spkFGVnKMHZ83pDAhW3Mx{display:-ms-flexbox;display:flex;width:100%;height:100%}._3spkFGVnKMHZ83pDAhW3Mx ._2WxICCKdnGu7x2n4CBv6zE{max-width:240px;max-height:240px;min-width:20px;min-height:20px;object-fit:cover;border-radius:4px}._2b68Lt6xHaLir5082LDDA9{-ms-flex-pack:center;justify-content:center}.tErWI93xEKrI2OkozPs7J{display:block;height:100%;max-width:100%;position:relative}
._7T4UafM1PdBGycd5na9nF{font-size:22px;line-height:26px}._7T4UafM1PdBGycd5na9nF,._1WODZhR-x-fbMu3MOL9cH1{font-family:Noto Sans,Arial,sans-serif;font-weight:400;margin-bottom:8px;margin-top:1.4em}._1WODZhR-x-fbMu3MOL9cH1{font-size:20px;line-height:24px}.WFFrvt6_3z5B7MBcYKr8U{font-size:18px;line-height:22px}.WFFrvt6_3z5B7MBcYKr8U,._2UlSUuiYR4BRv_FiLxCcu9{font-family:Noto Sans,Arial,sans-serif;font-weight:400;margin-bottom:8px;margin-top:1.4em}._2UlSUuiYR4BRv_FiLxCcu9{font-size:16px;line-height:20px}.hnYPKCNkyo9X6QpCXHj1I{font-size:14px;line-height:18px}.hnYPKCNkyo9X6QpCXHj1I,._1ceLNhXCFZ1_Lj9Th4go_C{font-family:Noto Sans,Arial,sans-serif;font-weight:400;margin-bottom:8px;margin-top:1.4em}._1ceLNhXCFZ1_Lj9Th4go_C{font-size:12px;line-height:16px}._2ACwpV3Y0LKhHHKbsxNmmY{border:0;border-top:1px solid var(--newCommunityTheme-bodyTextAlpha20);height:1px;margin:8px 0}._34q3PgLsx9zIU5BiSOjFoM{font-family:Noto Mono,Menlo,Monaco,Consolas,monospace;font-size:13px;font-weight:400;line-height:20px;color:var(--newRedditTheme-monospaceColor);margin:0 2px}._34q3PgLsx9zIU5BiSOjFoM,._3GnarIQX9tD_qsgXkfSDz1{background:var(--newRedditTheme-field);max-width:100%;overflow:auto}._3GnarIQX9tD_qsgXkfSDz1{display:-ms-grid;display:grid;line-height:1.4;margin:4px 0;padding:8px}._3GnarIQX9tD_qsgXkfSDz1>._34q3PgLsx9zIU5BiSOjFoM{background-color:transparent;color:var(--newRedditTheme-bodyText);margin:0}._28lDeogZhLGXvE95QRPeDL{border-left:4px solid var(--newCommunityTheme-bodyTextAlpha20);margin:4px 0 4px 8px;padding-left:8px}._1qeIAgB0cPwnLhDF9XSiJM{padding:.8em 0 .25em}._1qeIAgB0cPwnLhDF9XSiJM:first-child{padding-top:0}._1qeIAgB0cPwnLhDF9XSiJM:last-child{padding-bottom:0}._3gqTEjt4x9UIIpWiro7YXz{margin:.4em 1em}._3gqTEjt4x9UIIpWiro7YXz ._1qeIAgB0cPwnLhDF9XSiJM{padding:0}._33MEMislY0GAlB78wL1_CR{list-style:disc outside;margin:4px 0 4px 8px}._33MEMislY0GAlB78wL1_CR ._33MEMislY0GAlB78wL1_CR{list-style-type:circle}._33MEMislY0GAlB78wL1_CR ._33MEMislY0GAlB78wL1_CR ._33MEMislY0GAlB78wL1_CR{list-style-type:square}._1eJr7K139jnMstd4HajqYP{list-style:decimal outside;margin:4px 0 4px 8px}._1eJr7K139jnMstd4HajqYP ._1eJr7K139jnMstd4HajqYP{list-style-type:lower-alpha}._1eJr7K139jnMstd4HajqYP ._1eJr7K139jnMstd4HajqYP ._1eJr7K139jnMstd4HajqYP{list-style-type:lower-roman}._12FoOEddL7j_RgMQN0SNeU{font-weight:700}._7s4syPYtk5hfUIjySXcRE{font-style:italic}.HoWuCifWxDx-PnwllGmZd{text-decoration:underline}._2aQztsTwdz2uTN4arsyBD6{bottom:-.4em}._2aQztsTwdz2uTN4arsyBD6,._1jsgSPRO0cMQfs1UZrSovE{position:relative;font-size:.7em;line-height:.7em}._1jsgSPRO0cMQfs1UZrSovE{top:-.4em}.MRH-njmSb5ZTkfb1o4dqv{border:2px solid #eee;border-collapse:collapse;display:inline-block;margin-bottom:4px;margin-top:4px;overflow-x:auto;word-break:normal}.s6JZe6869f81l9E_5G7Q9{background-color:var(--newCommunityTheme-bodyAlpha80);border:1px solid #eee}._3DYfYn_cczg1wj_a3hhyV6{background-color:var(--newCommunityTheme-bodyAlpha80);text-align:left}._1LHijgw3WoeCUe8AUewfUB,._3DYfYn_cczg1wj_a3hhyV6{border:1px solid #eee;color:var(--newCommunityTheme-bodyText);padding:4px 8px}._1LHijgw3WoeCUe8AUewfUB{text-align:center}._3DqGFKR55y45L5IxBTgsFz{text-align:right}._3DqGFKR55y45L5IxBTgsFz,._4uv59XIILEFm6V3BmtSuR{border:1px solid #eee;color:var(--newCommunityTheme-bodyText);padding:4px 8px}._4uv59XIILEFm6V3BmtSuR{text-align:left}._3TNkDptlyGOiWXvdX_acOB{text-align:center}._3TNkDptlyGOiWXvdX_acOB,._1AUCpXmm3maPuEbUSe90Y8{border:1px solid #eee;color:var(--newCommunityTheme-bodyText);padding:4px 8px}._1AUCpXmm3maPuEbUSe90Y8{text-align:right}._3t5uN8xUmg0TOwRCOGQEcU,._3t5uN8xUmg0TOwRCOGQEcU:visited{color:var(--newCommunityTheme-linkText);text-decoration:underline}
.voEElhHVrm-yKZcIbBmik{display:block}._1gg1MfJZaNkaPmqHpGQHni{max-height:175px;max-width:512px;border-radius:8px}._1gg1MfJZaNkaPmqHpGQHni:first-child{padding-top:4px}.U76N5pdhVpwLUkKv0jpDZ{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;padding-top:4px}.lhXj5Lw1-62CSn58uodEt{transform:translateX(-2px)}.WZIEUuvYX30GAtLJofhDk{margin-left:8px;color:#787c7e;font-size:12px}.WZIEUuvYX30GAtLJofhDk a{color:var(--newCommunityTheme-linkText);margin-right:5px;text-decoration:none}
._1PlxnYkerei9iGJsL9JyrP{display:block}._2LjgQiHLCZ9LDbCQx5KaOi{margin-top:16px}._2-UiOdhyj4wHBv7Rc2FeDr{margin:24px 0}._2-UiOdhyj4wHBv7Rc2FeDr.c1cmiB1jfdq4sxidlPDAx{margin-bottom:0}._2-UiOdhyj4wHBv7Rc2FeDr._1yyTGHoIL7vZ6fNJ2-s3dL{margin:6px 0 12px}._2R6TbsJdSgxwd1OzbbrIjl{margin-top:8px}._2R6TbsJdSgxwd1OzbbrIjl:first-child{margin-top:2px}.FJNSiirwoPtG58aeGw2Jx{margin-bottom:24px;font-size:.8em;text-align:center}._2-H7KMbqeJxA6VjyAX4GMX{background-color:var(--newCommunityTheme-inactive);border-radius:4px;padding-bottom:56%;position:relative;width:100%;margin-bottom:20px}._2-H7KMbqeJxA6VjyAX4GMX:after{bottom:8px;content:var(--placeholder-content-text,"");font-size:.9em;left:16px;position:absolute}._2-H7KMbqeJxA6VjyAX4GMX._18dflNtNlz_sHfoBK19VZn{width:175px;height:175px;padding-bottom:0;margin:6px 0}._2-H7KMbqeJxA6VjyAX4GMX._2O6ZaJBTx6OGys4GI6Egy-{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:distribute;justify-content:space-around}
.JnJcJlA7hHeajn8Um_Bh5{display:inline-block;vertical-align:middle;line-height:100%;margin:0 2px}
._3mIYu0jAt23sIWGr4pFcI{opacity:0;transition:opacity 1s ease-out}._2XOXS9oLSigrX7LIefjqhe:before{content:"";position:absolute;visibility:hidden}._2v4IIjPhKL0PDaWaWtjJ1E{background:#545452;border-radius:2px;transition:background 1s ease-out}._2v4IIjPhKL0PDaWaWtjJ1E:not(._15VS32zBYFUDI5ssldQhEK){cursor:pointer}._2v4IIjPhKL0PDaWaWtjJ1E._15VS32zBYFUDI5ssldQhEK{background:rgba(84,84,82,.1)}._2v4IIjPhKL0PDaWaWtjJ1E._15VS32zBYFUDI5ssldQhEK ._3mIYu0jAt23sIWGr4pFcI{opacity:1}._3CBmNG6xIaLHHh1ts_10tN{animation-duration:.1s}._3CBmNG6xIaLHHh1ts_10tN:after{left:10px}
.Zwo7CZoszMU6kBYhWyIC7{background-color:var(--newCommunityTheme-field);border-radius:.8em;padding-right:.2em;padding-left:.8em;color:var(--newCommunityTheme-linkText);display:inline;text-decoration:none}.Zwo7CZoszMU6kBYhWyIC7:hover{text-decoration:underline}._33bYVIxJlbFcqiiYlexnqp{max-width:100%;display:block;border:1px}
._2Pw8j7a2DYkjTDOFbIdODA{font-size:12px;font-weight:400;line-height:16px;color:var(--newCommunityTheme-metaText);padding-left:12px;margin-bottom:-4px}._2ktYI4-r7C-HaMk9ulbwog{width:364px}._3rKUrAbYNFvE7-nMDs6lwZ{fill:var(--newCommunityTheme-metaText);height:14px;padding-right:4px;vertical-align:bottom;width:12px}._1e2szH8g0XMMM_EuCN8Olk{position:relative}._3kpwADnYG-SH40aaSdX3ZE{position:relative;height:1em;width:1em;display:inline-block;vertical-align:middle;margin-left:-.6em;margin-right:.2em;margin-bottom:.1em}
._1JFRpTrF6njlI0ABgMOrZ4{position:relative;overflow:hidden;display:-ms-grid;display:grid;width:calc(150px*var(--expression-width));height:calc(150px*var(--expression-height))}.I5Xb2tM-BRe5nhJwCv1vE{position:absolute;display:-ms-flexbox;display:flex;top:calc(150px*var(--avatar-position-top));height:calc(150px*var(--avatar-position-height));width:calc(150px*var(--avatar-position-width));justify-self:var(--avatar-position-alignment)}._3rXmBWRJREVVaF_z2zkgJp{height:auto;width:100%;-ms-flex-item-align:end;align-self:flex-end}.XI9fYJ1uvJoTy0Aq0S9LE{width:100%;height:100%;position:absolute;top:0;left:0}.G-Xm8rxA8XuTfXF3bPlcA{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:18px;display:inline-block;margin-top:8px;color:var(--newRedditTheme-metaText)}._1KPfdJXffAMwJPUJ6ybNBb{color:var(--newCommunityTheme-linkText)}
._292iotee39Lmt0MkQZ2hPV{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:21px;word-break:break-word;overflow:auto;padding-bottom:1px;margin-bottom:-1px;color:var(--newCommunityTheme-bodyText)}a:visited ._292iotee39Lmt0MkQZ2hPV{color:var(--postBodyLink-VisitedLinkColor)}.YCBAlwtFjC7cDSMdBeA2W{display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center}.gCpM4Pkvf_Xth42z4uIrQ{background:none;border:1px solid var(--newCommunityTheme-bodyText);color:var(--newCommunityTheme-bodyText);padding:10px 20px;text-transform:uppercase}._1GPL7pYOAn5YHfoARxZ8-F{--postBodyLink-VisitedLinkColor:var(--newCommunityTheme-bodyText)}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/CollectionCommentsPage~CommentsPage~CountryPage~FramedGild~GildModal~GovernanceReleaseNotesModal~Hap~cb450973.574222e94257c4de6a11_.css.map*/</style><style class="" data-href="chunkCSS/CollectionCommentsPage~CommentsPage~CountryPage~Frontpage~GovernanceReleaseNotesModal~ModListing~Mod~e3d63e32.74eb929a3827c754ba25_.css">._3h6zBMaGJuwN_qOmhUyv7E{padding:8px}
._23h0-EcaBUorIHC-JZyh6J{-ms-flex-align:center;align-items:center;box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;left:0;padding:8px 4px 8px 0;position:absolute;top:0}@media (max-width:639px){._23h0-EcaBUorIHC-JZyh6J{display:none}}
._2lHXa-mLMsRfm1Q5JxgU4r,.REwsaLIz5u3DhM7zbbzIU,.bE7JgM2ex7W3aF3zci5bm,.FeLWdhOO-cVXowAo3Rndk,._3Qkp11fjcAw9I9wtLo8frE{background-color:var(--newCommunityTheme-postTransparent20);color:var(--newCommunityTheme-actionIcon);position:relative;border:thin solid transparent}._2lHXa-mLMsRfm1Q5JxgU4r:hover,.REwsaLIz5u3DhM7zbbzIU:hover,.bE7JgM2ex7W3aF3zci5bm:hover,.FeLWdhOO-cVXowAo3Rndk:hover,._3Qkp11fjcAw9I9wtLo8frE:hover{border:thin solid var(--newCommunityTheme-postIcon);z-index:1}._2yN8L-c8UBoKxHn0-vg_dS,.bE7JgM2ex7W3aF3zci5bm{border:thin solid var(--newCommunityTheme-postLine);margin-bottom:-1px;position:relative;z-index:0}._2zRMh6o0BucltCL6o64pa4{position:relative;color:var(--newCommunityTheme-actionIcon)}._1Accc3h2AW0sB8E4CcEz2n._1LmKpEAguLZV4jQMgQSFVL:focus,.bE7JgM2ex7W3aF3zci5bm._1LmKpEAguLZV4jQMgQSFVL:focus,.FeLWdhOO-cVXowAo3Rndk._1LmKpEAguLZV4jQMgQSFVL:focus{border:1px solid var(--newCommunityTheme-postIcon);box-shadow:0 0 1px var(--newCommunityTheme-postIcon);z-index:2}._3joKifdh6j3tG_vsgFS85R{-webkit-backface-visibility:hidden;backface-visibility:hidden;transform:translateZ(0)}.bE7JgM2ex7W3aF3zci5bm{overflow:hidden;position:relative}@media (min-width:640px){.bE7JgM2ex7W3aF3zci5bm{padding-left:40px}}.FeLWdhOO-cVXowAo3Rndk{overflow:hidden}._2lHXa-mLMsRfm1Q5JxgU4r,._3Qkp11fjcAw9I9wtLo8frE{--post-line-color:var(--newCommunityTheme-postLine);--post-icon-color:var(--newCommunityTheme-postIcon);border:1px solid var(--post-line-color);margin-bottom:10px;overflow:hidden}._2lHXa-mLMsRfm1Q5JxgU4r:hover,._3Qkp11fjcAw9I9wtLo8frE:hover{border:1px solid var(--post-icon-color)}._2lHXa-mLMsRfm1Q5JxgU4r._1nQXomgzQ2rnBsRU2iZ00l,._3Qkp11fjcAw9I9wtLo8frE._1nQXomgzQ2rnBsRU2iZ00l{--post-line-color:var(--newRedditTheme-postLine);--post-icon-color:var(--newRedditTheme-postIcon)}._1qftyZQ2bhqP62lbPjoGAh{--post-icon-color:var(--newCommunityTheme-postIcon)}._1qftyZQ2bhqP62lbPjoGAh._1LmKpEAguLZV4jQMgQSFVL:focus{border:1px solid var(--post-icon-color);box-shadow:0 0 0 1px var(--post-icon-color);transition:box-shadow 0s}._1qftyZQ2bhqP62lbPjoGAh._1nQXomgzQ2rnBsRU2iZ00l{--post-icon-color:var(--newRedditTheme-postIcon)}._3Qkp11fjcAw9I9wtLo8frE{transition:color .5s,fill .5s,box-shadow .5s}._2RFRmGwuh0BemW7iUA3-VB{text-overflow:ellipsis;overflow:hidden;white-space:nowrap}
._3cwq18vPueuAxRSrd1foNB{display:none;margin-left:8px}@media (min-width:320px){._3cwq18vPueuAxRSrd1foNB{display:-ms-flexbox;display:flex;-ms-flex:0 0 96px;flex:0 0 96px;height:72px}}@media (min-width:375px){._3cwq18vPueuAxRSrd1foNB{display:-ms-flexbox;display:flex;-ms-flex:0 0 96px;flex:0 0 96px;height:72px}}@media (min-width:414px){._3cwq18vPueuAxRSrd1foNB{display:-ms-flexbox;display:flex;-ms-flex:0 0 96px;flex:0 0 96px;height:72px}}@media (min-width:436px){._3cwq18vPueuAxRSrd1foNB{display:-ms-flexbox;display:flex;-ms-flex:0 0 96px;flex:0 0 96px;height:72px}}._1jxw1P65tWXN5u8kVHlX-n{margin:8px 0}._2KR7fLQx_7rIv8QaoeXKZw,._1jxw1P65tWXN5u8kVHlX-n{display:-ms-flexbox;display:flex}._2KR7fLQx_7rIv8QaoeXKZw{-ms-flex-direction:column;flex-direction:column;-ms-flex-pack:justify;justify-content:space-between;margin-left:8px}._6w7aNMh3t6UMe07Q6oWFE{border-radius:4px;height:16px;margin:1.5px 0;width:16px}._1Xs9oeessHWcuF0VTVxRnl{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;fill:inherit;-ms-flex-direction:column;flex-direction:column;text-align:center}._2XOZ5bYpLdswvBAYUNa-ly{border-radius:4px;-ms-flex:1;flex:1;height:100%;width:100%;border-radius:2px;position:relative}.n3AVRrP7HOfc0gAtGFpfv{height:20px;width:328px}._1BoNlCqTsaeLXkuZbADxyl{height:10px;margin-top:8px;width:88px}._1IgQuZI8L6A0NcShWmf08y{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;margin:auto 8px 0 0}._2AMaFX8Gwojg29X4_nOnaL{height:12px;width:16px}.oljBm1Q059l3l84VHO9VM{border-right:1px solid var(--newCommunityTheme-line);height:16px;margin:0 8px;vertical-align:middle}._2xeK0Acj_38O5kqiHgp7VC{height:12px;width:110px}._3WphuhFsMSKk2tQyD3fZeI{height:12px;margin-left:8px;width:20px}
._3RRgbzXvoZ4MUYm45lAqp7{border-radius:4px;height:16px;margin:0 14px 0 4px;width:16px}._2rSb53hAOWG9j6R_ToxoSJ{fill:inherit;-ms-flex-direction:column;flex-direction:column;-ms-flex-align:center;align-items:center}._2rSb53hAOWG9j6R_ToxoSJ,._2wuOxz4--LcoxCYSrpCBlx{display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row}._2wuOxz4--LcoxCYSrpCBlx{-ms-flex-align:start;align-items:flex-start;padding:3px 8px 3px 4px}._3CIl2qTD30RwYsMAGO2Y2S{margin:4px 4px 4px 14px}._2UCpUVZ4aSncQhvkrQW_0i{border-radius:100%;height:16px;width:16px}._2IJnSguizdehDk_JnTKrdK{margin:2px 12px 0 4px}._1OQE_XsSHzM7AtjVQahjoI{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex:1 1 100%;flex:1 1 100%;min-height:24px;overflow:hidden}._28eZmJsl2bogBZ2KPmeoFO{width:160px}._24dJJDh8muEbehYysONmV1,._28eZmJsl2bogBZ2KPmeoFO{height:12px;margin-top:2px}._24dJJDh8muEbehYysONmV1{margin-left:8px;width:256px}._2-iJVRFJK-xC7a7xgBF-T5{width:52px}._2-iJVRFJK-xC7a7xgBF-T5,._1IFRAIwzfwChKq85FhLG69{height:12px;margin-left:8px}._1IFRAIwzfwChKq85FhLG69{width:20px}._3HxvQvODjYEHa-X5AuQinY{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;margin-left:auto;min-height:24px}
._1yYeg-XN7v7i06TrK8Lh13{margin:8px 0 0 40px}._3Qm3gV6v4Y9YWuQgCqMvJr{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;fill:inherit;-ms-flex-direction:column;flex-direction:column}.y9vamInQ4LrXndusvhkBl{height:16px;margin:1.5px 0 1.5px -8px;width:16px;border-radius:4px}._3QuUl4wSXyqVEAkIgGaLXl{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-flow:row nowrap;flex-flow:row nowrap;margin:0 8px 8px 0}.CgxUJgu3x2x0HIb96uJcV{border-radius:100px;height:20px;width:20px}._3vDeGQp8VifbnDC95HagCL{height:12px;margin-right:8px}.Nci_4K-inwrSvpM-HSgWy{height:12px;width:232px}._1QxTngAAL4xURgv5RVNOq1{height:20px;margin-top:16px;width:328px}._2cFr_UVzM0pQGvZVL2Pmx5{height:343px;margin:8px 0 0 40px;width:100%}._33_7mRxP4egdr8CL9OMSdb{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;margin:8px 8px 8px 0}._EVV9UvUf3cYf-HtTUL33{height:16px;width:110px}._2Ovk4TwuzZDamFhAj_X5Nl{height:16px;margin-left:8px;width:20px}._3Yno3UEEUpbfXOklgaEf27{height:20px;width:120px}._3-iHWkhaRqC0JmCwckFVg1{height:36px;display:-ms-flexbox;display:flex;margin-bottom:12px}._314KvlynGyTcpUjSXckrbY{height:36px;width:36px;border-radius:1000px;margin-right:12px}._314KvlynGyTcpUjSXckrbY._3EpUFkJ6GGzK-aVzndYmTT{width:100px}
._2486DvSWPD-F9xM1LaS9AZ{background-color:var(--newRedditTheme-postTransparent20);max-width:100%}._2486DvSWPD-F9xM1LaS9AZ,.-epve_JNERIUWcWNKZJF6{display:-ms-flexbox;display:flex}.-epve_JNERIUWcWNKZJF6{-ms-flex-direction:column;flex-direction:column;width:100%}._2dzkHWoQ7wLdDsEAwyw1NL{display:-ms-flexbox;display:flex;padding:16px}._1cE9WBao1CSNnKKQd97erN{height:20px;width:80px}.dXH0UqIq_Mtkd24573Rs5{height:20px;margin-left:10px;width:200px}._1NHO6pCrlHfrC6Q-_d-3kZ{display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;padding:0 16px}.aHlABuIzfJ3NbabTwjGN8{width:100%}._1wEL9K8jt2pgaYL1hhQt_P{border-radius:4px;-ms-flex:1;flex:1;height:100%;width:100%;border-radius:2px}._22TlQsT52A1DMzjuJNEb7b{display:none;margin-left:8px}@media (min-width:320px){._22TlQsT52A1DMzjuJNEb7b{display:-ms-flexbox;display:flex;-ms-flex:0 0 138px;flex:0 0 138px;height:98px}}@media (min-width:375px){._22TlQsT52A1DMzjuJNEb7b{display:-ms-flexbox;display:flex;-ms-flex:0 0 138px;flex:0 0 138px;height:98px}}@media (min-width:414px){._22TlQsT52A1DMzjuJNEb7b{display:-ms-flexbox;display:flex;-ms-flex:0 0 138px;flex:0 0 138px;height:98px}}@media (min-width:478px){._22TlQsT52A1DMzjuJNEb7b{display:-ms-flexbox;display:flex;-ms-flex:0 0 138px;flex:0 0 138px;height:98px}}._2ztqeqAwKeO-Fwjjpm3ou2{display:-ms-flexbox;display:flex;padding:8px 16px}.hKjLaaNx-nWjCGihE3wwZ{height:16px;width:70px}
._3AaWcDg070_adHsR2kuysq{border:1px solid var(--newCommunityTheme-postLine);border-radius:4px;margin:5px 0;overflow:hidden}._3AaWcDg070_adHsR2kuysq._2haLgsTDyDtdH_2cecOvLP{margin:6px 0 5px}._3AaWcDg070_adHsR2kuysq._1nHCEySWEWsOIjYYvrF3Ay{margin:-5px 0 10px}._3EYDFTyujo6kmshltlBq10{font-size:14px;font-weight:500;line-height:18px;background-color:var(--newCommunityTheme-body);padding:10px 20px 13px;text-align:center}._3EYDFTyujo6kmshltlBq10 ._21u1WVXVWqUtM7v_Y0c9_0{line-height:18px;padding:0 0 15px;color:var(--newCommunityTheme-bodyText)}._3EYDFTyujo6kmshltlBq10 ._3FNnHKnM8zvRUpKS2hqoVu{color:var(--newCommunityTheme-active);line-height:18px;padding:3px 0}._3EYDFTyujo6kmshltlBq10 ._5XRkOTBpwyH-aTpv3Uj2{border:0;border-top:1px solid var(--newCommunityTheme-line);width:100%}._15k2ydh8mxGtI2wxNW_lBA,._3jke_Z4bAXFPXe4m2Z_ocv{-ms-flex-align:center;align-items:center;background-color:var(--newCommunityTheme-body);display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-pack:center;justify-content:center;min-height:80px;padding:10px 20px;text-align:center}._15k2ydh8mxGtI2wxNW_lBA ._3Qyit4QoTHIo9Mp3ed0NZg,._3jke_Z4bAXFPXe4m2Z_ocv ._3Qyit4QoTHIo9Mp3ed0NZg{color:var(--newCommunityTheme-active);font-weight:600;left:-30px;position:absolute}._15k2ydh8mxGtI2wxNW_lBA ._21u1WVXVWqUtM7v_Y0c9_0,._3jke_Z4bAXFPXe4m2Z_ocv ._21u1WVXVWqUtM7v_Y0c9_0{font-size:14px;font-weight:500;line-height:18px;padding:0 0 15px;position:relative}._15k2ydh8mxGtI2wxNW_lBA .HHkkaXqGVK3_gJrR3VcQS,._3jke_Z4bAXFPXe4m2Z_ocv .HHkkaXqGVK3_gJrR3VcQS{font-size:14px;font-weight:500;line-height:18px;color:var(--newCommunityTheme-active);padding:0 0 15px}._15k2ydh8mxGtI2wxNW_lBA ._2f9EhN-2fH0l-KxOeQ_wj8,._3jke_Z4bAXFPXe4m2Z_ocv ._2f9EhN-2fH0l-KxOeQ_wj8{font-size:12px;font-weight:400;line-height:16px}._15k2ydh8mxGtI2wxNW_lBA{padding:0 20px}
._3tBFh6Ty3gSaxW4gcm6hZ_{height:156px;margin-bottom:-20px;overflow:hidden}
.FohHGMokxXLkon1aacMoi{position:relative}._1Uj2L1UhJuirkaXINcf9S8{margin-bottom:10px;padding:16px 0 16px 12px}._2DB_2VI3a-y6nk57R2aWVo{font-size:16px;font-weight:500;line-height:20px}.zfoxmi0VvZvMZu1rHVbMX{top:0;left:0;right:0;bottom:0;max-height:300px;position:absolute;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;z-index:10}.Ii7DEkcMDxQHElTHeeaci{margin:0 50px 10px;text-align:center}.rpBJOHq2PR60pnwJlUyP0{min-height:1000px;width:100%}.QBfRw7Rj8UkxybFpX-USO{height:auto;width:100%}._1yJOfuD_qgqaaG8ZIFbQVc{background-color:var(--newCommunityTheme-body);color:var(--newCommunityTheme-linkText)}.wakXAw7uCIqmSRV84RKMW{fill:var(--newCommunityTheme-linkText);padding-left:12px;vertical-align:middle;width:16px}
.wwHbgRV0ZXGp5CHHlpo5u{display:none}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/CollectionCommentsPage~CommentsPage~CountryPage~Frontpage~GovernanceReleaseNotesModal~ModListing~Mod~e3d63e32.74eb929a3827c754ba25_.css.map*/</style><style class="" data-href="chunkCSS/CollectionCommentsPage~CommentsPage~EconTopAwardersModal~ModQueuePages~ModerationPages~PostCreation~~bca2b657.04ea9543b9fabdb4bfe4_.css">._3Wf5TsmUR8Qf8nr0fDHjur{width:28px;display:-ms-inline-flexbox;display:inline-flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;color:var(--newCommunityTheme-actionIcon);position:relative}.eQZZIJf9NTq5MBV2285S2{vertical-align:top}
@keyframes _1nKXGUCyFMbujKJCUr7v1F{0%{transform:scale(1)}50%{transform:scale(.125)}83%{transform:scale(.172)}to{transform:scale(.156);display:none}}@keyframes _3Unh28GaDqT2GLqHAD02_S{0%{opacity:0}to{opacity:1}}.yW-ely1Ik8KTYTO9TSOSa{display:inline-block;vertical-align:top}.q2KM5tcmhqOBd4ElRihZQ{display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;-ms-flex-align:center;align-items:center;min-width:40px;padding:4px;color:var(--newCommunityTheme-titleText);font-size:12px;font-weight:400;line-height:16px}.q2KM5tcmhqOBd4ElRihZQ._1HqRbG571qt3Nk2zj_W3TS{background-color:var(--newCommunityTheme-active)}.q2KM5tcmhqOBd4ElRihZQ._1HqRbG571qt3Nk2zj_W3TS:focus,.q2KM5tcmhqOBd4ElRihZQ._1HqRbG571qt3Nk2zj_W3TS:hover{background-color:var(--newCommunityTheme-activeShaded90)}.q2KM5tcmhqOBd4ElRihZQ._1HqRbG571qt3Nk2zj_W3TS:active{background-color:var(--newCommunityTheme-activeShaded80)}._1rwi4ljDNaPtYUiOiXomov{height:20px;width:20px;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;-ms-flex-align:center;align-items:center}._1YpK2GgjHXEnSEetPdXV17{margin-left:4px}._2lnLb-ItT6LeziBNeQZx8I{height:20px;width:20px}._2lnLb-ItT6LeziBNeQZx8I._3JxvBqAeBggcg7vHXhdVlS{visibility:hidden}._2qKgWPWPiz4EnwPhDH9jaU{opacity:0;position:absolute;height:128px;width:128px;animation:_1nKXGUCyFMbujKJCUr7v1F .6s ease-in-out 1.7s,_3Unh28GaDqT2GLqHAD02_S .1s ease-in-out 1.7s;animation-fill-mode:forwards}@media (prefers-reduced-motion:reduce){._2lnLb-ItT6LeziBNeQZx8I._3JxvBqAeBggcg7vHXhdVlS{visibility:visible}._2qKgWPWPiz4EnwPhDH9jaU{display:none;animation:none}}
._1c_YBKkiW4FhhLJPkq9c1v{fill:var(--newCommunityTheme-actionIcon)}
.DInSK-8C_3_wtp8rkyyk_{position:-webkit-sticky;position:sticky;left:-1px;bottom:0;height:100%;width:52px;min-width:52px;background:linear-gradient(90deg,var(--newCommunityTheme-post),var(--newCommunityTheme-post) 50%,hsla(0,0%,100%,0));display:-ms-inline-flexbox;display:inline-flex;-ms-flex-align:center;align-items:center;z-index:1}.DInSK-8C_3_wtp8rkyyk_._3h4h05agLr2A_NU_Rf3yCn{left:unset;right:-1px;transform:rotate(180deg)}._2MU8EpOTDEghV1ecmq37UZ{color:var(--newCommunityTheme-actionIcon);padding:4px 4px 4px 3px;margin-left:8px;border-radius:4px}._2MU8EpOTDEghV1ecmq37UZ:focus,._2MU8EpOTDEghV1ecmq37UZ:hover{background-color:var(--newCommunityTheme-navIconFaded10)}._2MU8EpOTDEghV1ecmq37UZ:active{background-color:var(--newCommunityTheme-postLine)}._2MU8EpOTDEghV1ecmq37UZ:focus:not(._38NFrOkGDKwQs4baFR_XWF){outline:none}.uPrjAc1vFe8cn_-JitBDg{height:14px;transform:rotate(180deg)}
.AavtiP0APDAhqwl7opcvC{display:-ms-inline-flexbox;display:inline-flex;-ms-flex-pack:center;justify-content:center;-ms-flex-align:center;align-items:center;white-space:nowrap;color:var(--newCommunityTheme-metaText);cursor:pointer;margin-left:2px;margin-right:4px;font-size:12px;font-weight:400;line-height:16px}._2NhWk2-d-tn8oC0A-k_Ss-{margin-left:4px;margin-right:2px;height:16px}._20LMDg4_PtezakicbNPSfn{height:16px;width:16px}.qntP0rU06Z8LVP6TKmQHQ.AavtiP0APDAhqwl7opcvC{height:28px;padding:4px 8px;margin:8px 0 0 8px;box-sizing:border-box;border-radius:999px;background-color:var(--newCommunityTheme-line);color:var(--newCommunityTheme-titleText)}.qntP0rU06Z8LVP6TKmQHQ.AavtiP0APDAhqwl7opcvC:focus,.qntP0rU06Z8LVP6TKmQHQ.AavtiP0APDAhqwl7opcvC:hover{background-color:var(--newCommunityTheme-lineShaded90)}.qntP0rU06Z8LVP6TKmQHQ.AavtiP0APDAhqwl7opcvC:active{background-color:var(--newCommunityTheme-lineShaded80)}.qntP0rU06Z8LVP6TKmQHQ.AavtiP0APDAhqwl7opcvC:focus:not(.qbP9Qnm2Qru28YDgfefpw){outline:none}.qntP0rU06Z8LVP6TKmQHQ ._2NhWk2-d-tn8oC0A-k_Ss-{height:20px;width:20px;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;-ms-flex-align:center;align-items:center;margin-right:4px}.qntP0rU06Z8LVP6TKmQHQ ._20LMDg4_PtezakicbNPSfn{height:20px;width:20px}
._1wgnb6w6OJogtEV2N4B3lD{display:block;white-space:nowrap;height:40px;transition:height .3s ease-in-out;overflow:hidden;position:relative}._1wgnb6w6OJogtEV2N4B3lD:not(._1pZRAWakamwUD9Urx217oC){padding:100px 0;margin:-100px 0;pointer-events:none}._1wgnb6w6OJogtEV2N4B3lD:not(._1pZRAWakamwUD9Urx217oC)>*{pointer-events:all}._1wgnb6w6OJogtEV2N4B3lD._3c1kr0TjcknQSAP9naDKGv{white-space:normal;height:auto;padding-right:8px}._1wgnb6w6OJogtEV2N4B3lD._1pZRAWakamwUD9Urx217oC{height:0}._1FZ8jCjLuxoHLtbgJDekEU{min-width:12px;display:inline-block}@media (prefers-reduced-motion:reduce){._1wgnb6w6OJogtEV2N4B3lD{transition:none}}._2PVXBodfFt50jjk5ydPpWY{height:28px;margin:8px 0 0 8px;border-radius:999px;background-color:var(--newCommunityTheme-line)}._2PVXBodfFt50jjk5ydPpWY:focus,._2PVXBodfFt50jjk5ydPpWY:hover{background-color:var(--newCommunityTheme-lineShaded90)}._2PVXBodfFt50jjk5ydPpWY:active{background-color:var(--newCommunityTheme-lineShaded80)}._2PVXBodfFt50jjk5ydPpWY:focus:not(._3JCIceLNhOdJUR_ABw_M2V){outline:none}._1wgnb6w6OJogtEV2N4B3lD._3c1kr0TjcknQSAP9naDKGv ._2PVXBodfFt50jjk5ydPpWY{margin-top:8px}
@keyframes _3bDgD_5hXKabLRqOe9sXRi{0%{transform:scale(0)}33%{transform:scale(1.3)}67%{transform:scale(.8)}to{transform:scale(1)}}._2OYwDdghtXEuTF67C95YLY{display:inline-block;white-space:nowrap;color:var(--newCommunityTheme-metaText);cursor:pointer;font-size:12px;font-weight:400;line-height:16px}._2OYwDdghtXEuTF67C95YLY .n08B7PrU01wzgZYIh-s7N{cursor:inherit}._2OYwDdghtXEuTF67C95YLY .n08B7PrU01wzgZYIh-s7N.f18KwJcHh9SCfKw_W3Dm2{animation-name:_3bDgD_5hXKabLRqOe9sXRi;animation-duration:1s;animation-iteration-count:1}.n08B7PrU01wzgZYIh-s7N{margin-left:4px;margin-right:2px;cursor:default;vertical-align:middle;max-height:16px;max-width:16px}
.icon{font-size:20px;font-weight:400;height:20px;line-height:20px;vertical-align:middle;width:20px}
._3XoW0oYd5806XiOr24gGdb{display:-ms-inline-flexbox;display:inline-flex;-ms-flex-align:center;align-items:center;position:relative;-ms-flex-wrap:wrap;flex-wrap:wrap;overflow:hidden;z-index:5}._1vpnHb2bSTD6BcgVKisnPT{font-size:16px;padding:2px;border-radius:4px;margin-left:4px;outline:none;color:var(--newCommunityTheme-actionIcon)}._1vpnHb2bSTD6BcgVKisnPT._3vGYJIJIswDD8YOAMWGC4N{visibility:hidden;opacity:0;transition:visibility 0s linear .1s,opacity .1s linear}._1vpnHb2bSTD6BcgVKisnPT:focus,._1vpnHb2bSTD6BcgVKisnPT:hover{outline:none;background-color:rgba(26,26,27,.1)}._1vpnHb2bSTD6BcgVKisnPT ._3zozqOs5cvNd2uvuIiu2_L{display:block;height:16px;line-height:16px;width:16px;font-size:16px}._1vpnHb2bSTD6BcgVKisnPT ._3zozqOs5cvNd2uvuIiu2_L:hover{color:var(--newCommunityTheme-actionIconTinted80)}._3XoW0oYd5806XiOr24gGdb:hover ._1vpnHb2bSTD6BcgVKisnPT._3vGYJIJIswDD8YOAMWGC4N{visibility:visible;opacity:1;transition-delay:0s}._1tAFPduILh7Zse0gkxT4vj{margin-left:4px;color:var(--newCommunityTheme-metaText);font-size:12px;font-weight:400;line-height:16px}._1tAFPduILh7Zse0gkxT4vj:hover{text-decoration:underline}
._3LS4zudUBagjFS7HjWJYxo{margin:0 4px}._37gsGHa8DMRAxBmQS-Ppg8{color:var(--newCommunityTheme-metaText);font-size:6px;line-height:20px}
._23wugcdiaj44hdfugIAlnX{font-size:12px;font-weight:400;line-height:16px;color:var(--newCommunityTheme-linkText)}._23wugcdiaj44hdfugIAlnX:not(.oQctV4n0yUb0uiHDdGnmE)._2YPMtQeUrWhVZuFXPpgmXz{font-size:14px;font-weight:700;line-height:18px}._23wugcdiaj44hdfugIAlnX.oQctV4n0yUb0uiHDdGnmE{color:inherit}._23wugcdiaj44hdfugIAlnX._2YPMtQeUrWhVZuFXPpgmXz{color:var(--newCommunityTheme-titleText);font-size:14px;font-weight:700;line-height:18px}._23wugcdiaj44hdfugIAlnX:hover{text-decoration:underline}.lizQBHVukyun2S2babj-l{font-size:12px;font-weight:400;line-height:16px;color:inherit}
.LalRrQILNjt65y-p-QlWH{fill:var(--newRedditTheme-actionIcon);height:18px;width:18px}.LalRrQILNjt65y-p-QlWH rect{stroke:var(--newRedditTheme-metaText)}._3J2-xIxxxP9ISzeLWCOUVc{height:18px}.FyLpt0kIWG1bTDWZ8HIL1{margin-top:4px}._2ntJEAiwKXBGvxrJiqxx_2,._1SqBC7PQ5dMOdF0MhPIkA8{vertical-align:middle}._1SqBC7PQ5dMOdF0MhPIkA8{-ms-flex-align:center;align-items:center;display:-ms-inline-flexbox;display:inline-flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-pack:center;justify-content:center}
.ekl2maIRbrCrsYFt1OwaE{margin-right:4px}
._3HFQBVggvR9KDsFzm7jIdr{font-size:12px;font-weight:700;line-height:16px;cursor:pointer;color:var(--newCommunityTheme-actionIcon);fill:currentColor;padding:6px 12px}._3HFQBVggvR9KDsFzm7jIdr:hover{background-color:var(--newCommunityTheme-line);color:var(--newCommunityTheme-bodyText)}
._2mHuuvyV9doV3zwbZPtIPG{display:inline-block;-ms-flex:0 0 auto;flex:0 0 auto}
._2sD9TJ9u16l-c0te-dTdGd._2sD9TJ9u16l-c0te-dTdGd{color:var(--newRedditTheme-bodyText);font-size:14px;width:14px;height:14px;line-height:1;opacity:.3}
.Q0CnEiiTYWW90JwBPi-3X{-ms-flex-align:center;align-items:center;color:var(--newRedditTheme-metaText);display:-ms-flexbox;display:flex;-ms-flex-flow:wrap;flex-flow:wrap;white-space:nowrap;font-size:12px;font-weight:400;line-height:16px}.Q0CnEiiTYWW90JwBPi-3X:hover ._3xGgEou3qoyvyHtklgaVwR{display:block}._3mkZJiG1HSCl4dWJD3SJX7{-ms-flex:0 0;flex:0 0;margin-right:4px;-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex}._3mkZJiG1HSCl4dWJD3SJX7:hover{text-decoration:underline}._3DKC-l35UqIQdbPaQm6M_T{-ms-flex:1 1;flex:1 1;margin-right:4px;overflow:hidden;text-overflow:ellipsis}._1EQPlMscZuMqwdEddympoR{border:none;border-radius:50%;display:-ms-flexbox;display:flex;height:16px;margin-right:4px;width:16px}
._3hiYGoi3Vu4LyfvVOlMZcW{margin-bottom:8px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center}._2eTjg2aoICUGQm_8asj04C._2eTjg2aoICUGQm_8asj04C{display:block;width:15px;height:15px;margin-right:4px;font-size:15px;line-height:1}.E4q4Yx4JzJgDXXNirDocx{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;text-transform:none}.E4q4Yx4JzJgDXXNirDocx,._3ePON7WCMU0Fi11blkHDzm{color:var(--newRedditTheme-bodyText)}._3ePON7WCMU0Fi11blkHDzm{word-break:break-word;font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px}
.pGw5f7WKM2dO9R0Aotv_x{cursor:pointer;padding:8px 12px}.CYDdrcSbk6kboc66uF_7m{position:relative;margin-top:8px}.OtVR2-taBTlpgc-PYOW3y{color:var(--newRedditTheme-metaText);font-size:10px;line-height:16px}._2Dl07XZ7LNM7tsrbGG4Ym1{position:absolute;right:0;bottom:0}
.GPstmeFeO4czqJR2zs1mz{margin:0 2px 4px;max-height:190px;width:300px;pointer-events:none;cursor:pointer}._3r14JJj4Xkm_GnndoMhqik{background-color:var(--newRedditTheme-body);border-radius:8px;margin:0 2px 8px;pointer-events:all}.BQRl_o5B2PQPF96yT1qZc{border:1px solid rgba(0,0,0,.12156862745098039);border-radius:8px;box-shadow:0 2px 4px 0 var(--newRedditTheme-bodyTextAlpha20);cursor:pointer}.BQRl_o5B2PQPF96yT1qZc._2NlJQ9MQqeRtsH7eKMyZVd{border:1px solid hsla(0,0%,100%,.12156862745098039)}.sLQ_5L4_zMOcWEY-pLAkI{width:28px;height:16px;margin:0 auto;pointer-events:none}.sLQ_5L4_zMOcWEY-pLAkI,._2nXhIGpJFqVn_qWacMlFhL{background-color:transparent}._2nXhIGpJFqVn_qWacMlFhL{height:8px}
._282iT6zlGPTjxs4_wnUw_R{display:inline-block;margin-right:6px;padding:0 2px}._282iT6zlGPTjxs4_wnUw_R.RaBr7sOrqehAgubv6f1hE,._282iT6zlGPTjxs4_wnUw_R:hover{background-color:var(--newRedditTheme-actionIconAlpha20);border-radius:4px}._282iT6zlGPTjxs4_wnUw_R.RaBr7sOrqehAgubv6f1hE._1-EjTsf9H83ryPyVjAZp2A,._282iT6zlGPTjxs4_wnUw_R:hover._1-EjTsf9H83ryPyVjAZp2A{background-color:#2a2a2a}
._3fdQM74ud_8KssWgeznOrR{fill:#ffb000;height:12px;margin-right:4px;vertical-align:middle;width:12px}._3Ph6ensT9WFRjOg8dQQKJK{font-size:12px;font-weight:500;line-height:16px;border-radius:2px;border:1px solid #ffb000;display:inline-block;margin-left:4px;padding:2px 4px;text-transform:capitalize;color:var(--newCommunityTheme-bodyText)}
._2oEYZXchPfHwcf9mTMGMg8{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;color:var(--newCommunityTheme-linkText);-ms-flex:0 0 auto;flex:0 0 auto;letter-spacing:normal}._2oEYZXchPfHwcf9mTMGMg8._3NAtxpywJRrKZN5zIU9vwP,._2oEYZXchPfHwcf9mTMGMg8.V0WjfoF5BV7_qbExmbmeR{font-size:12px;font-weight:400;line-height:16px;padding-right:4px;text-transform:capitalize}
._2ke5Q4KsrJWi6sCDENRwI2{width:100%}._2ke5Q4KsrJWi6sCDENRwI2:first-of-type{margin-bottom:16px}
._2kj4VmBwjxriyYFAErhLcT{cursor:default;padding:0 4px;height:12px;width:12px;font-size:12px}.FCXb7huCxyBIXH7T23q_k{display:inline-block;height:12px;margin:0 4px -2px -18px;opacity:0;width:12px}._2v3rPYFjifVGM7CfOh1dOl{display:inline-block;margin-right:4px}._3AStxql1mQsrZuUIFP9xSg{font-size:12px;font-weight:400;line-height:16px;-ms-flex-align:center;align-items:center;color:inherit}.icon.s46mo3ittWDxpPuCSXJ_T,.icon.MMQAY3zdk1u4R9hIKTklf,.icon._6W0v52Yp6BzEfoWlrczS8{font-size:16px;line-height:16px;vertical-align:middle}._3hh-iGjzOv78L_7t_PUHev{display:inline-block;fill:var(--newCommunityTheme-button);height:10px;margin-left:2px;margin-right:2px;margin-bottom:-1px;vertical-align:baseline;width:10px}._1ra0Iw9wwPoS0QhWWssr-u._1ra0Iw9wwPoS0QhWWssr-u{display:inline;vertical-align:middle;height:20px;width:20px;border-radius:100%;margin-right:4px}.eQgJJIfdY4JNXam_N622j{margin-right:3px;text-decoration:none}.eQgJJIfdY4JNXam_N622j:hover:not._1pHpG_nGDGKayS5oFfQGDX{text-decoration:underline}.SxdIdV2SgMWcIFG6Qsk0Q{cursor:default;margin:-2px 0 0 4px;vertical-align:middle}._2tbHP6ZydRpjI44J3syuqC{margin-right:3px;text-decoration:none}._2tbHP6ZydRpjI44J3syuqC:hover:not._1pHpG_nGDGKayS5oFfQGDX{text-decoration:underline}._2tbHP6ZydRpjI44J3syuqC._1qzCGTSJOhg8noWqRayhmN{font-size:12px;font-weight:700;line-height:16px;color:var(--newCommunityTheme-bodyText);display:inline;line-height:20px;text-decoration:none;vertical-align:baseline}._2tbHP6ZydRpjI44J3syuqC._1qzCGTSJOhg8noWqRayhmN:hover{text-decoration:underline}._3V0C4FGg6153xIBQjwsycq{margin-right:3px;text-decoration:none}._3V0C4FGg6153xIBQjwsycq:hover:not._1pHpG_nGDGKayS5oFfQGDX{text-decoration:underline}.NAURX0ARMmhJ5eqxQrlQW{display:inline;vertical-align:text-top}._2VF2J19pUIMSLJFky-7PEI{display:inline-block;-ms-flex:0 0 auto;flex:0 0 auto}._1iAifs5p5MzPoJz5YrErUW{-ms-flex:1 1 auto;flex:1 1 auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}._2fCzxBE1dlMh4OFc7B3Dun{color:var(--newCommunityTheme-button);-ms-flex:0 0 auto;flex:0 0 auto;margin-right:3px}._3V4xlrklKBP2Hg51ejjjvz{vertical-align:middle}.s46mo3ittWDxpPuCSXJ_T{color:#ea0027}.MMQAY3zdk1u4R9hIKTklf{color:#24a0ed}._6W0v52Yp6BzEfoWlrczS8{padding:0 4px 0 2px;color:#ff4500}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/CollectionCommentsPage~CommentsPage~EconTopAwardersModal~ModQueuePages~ModerationPages~PostCreation~~bca2b657.04ea9543b9fabdb4bfe4_.css.map*/</style><style class="" data-href="chunkCSS/CollectionCommentsPage~CommentsPage~GovernanceReleaseNotesModal~ModerationPages~PostCreation~Profile~9a5d9fab.5280f54325366299a5fb_.css">._1Bdk-WLPvP2xHwSSQ3qsHq{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:21px;color:var(--newCommunityTheme-titleText);padding:16px 12px 10px}
.kcerW9lbT-se3SXd-wp2i{box-sizing:border-box;outline:none;width:100%}._38uXo2TofvhEuLKeH-rRcV{right:0}._32kofHIEwuARK_15MrzAuT{-ms-flex-align:center;align-items:center;background:#fff;border-radius:40px;box-shadow:0 4px 14px rgba(0,0,0,.1);display:-ms-flexbox;display:flex;height:44px;-ms-flex-pack:center;justify-content:center;top:calc(50% - 22px);width:44px}._32kofHIEwuARK_15MrzAuT,._3b8u2OJXaSDdBWoRB7zUoK{position:absolute}._3b8u2OJXaSDdBWoRB7zUoK{font-size:12px;font-weight:700;letter-spacing:.5px;line-height:24px;text-transform:uppercase;background-color:rgba(80,85,87,.8);border-radius:4px;bottom:16px;color:#fff;line-height:32px;text-align:center;text-decoration:none;width:320px;left:50%;transform:translate(-50%)}._3PkAZ5W4aDQ7cujQ426UiB{fill:var(--newCommunityTheme-actionIcon);height:24px;width:24px}.CxV9u12DiN4nfOLEzaWGg{transform:rotate(90deg)}.Qfn6RihWXp6riuP88alpI{transform:rotate(-90deg)}.iUP9nbvcaxfwKrQTgt0sw{display:-ms-flexbox;display:flex;height:100%;position:relative}._1ti9kvv_PMZEF2phzAjsGW{-ms-flex-align:start;align-items:flex-start}._3BxRNDoASi9FbGX01ewiLg{-ms-flex-align:center;align-items:center}._1fSFPkxZ9pToLETLQT2dmc{cursor:default;display:block;height:44px;padding:16px;position:absolute;top:calc(50% - 38px);width:44px}._1fSFPkxZ9pToLETLQT2dmc:hover ._32kofHIEwuARK_15MrzAuT{opacity:1}._3-JCOd-nY76g29C7ZVX_kl{cursor:pointer}.KVyBaj7FjzElWsqJDmw7v{height:100%;outline:none;overflow:hidden;position:relative;width:100%;margin:auto;max-height:100%;max-width:100%}._35oEP5zLnhKEbj5BlkTBUA{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;height:100%}._1dwExqTGJH2jnA-MYGkEL-{display:block;margin:0 auto;max-width:100%;position:relative}.KVyBaj7FjzElWsqJDmw7v ._28TEYBuEdOuE3kN6UyoKMa{display:-ms-flexbox;display:flex;position:absolute;transition:left .25s}._2Ev7WJU0f45KxlmClce9t8,.KVyBaj7FjzElWsqJDmw7v ._28TEYBuEdOuE3kN6UyoKMa,._1apobczT0TzIKMWpza0OhL{height:100%;margin:0;padding:0;width:100%}.KVyBaj7FjzElWsqJDmw7v ._3o5Vzct5tn9PE7e-emdDmf{height:100%;-ms-flex-pack:center;justify-content:center;margin:0}._26daP6nhhW7BT-CMzL0ijs,.KVyBaj7FjzElWsqJDmw7v ._3o5Vzct5tn9PE7e-emdDmf{display:-ms-flexbox;display:flex;width:100%}._26daP6nhhW7BT-CMzL0ijs{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:18px;-ms-flex-align:center;align-items:center;background-color:var(--newCommunityTheme-line);box-sizing:border-box;color:var(--newCommunityTheme-titleText);-ms-flex-flow:row wrap;flex-flow:row wrap;overflow:hidden}._1JvpVe-IA894KlEuAn5i9c{max-width:50%;padding-right:16px}._1JvpVe-IA894KlEuAn5i9c ._2ZUcZqGYDSM0BMbiracglV{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;color:#0079d3;font-weight:700}._1JvpVe-IA894KlEuAn5i9c ._2ZUcZqGYDSM0BMbiracglV ._2pA6COv2OLOcG3Ma_ZAzLs{fill:#0079d3;height:16px;width:16px}._1JvpVe-IA894KlEuAn5i9c ._2ZUcZqGYDSM0BMbiracglV .G960looU9eqiZ1POYed8r{overflow:hidden;text-align:right;text-overflow:ellipsis;white-space:nowrap}.cKdLDCF6ney9RBLRzJt8j{background-color:var(--newCommunityTheme-line)}._15nNdGlBIgryHV04IfAfpA{box-sizing:border-box;-ms-flex:1;flex:1;max-height:40px;overflow:hidden;padding:0 8px 0 16px;text-align:left;text-overflow:ellipsis;white-space:nowrap}._61i6grM3um1yuw4GrN97P{-ms-flex-align:center;align-items:center;-webkit-backdrop-filter:blur(40px);backdrop-filter:blur(40px);background:rgba(0,0,0,.5);border-radius:50px;color:#fff;font-size:12px;padding:4px 8px;position:absolute;right:16px;top:16px}._61i6grM3um1yuw4GrN97P,.bVildkms0x9XcY2qrG0Mr{display:-ms-flexbox;display:flex}.bVildkms0x9XcY2qrG0Mr{-ms-flex-flow:row wrap;flex-flow:row wrap;-ms-flex-pack:justify;justify-content:space-between}._1ynfiEQPXyJqwL8az8sG71{background-position:50% 50%;background-repeat:no-repeat;background-size:contain;height:143.5px;margin-bottom:8px;width:143.5px}.kYRcqD1CH-tXu0xGsAOLH{cursor:pointer;filter:blur(60px);height:100%;width:100%}.Qazqk11mIzZph1VMsNMtk{height:0;visibility:hidden;width:143.5px}._3VAoQueUjpnNBtHAZRjo_0{fill:#fff;width:18px}
.Chtkt3BCZQruf0LtmFg2c{-webkit-mask-image:linear-gradient(180deg,#000 60%,transparent);mask-image:linear-gradient(180deg,#000 60%,transparent);overflow:hidden;padding:5px 8px 10px}._2XNPI46MXRfDdsSoDqaksI{overflow:hidden;padding:0}._3xX726aBn29LDbsDtzr_6E{padding:5px 16px 5px 8px;max-width:800px}._1aLU7RPNLdvfcbaNdcN11x{margin:12px 0}._1aLU7RPNLdvfcbaNdcN11x .Owi9iYzjyVpDq_0YbCdJY:not(:first-child){margin-top:24px}._1aLU7RPNLdvfcbaNdcN11x .Owi9iYzjyVpDq_0YbCdJY>div{border-radius:4px;height:16px;margin:8px 0}._1aLU7RPNLdvfcbaNdcN11x .Owi9iYzjyVpDq_0YbCdJY>div:last-child{width:80%}
.q0jsD_ZcQRuuUQzXawr8J{border-radius:5px;border:1px solid var(--newRedditTheme-line);height:100%;width:100%;position:absolute;top:0;left:0}._2yB7G9L-6O_6Lp6D0n7EAl{position:relative;max-width:550px;margin:0 auto;padding-right:12px}._3pYTJO5FjsoQWRUsIFQASN{opacity:1;pointer-events:unset}._3pYTJO5FjsoQWRUsIFQASN._3xICr9rbunMOudN40P1GgI{opacity:0;pointer-events:none}.sIgL7k1Lz6YLL146KNk8k{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:21px;background:var(--newRedditTheme-body);border:1px solid var(--newRedditTheme-line);border-radius:5px;color:var(--newRedditTheme-actionIcon);margin:0 auto;padding:32px 0;text-align:center;width:300px}._2f5uYHvlfzs2DngQsiCdvB{font-size:12px;font-weight:700;letter-spacing:.5px;line-height:24px;text-transform:uppercase;background-color:rgba(80,85,87,.8);border-radius:4px;bottom:16px;color:#fff;left:50%;line-height:32px;position:absolute;text-align:center;text-decoration:none;transform:translate(-50%);width:320px}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/CollectionCommentsPage~CommentsPage~GovernanceReleaseNotesModal~ModerationPages~PostCreation~Profile~9a5d9fab.5280f54325366299a5fb_.css.map*/</style><style class="" data-href="chunkCSS/CollectionCommentsPage~ProfileComments~ProfileOverview~ProfilePrivate~SearchResults.f4720d86be16fa61e9aa_.css">.VHCAEHBEuD8bln8MDFl35{border-radius:4px;box-shadow:0 2px 4px 0 var(--newCommunityTheme-flair);cursor:pointer;line-height:0;overflow:hidden;width:100%}._3WbGqnEpw_ds1P508Qawma{height:12px;margin-top:-6px;padding-right:4px;vertical-align:middle;width:12px}.x_9o8pHUgKrlsT51QhLnG{font-size:14px;font-weight:500;line-height:18px;border-bottom:none;color:var(--newCommunityTheme-actionIcon);cursor:pointer;line-height:16px;padding:8px 16px 8px 8px;height:40px;text-transform:none}.x_9o8pHUgKrlsT51QhLnG:hover{background-color:var(--newRedditTheme-highlight);color:var(--newRedditTheme-bodyText);fill:var(--newRedditTheme-bodyText)}.x_9o8pHUgKrlsT51QhLnG ._1llB9GXV3OPp_55xrtgYNh{vertical-align:middle;text-transform:none}._2mkCGM7pDFARBtuKmKCBf0{width:20px;height:20px;margin-right:2px;vertical-align:middle}
._1PC9CIsUh5fq8cQdx3iMRr{margin-top:-4px}.BmpGQCO3oZBeUMzSaC5yX{height:16px;padding-right:4px;vertical-align:middle;width:16px}.BmpGQCO3oZBeUMzSaC5yX path{width:24px;fill:grey}
._3aVdI6Y8gye7mgZBvUx5X-{color:var(--newCommunityTheme-bodyText)}._2fiLaXOPdMYold0b-FKdVN{padding:8px}._1kl3eXeS_cuuM03T3_G8G1,._1EcSEYj-g98-QR-5idlQZr{height:12px;width:12px;margin-right:4px}._1EcSEYj-g98-QR-5idlQZr{fill:#0079d3}._1uVj4QJ6tIy-PC9lK3eOYO{font-size:14px;font-weight:500;line-height:18px;background-color:var(--newCommunityTheme-body);border:1px solid var(--newCommunityTheme-line);border-radius:4px;box-shadow:0 2px 4px 0 var(--newCommunityTheme-flair);cursor:pointer;position:absolute;width:189px;z-index:100}
.wM6scouPXXsFDSZmZPHRo{color:var(--newCommunityTheme-bodyText)}
._2ETuFsVzMBxiHia6HfJCTQ{font-size:12px;font-weight:400;line-height:16px;color:var(--newCommunityTheme-metaText)}
.sMaSljeAO1a-nAhrURxdj{margin-left:5px}.NL6v1uLnaxK0IHIJdUdel{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap}
._12wHSVQW6wUCbn56VnIfI-{width:16px;height:16px}
._3UBJEBi_CJ8y1i9Up_67Hb{-ms-flex:0 0 auto;flex:0 0 auto;margin-left:4px}
._18WUrfxbke5CjwIjhXu6C-{-ms-flex:0 0 auto;flex:0 0 auto;font-style:italic}
.icon._3Jlybj1GmQS_PfZVxE6yR1,.icon._2EBjdWEqs2dwPePq0_1vJn,.icon.YjyVr4SnBmO7WorLVMXq5,.icon._3M_jIwyB1POxBFR2jnGIp_,.icon._3hI84iVaolaHi85h6liPyp,.icon.MufLXlXcv1oes9OlakuXr{font-size:12px;height:12px;width:12px;line-height:12px;margin-left:4px}.icon._2EBjdWEqs2dwPePq0_1vJn{color:#46d160}.icon._2EBjdWEqs2dwPePq0_1vJn._2LQnjoTNHDUWKBOoq2gTlm{color:#ff585b}.icon._3Jlybj1GmQS_PfZVxE6yR1{color:#46d160}.icon.YjyVr4SnBmO7WorLVMXq5{color:#ffd635}.icon._3M_jIwyB1POxBFR2jnGIp_{color:#ff585b}.icon._3hI84iVaolaHi85h6liPyp{color:#ffb000}.icon.MufLXlXcv1oes9OlakuXr{color:#ff585b}.EM8fL_jC3oe9bruIOZt2U,._1KVzcRpEm0U5vCgrZbgiyN{font-size:12px;font-weight:400;line-height:16px;color:#ff585b;margin-left:4px}.EM8fL_jC3oe9bruIOZt2U{cursor:pointer}
.LWgI-A6rN9Wajn1VLxu2A{font-size:12px;font-weight:500;line-height:16px;cursor:default;font-weight:700;text-transform:uppercase;display:-ms-inline-flexbox;display:inline-flex}._2am63Mu1vtyM2MwmCJoxJp{margin-left:4px;width:16px;height:16px}
._2wd-K5Djdc9TGPRGDgmkpX{-ms-flex:0 0 auto;flex:0 0 auto;color:#75d377;white-space:nowrap}
.DjcdNGtVXPcxG0yiFXIoZ.DjcdNGtVXPcxG0yiFXIoZ{font-size:12px;font-weight:500;line-height:16px;color:var(--newRedditTheme-titleText)}._1a_HxF03jCyxnx706hQmJR,._2nobNdIwmDrXK7NZps5zUO{min-height:18px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-flow:row wrap;flex-flow:row wrap;-ms-flex-pack:start;justify-content:flex-start}.cFNx42ceihnMpvAsovOTi.cFNx42ceihnMpvAsovOTi{font-weight:400}._3QEK34iVL1BjyHAVleVVNQ{-ms-flex-item-align:baseline;align-self:baseline}.-Xcv3XBXmgiY2X5RqaPbO{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-align:start;align-items:flex-start;-ms-flex-pack:center;justify-content:center}._2bfuNFXt4pN8991xPpimzy{margin-left:8px}._3AgEmWP1qkCB8nds7LhzEB{-ms-flex-item-align:baseline;align-self:baseline;line-height:18px}._2a_XgY10KOzM0PRvywwDuY,.TNzy9Y4Ql8v80YssZ59GR,._3AgEmWP1qkCB8nds7LhzEB{margin-left:4px}._3yx4Dn0W3Yunucf5sVJeFU{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:18px;color:var(--newCommunityTheme-metaText)}._3yx4Dn0W3Yunucf5sVJeFU,._8b8fUdBRxCYj9MkNpFvvv{-ms-flex-item-align:baseline;align-self:baseline}._8b8fUdBRxCYj9MkNpFvvv{-ms-flex:0 0 auto;flex:0 0 auto;margin:0 4px}._3AXw8D3tzlqTRxjQdd5ve7{-ms-flex-item-align:end;align-self:flex-end;margin-right:4px}._3w527zTLhXkd08MyacMV9H{min-height:18px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-flow:row wrap;flex-flow:row wrap;-ms-flex-pack:start;justify-content:flex-start;width:100%;margin-top:2px}._3TVHJ99XXRlGtv0wqGCBFy{margin-left:2px}
.S8WH2aCfP030wVxp0iR_o,.icon.xIZgDbR-AMck1mC6sZI1m,.icon._2IdAWdzNdIq-LUdJv0lpD6,.icon._39FDxNax8J3IkHXRxQmeJE,.icon.rZkjnStRKzlmtr__ixhKy,.icon._3X_-kuWbD5_nVi9_eTAYVC{font-size:12px;height:12px;width:12px;line-height:12px;margin-left:4px}._zMIUk6t-WDI7fxfkvD02{margin-right:0;margin-left:4px}.yJGcpQjpmA13QcuUz2h0B{margin:0 3px}._2LXcsgibmlCEsBPk8MLy7e{margin-left:8px}.kDnKKJWz2PJGoalLInCW1{color:#2390d3}._1sA-1jNHouHDpgCp1fCQ_F{font-size:12px;font-weight:400;line-height:16px;color:var(--newCommunityTheme-metaText);-ms-flex:0 0 auto;flex:0 0 auto;padding-left:4px}._1sA-1jNHouHDpgCp1fCQ_F:hover{text-decoration:underline}._1sA-1jNHouHDpgCp1fCQ_F:last-child{padding-right:8px}._2Wu4MNMVl4bsJ9iVnQz0dF{color:var(--newCommunityTheme-metaText);margin-right:8px}._3ezOJqKdLbgkHsXcfvS5SA,._2Wu4MNMVl4bsJ9iVnQz0dF{font-size:12px;font-weight:400;line-height:16px}._3ezOJqKdLbgkHsXcfvS5SA{-ms-flex-align:center;align-items:center;color:var(--newCommunityTheme-bodyText);display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;line-height:20px;transition:opacity .2s}._3ezOJqKdLbgkHsXcfvS5SA._2k27lgIDltx9kOzVGXt48i{margin-left:5px;opacity:.5}._3ezOJqKdLbgkHsXcfvS5SA._2k27lgIDltx9kOzVGXt48i:hover{opacity:1}._3ezOJqKdLbgkHsXcfvS5SA._1KMFaeLEhRikeFEOlWE9Ti{margin-bottom:2px}._3uDFtRr_CTErFPJQBtzECl{margin-left:4px}._3_GZIIN1xcMEC5AVuv4kfa{padding-left:4px}._3_GZIIN1xcMEC5AVuv4kfa,._1PuBpmbH2FA5sozYR7EuCs{-ms-flex:0 0 auto;flex:0 0 auto}._1PuBpmbH2FA5sozYR7EuCs{margin:0 4px}._3Ofd-Ek86mwX500i92F84q{margin-right:4px}.UG2sa-VYMzrn7D1iNXtfR{margin-left:4px}.icon._2IdAWdzNdIq-LUdJv0lpD6{color:#ea0027}.icon.xIZgDbR-AMck1mC6sZI1m{color:#be1337}.icon.rZkjnStRKzlmtr__ixhKy{color:#75d377}.icon._39FDxNax8J3IkHXRxQmeJE,.icon._3X_-kuWbD5_nVi9_eTAYVC{color:#24a0ed}._3xk2cMvsSpPHBinHNwkDHi{color:var(--newCommunityTheme-metaText);text-decoration:underline;display:inline;visibility:hidden;margin-left:4px}.UnthreadedComment:hover ._3xk2cMvsSpPHBinHNwkDHi{visibility:visible}
._2vEf-C2keJaBMY9qk_BxVn{margin-top:16px;width:312px}
._3ms2Z8z8rPWLXaErcTJ9yH{font-size:14px;line-height:21px;--RawHTMLDisplay-tr-even:var(--newCommunityTheme-line);--RawHTMLDisplay-tr-odd:var(--newCommunityTheme-line);color:var(--newCommunityTheme-bodyText);word-break:break-word}._3ms2Z8z8rPWLXaErcTJ9yH,._3ms2Z8z8rPWLXaErcTJ9yH h1{font-family:Noto Sans,Arial,sans-serif;font-weight:400}._3ms2Z8z8rPWLXaErcTJ9yH h1{font-size:22px;line-height:26px}._3ms2Z8z8rPWLXaErcTJ9yH h2{font-size:20px;line-height:24px}._3ms2Z8z8rPWLXaErcTJ9yH h2,._3ms2Z8z8rPWLXaErcTJ9yH h3{font-family:Noto Sans,Arial,sans-serif;font-weight:400}._3ms2Z8z8rPWLXaErcTJ9yH h3{font-size:18px;line-height:22px}._3ms2Z8z8rPWLXaErcTJ9yH h4{font-size:16px;line-height:20px}._3ms2Z8z8rPWLXaErcTJ9yH h4,._3ms2Z8z8rPWLXaErcTJ9yH h5{font-family:Noto Sans,Arial,sans-serif;font-weight:400}._3ms2Z8z8rPWLXaErcTJ9yH h5{font-size:14px;line-height:18px}._3ms2Z8z8rPWLXaErcTJ9yH h6{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px}._3ms2Z8z8rPWLXaErcTJ9yH h1,._3ms2Z8z8rPWLXaErcTJ9yH h2,._3ms2Z8z8rPWLXaErcTJ9yH h3,._3ms2Z8z8rPWLXaErcTJ9yH h4,._3ms2Z8z8rPWLXaErcTJ9yH h5,._3ms2Z8z8rPWLXaErcTJ9yH h6{margin-top:1.4em;margin-bottom:8px}._3ms2Z8z8rPWLXaErcTJ9yH em{font-style:italic}._3ms2Z8z8rPWLXaErcTJ9yH strong{font-weight:700}._3ms2Z8z8rPWLXaErcTJ9yH sup{position:relative;top:-.4em;font-size:.7em;line-height:.7em}._3ms2Z8z8rPWLXaErcTJ9yH ol,._3ms2Z8z8rPWLXaErcTJ9yH ul{margin:4px 0 4px 8px}._3ms2Z8z8rPWLXaErcTJ9yH a,._3ms2Z8z8rPWLXaErcTJ9yH a:visited{color:var(--newCommunityTheme-linkText);text-decoration:underline}._3ms2Z8z8rPWLXaErcTJ9yH img{max-width:100%}._3ms2Z8z8rPWLXaErcTJ9yH ol li,._3ms2Z8z8rPWLXaErcTJ9yH ul li{margin:.4em 1em}._3ms2Z8z8rPWLXaErcTJ9yH ol li>p,._3ms2Z8z8rPWLXaErcTJ9yH ul li>p{margin-left:-.2em}._3ms2Z8z8rPWLXaErcTJ9yH ul li{list-style:disc outside}._3ms2Z8z8rPWLXaErcTJ9yH ol li{list-style:decimal outside}._3ms2Z8z8rPWLXaErcTJ9yH p{padding:.5em 0}._3ms2Z8z8rPWLXaErcTJ9yH p:first-child{padding-top:0}._3ms2Z8z8rPWLXaErcTJ9yH p:last-child{padding-bottom:0}._3ms2Z8z8rPWLXaErcTJ9yH blockquote{border-left:4px solid rgba(0,0,0,.2);margin:4px 0 4px 8px;padding-left:8px}._3ms2Z8z8rPWLXaErcTJ9yH pre{background:hsla(0,0%,93.3%,.8);display:-ms-grid;display:grid;line-height:1.4;margin:4px 0;max-width:100%;overflow:auto;padding:8px}._3ms2Z8z8rPWLXaErcTJ9yH pre code{background-color:transparent;color:#222;margin:0}._3ms2Z8z8rPWLXaErcTJ9yH code{font-family:Noto Mono,Menlo,Monaco,Consolas,monospace;font-size:13px;font-weight:400;line-height:20px;background:var(--newCommunityTheme-flair);color:var(--newCommunityTheme-postFlairText);margin:0 2px;max-width:100%;overflow:auto}._3ms2Z8z8rPWLXaErcTJ9yH table{border:2px solid var(--newCommunityTheme-line);border-collapse:collapse;display:inline-block;margin-bottom:4px;margin-top:4px;overflow-x:auto;word-break:normal;max-width:100%}._3ms2Z8z8rPWLXaErcTJ9yH tr{border:1px solid var(--newCommunityTheme-line)}._3ms2Z8z8rPWLXaErcTJ9yH tr:nth-child(2n){background-color:var(--RawHTMLDisplay-tr-even)}._3ms2Z8z8rPWLXaErcTJ9yH tr:nth-child(odd){background-color:var(--RawHTMLDisplay-tr-odd)}._3ms2Z8z8rPWLXaErcTJ9yH td,._3ms2Z8z8rPWLXaErcTJ9yH th{border:1px solid var(--newCommunityTheme-line);padding:4px 8px}._3ms2Z8z8rPWLXaErcTJ9yH th{text-align:center}._3ms2Z8z8rPWLXaErcTJ9yH hr{border:0;border-top:1px solid var(--newCommunityTheme-bodyTextAlpha20);height:1px;margin-bottom:8px;margin-top:8px}._3ms2Z8z8rPWLXaErcTJ9yH .md-spoiler-text:not([data-revealed]){border-radius:2px;background:var(--newCommunityTheme-metaText);cursor:pointer;color:transparent}._3ms2Z8z8rPWLXaErcTJ9yH .md-spoiler-text:not([data-revealed])>*{opacity:0}
._1poyrkZ7g36PawDueRza-J{background:#fff;position:relative}._1lLKAbRNH1mm32sVm7yCzQ{bottom:0;left:0;position:absolute;top:0;width:4px;z-index:1}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/CollectionCommentsPage~ProfileComments~ProfileOverview~ProfilePrivate~SearchResults.f4720d86be16fa61e9aa_.css.map*/</style><style class="" data-href="chunkCSS/CollectionCommentsPage~SearchResults.34071d8a7f9938b08a4f_.css">@keyframes vnt666wwqSK5qL63sBn9P{0%{background-position:0 0}to{background-position:-200% 0}}.fzTkuBRFT8iIn1XnJX_Yn{background:var(--newCommunityTheme-field);background-size:200%}.fzTkuBRFT8iIn1XnJX_Yn._34yMY7-6MNnz3utfjExvIq{animation:vnt666wwqSK5qL63sBn9P 1.5s ease infinite;background:linear-gradient(90deg,var(--newCommunityTheme-field),var(--newCommunityTheme-inactive),var(--newCommunityTheme-field));background-size:200%}._3giTODNeZ-Po90u8Ghs4aI{border-radius:4px}.VRC9QT7CgUxvhK0ceQSrn{background:var(--newCommunityTheme-post);border-radius:4px;box-shadow:0 2px 4px 0 rgba(0,0,0,.06)}
._3MknXZVbkWU8JL9XGlzASi{border:1px solid var(--newCommunityTheme-line);border-radius:4px;position:relative}._3MknXZVbkWU8JL9XGlzASi._3F2J0fSnCI3ZvF_tBSaV0s{border:1px solid var(--newCommunityTheme-navIcon)}._3MknXZVbkWU8JL9XGlzASi._1CpUVAt2tGEwaaBV3nZNJs{border:none}
._3Yo9aCwUoJBBuPKwf3r5cP{height:122px;padding:8px 16px}._3Yo9aCwUoJBBuPKwf3r5cP._225DoZxfrLcZu0fM8-Svk8{height:36px;box-sizing:border-box}._3CuuiBuYvA4VXTClabDCUK{height:21px;width:165px}._31gqZmjkDlF5-81EKQ7w_Y{background-color:var(--newCommunityTheme-bodyText);height:36px}._6rO7u4xvTeWjMNR68asbw{border-radius:4px 4px 0 0}._2Qh8N3s0Z7NWIPCVBDCcxH{border-radius:0 0 4px 4px}
._25blA2uobENRg70NGewwpP{margin:16px 0;position:relative}._25blA2uobENRg70NGewwpP._1chAIcRfDnelKBQkWMIXfl{margin:24px 40px}._25blA2uobENRg70NGewwpP._1chAIcRfDnelKBQkWMIXfl._2mGbbSC1nHodWNoj5NJEYY{margin-left:10px}._25blA2uobENRg70NGewwpP._2mGbbSC1nHodWNoj5NJEYY ._3NuRqPrgRBPdjWunXX3Q8E{margin-left:40px}._1KZHWcRRAqnSYcyX8FzWOK{height:19px;margin-bottom:4px;width:150px}._2gYdPXSssI0f1R9BPp9qsd{border-radius:50%;height:32px;overflow:hidden;position:absolute;top:2px;width:32px}
._2o0N1VHuLszWHqY5A8iayv{margin-top:20px}._2114DnVtHe_0MtbEW85tnL{display:-ms-flexbox;display:flex;margin:0 20px}._2114DnVtHe_0MtbEW85tnL>*{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column}._3ES-TCR45dPoj_NuOATuNi{border-radius:50%;-ms-flex:0 0 32px;flex:0 0 32px;height:32px;margin-left:-8px;width:32px}._3j7WNOCzFwCp1SXZGJP1-V{-ms-flex:0 0 auto;flex:0 0 auto;margin-left:-1px}._3tQxKBNuEJsKH_mPQEy34W{-ms-flex:1 1 auto;flex:1 1 auto;margin:5px 6px 0}.TbMmDiSaSaBQFF9F3FGe8{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-pack:center;justify-content:center;min-height:340px}._1-f8S_KoiOmIpA8kGxOgfh{fill:var(--newCommunityTheme-buttonAlpha40)}._1-f8S_KoiOmIpA8kGxOgfh,._1K0_Ej6gm6u-pTA1-FRY3S{height:28px;margin-bottom:20px;width:28px}._1K0_Ej6gm6u-pTA1-FRY3S{fill:var(--newCommunityTheme-metaText);stroke:var(--newCommunityTheme-body)}._2AxaYiv6EkZse5msRZqowQ{height:28px;margin-bottom:20px;width:28px}._39dVqXnozb8JxasPyFPu6C{margin-bottom:12px;text-transform:capitalize}._39dVqXnozb8JxasPyFPu6C,._2Nj40mHW74FkFefq6oqWkb{font-size:18px;font-weight:500;line-height:22px;color:var(--newCommunityTheme-metaText);opacity:.6}._2Nj40mHW74FkFefq6oqWkb{margin:0 50px 20px;text-align:center}._2x3Avx0lbWMcic-5bE_guO{font-size:14px;font-weight:500;line-height:18px;color:var(--newCommunityTheme-metaText);opacity:.6}._2ze7IsXK_2d3McYZHK6v_D,._3kZ_esGcijvfnM9KjA27vj{background-color:var(--newCommunityTheme-body);border-radius:4px;height:500px;margin:81px auto 60px;max-width:95%;position:relative;width:1200px}._32W1DnzyRkYXP82ZO96H0V,._1lwmFW6D9PmeT_QA-R5F_0{font-size:16px;color:var(--newCommunityTheme-actionIcon)}._32W1DnzyRkYXP82ZO96H0V{margin-top:-1px}._24vSs1yG3YhINbU6QRiFR9{height:16px;margin-bottom:8px;width:176px}._3S0qviXPTlIEUjYjSKT_Lb,._24vSs1yG3YhINbU6QRiFR9{background-color:var(--newCommunityTheme-placeholder)}._3S0qviXPTlIEUjYjSKT_Lb{height:124px;margin-bottom:12px;width:100%}
._15G4fCS1bzGgGK9kBOtN2t{position:absolute;z-index:3;overflow:hidden}._3rhkMikNPUTfnVDvk-6EFo{height:100%;max-height:75vh;top:0;bottom:0;left:0;right:0;pointer-events:none}._28x1bnTjOY6zWZfooCxkKQ{height:40px;top:0;right:0;width:200px;pointer-events:auto}
._2Gzh48SaLz7dQBCULfOC6V{background:none;border:none;color:var(--newCommunityTheme-linkText);cursor:pointer;height:12px;line-height:12px;outline:none;transform:rotate(180deg);width:12px}._2Gzh48SaLz7dQBCULfOC6V.hovered{color:var(--newCommunityTheme-line)}._2Gzh48SaLz7dQBCULfOC6V:hover{color:var(--newCommunityTheme-linkText)}._2Gzh48SaLz7dQBCULfOC6V ._1tnrhhM9S7dYjApTfvd14l{display:inline-block;width:12px;height:12px;font-size:12px;font-weight:400;line-height:12px}
@media (min-width:1206px){.SwOx7KbRrXYrqQCWMYPf0._2hXOR2fIcfnUg0p-Env7KQ ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1207px){.SwOx7KbRrXYrqQCWMYPf0._2hXOR2fIcfnUg0p-Env7KQ ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (min-width:1146px){.SwOx7KbRrXYrqQCWMYPf0._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1147px){.SwOx7KbRrXYrqQCWMYPf0._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (min-width:1269px){._2EcU45Nj3OvIEdu169RlLK._2hXOR2fIcfnUg0p-Env7KQ ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1270px){._2EcU45Nj3OvIEdu169RlLK._2hXOR2fIcfnUg0p-Env7KQ ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (min-width:1210px){._2EcU45Nj3OvIEdu169RlLK._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1211px){._2EcU45Nj3OvIEdu169RlLK._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}._2sxg06qfN6lCskrSU7pyoj ._2hr3tRWszeMRQ0u_Whs7t8,:not(:lang(en)) ._2t8wLytikHzPCUnvXdS_wu ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8,:not(:lang(en)) ._2Ik7QEXtA-lbZKj0ssL89G ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8,:not(:lang(en)) .SwOx7KbRrXYrqQCWMYPf0 ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8,:not(:lang(en)) ._2EcU45Nj3OvIEdu169RlLK ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}:not(:lang(en)) ._2t8wLytikHzPCUnvXdS_wu ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX,:not(:lang(en)) ._2Ik7QEXtA-lbZKj0ssL89G ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX,:not(:lang(en)) .SwOx7KbRrXYrqQCWMYPf0 ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX,:not(:lang(en)) ._2EcU45Nj3OvIEdu169RlLK ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}:not(:lang(en)) ._2t8wLytikHzPCUnvXdS_wu ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8,:not(:lang(en)) ._2Ik7QEXtA-lbZKj0ssL89G ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8,:not(:lang(en)) .SwOx7KbRrXYrqQCWMYPf0 ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8,:not(:lang(en)) ._2EcU45Nj3OvIEdu169RlLK ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}:not(:lang(en)) ._2t8wLytikHzPCUnvXdS_wu ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX,:not(:lang(en)) ._2Ik7QEXtA-lbZKj0ssL89G ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX,:not(:lang(en)) .SwOx7KbRrXYrqQCWMYPf0 ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX,:not(:lang(en)) ._2EcU45Nj3OvIEdu169RlLK ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}@media (max-width:540px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:541px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:99999999px),(min-width:960px) and (max-width:99999999px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000000px) and (max-width:960px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:99999999px),(min-width:960px) and (max-width:99999999px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000000px) and (max-width:960px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:99999999px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:100000000px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:700px),(min-width:960px) and (max-width:1030px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:701px) and (max-width:960px),(min-width:1031px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000159px),(min-width:960px) and (max-width:99999999px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000160px) and (max-width:960px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000159px),(min-width:960px) and (max-width:99999999px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000160px) and (max-width:960px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:100000159px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:100000160px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:603px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:604px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000062px),(min-width:960px) and (max-width:99999999px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000063px) and (max-width:960px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000062px),(min-width:960px) and (max-width:99999999px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000063px) and (max-width:960px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:100000062px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:100000063px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:763px),(min-width:960px) and (max-width:1093px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:764px) and (max-width:960px),(min-width:1094px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000222px),(min-width:960px) and (max-width:99999999px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000223px) and (max-width:960px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000222px),(min-width:960px) and (max-width:99999999px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000223px) and (max-width:960px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:100000222px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:100000223px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:666px),(min-width:960px) and (max-width:996px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:667px) and (max-width:960px),(min-width:997px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000125px),(min-width:960px) and (max-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000126px) and (max-width:960px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000125px),(min-width:960px) and (max-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000126px) and (max-width:960px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:100000125px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:100000126px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:826px),(min-width:960px) and (max-width:1156px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:827px) and (max-width:960px),(min-width:1157px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000285px),(min-width:960px) and (max-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000286px) and (max-width:960px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000285px),(min-width:960px) and (max-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000286px) and (max-width:960px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:100000285px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:100000286px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:729px),(min-width:960px) and (max-width:1059px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:730px) and (max-width:960px),(min-width:1060px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000188px),(min-width:960px) and (max-width:99999999px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000189px) and (max-width:960px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000188px),(min-width:960px) and (max-width:99999999px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000189px) and (max-width:960px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:100000188px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:100000189px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:889px),(min-width:960px) and (max-width:1219px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:890px) and (max-width:960px),(min-width:1220px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000348px),(min-width:960px) and (max-width:99999999px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000349px) and (max-width:960px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:100000348px),(min-width:960px) and (max-width:99999999px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:99999999px),(min-width:100000349px) and (max-width:960px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:100000348px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:100000349px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:800px),(min-width:960px) and (max-width:1050px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:801px) and (max-width:960px),(min-width:1051px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:935px),(min-width:960px) and (max-width:99999999px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:936px) and (max-width:960px),(min-width:99999999px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:935px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:936px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (width:960px){._2t8wLytikHzPCUnvXdS_wu:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:160px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:161px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:960px),(min-width:960px) and (max-width:1210px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:961px) and (max-width:960px),(min-width:1211px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:1095px),(min-width:960px) and (max-width:99999999px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1096px) and (max-width:960px),(min-width:99999999px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:1095px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1096px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (width:960px){._2t8wLytikHzPCUnvXdS_wu.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:63px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:64px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:863px),(min-width:960px) and (max-width:1113px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:864px) and (max-width:960px),(min-width:1114px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:998px),(min-width:960px) and (max-width:99999999px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:999px) and (max-width:960px),(min-width:99999999px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:998px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:999px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (width:960px){._2Ik7QEXtA-lbZKj0ssL89G:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:223px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:224px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:1023px),(min-width:960px) and (max-width:1273px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1024px) and (max-width:960px),(min-width:1274px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:1158px),(min-width:960px) and (max-width:99999999px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1159px) and (max-width:960px),(min-width:99999999px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:1158px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1159px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (width:960px){._2Ik7QEXtA-lbZKj0ssL89G.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:126px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:127px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:926px),(min-width:960px) and (max-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:927px) and (max-width:960px),(min-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:1061px),(min-width:960px) and (max-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1062px) and (max-width:960px),(min-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:1061px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1062px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (width:960px){.SwOx7KbRrXYrqQCWMYPf0:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:286px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:287px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:1086px),(min-width:960px) and (max-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1087px) and (max-width:960px),(min-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:1221px),(min-width:960px) and (max-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1222px) and (max-width:960px),(min-width:99999999px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:1221px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1222px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (width:960px){.SwOx7KbRrXYrqQCWMYPf0.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:189px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:190px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc):not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:989px),(min-width:960px) and (max-width:99999999px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:990px) and (max-width:960px),(min-width:99999999px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:1124px),(min-width:960px) and (max-width:99999999px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1125px) and (max-width:960px),(min-width:99999999px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:1124px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1125px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (width:960px){._2EcU45Nj3OvIEdu169RlLK:not(.FOPddbU-vkQ5LYmQP6Fgc)._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (max-width:349px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:350px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc:not(._2hXOR2fIcfnUg0p-Env7KQ) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:1149px),(min-width:960px) and (max-width:99999999px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1150px) and (max-width:960px),(min-width:99999999px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ:not(._3rHRwVOKmBBlBOQ4kIW_vq) ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (max-width:1284px),(min-width:960px) and (max-width:99999999px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1285px) and (max-width:960px),(min-width:99999999px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX{display:none}}@media (min-width:1284px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._2hr3tRWszeMRQ0u_Whs7t8{display:none}}@media (min-width:1285px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._14hLFU5cIJCyxH9DSgsCov._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}@media (width:960px){._2EcU45Nj3OvIEdu169RlLK.FOPddbU-vkQ5LYmQP6Fgc._2hXOR2fIcfnUg0p-Env7KQ._3rHRwVOKmBBlBOQ4kIW_vq ._1CUkbmFVuU6wklfYeYwPFk._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX._1YnPvd-E5MbmcM3PvRRcX{display:block}}
._3IuprPPEDVWAHB_tWQFgad{margin-right:8px}._1JwG70oEVxaFNeRI-8q_bd{display:inline-block}._1QhRdH9FgEwuJIYiBlnog8,.tfULaYlP83dV84XOxX3YE{height:16px;padding-right:4px;vertical-align:middle;width:12px}.hrV8gUgmt0V7wM2wgZ81l{margin-right:12px}.uoWjzSc1sqcAD_cLV6MWa{font-size:14px;line-height:18px;font-weight:500}.uoWjzSc1sqcAD_cLV6MWa,._1LXnp2ufrzN6ioaTLTjGQ1{color:var(--newCommunityTheme-actionIcon)}._1LXnp2ufrzN6ioaTLTjGQ1{font-size:12px;font-weight:700;line-height:16px;margin:4px 0 8px}._1LXnp2ufrzN6ioaTLTjGQ1 ._1g4YvNNIFoV_5_EhsVfyRy{margin-right:6px}._374Hkkigy4E4srsI2WktEd{border-radius:2px;-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;height:100%;line-height:20px;margin-right:4px;padding:6px 4px;text-align:left;transition:color .1s;white-space:nowrap}._374Hkkigy4E4srsI2WktEd:focus,._374Hkkigy4E4srsI2WktEd:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}._374Hkkigy4E4srsI2WktEd:first-letter{text-transform:uppercase}._374Hkkigy4E4srsI2WktEd:disabled{cursor:default}._2sGRD7t2kAbCLKrZ6UjoMW{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex}._2sGRD7t2kAbCLKrZ6UjoMW:before{content:"";border-left:1px solid var(--newCommunityTheme-line);height:20px;margin:6px 0;padding-left:6px}._3my60CXALAaQkY4P4xVmad{vertical-align:middle}._1VR6DV38j4rMT5OMeU4gJZ{padding:0 4px}
._3VH2iGVh92XtlKq0-eVoEN{position:absolute;z-index:3;overflow:hidden;pointer-events:none;border-radius:8px;top:0;bottom:0;left:3px;right:0}
.TmlaIdEplCzZ0F1aRGYQh{position:absolute;z-index:3;overflow:hidden;pointer-events:none;border-radius:8px;background:linear-gradient(188deg,rgba(255,230,0,.15) 1.7%,rgba(255,230,0,0) 46%),hsla(0,0%,100%,0);top:0;bottom:0;left:0;right:0;max-height:100px}
.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3 ._2m5vzALl8kQdr9kwIFUo5t{height:24px}.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3 ._22nWXKAY6OzAfK5GcUqWV2{padding:0}.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3 ._3ChHiOyYyUkpZ_Nm3ZyM2M{margin:4px;width:auto}.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3 ._3KgrO85L1p9wQbgwG27q4y{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-flow:row nowrap;flex-flow:row nowrap}.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3 ._1ewTEGuogtFmDvDII2T2Yy{margin:3px 4px 4px -4px;padding:0}.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3 ._2_lhaFUJdP8q0o2L9MN2TN{margin:4px 0}._1nGapmdexvR0BuOkfAi6wa{margin-left:8px;margin-right:8px;transition:width .05s,transform .05s;transition-timing-function:ease-out}._1nGapmdexvR0BuOkfAi6wa._1zN1-lYh2LfbYOMAho_O8g{margin:0;width:0;transform:translateX(-12px);opacity:0}._1nGapmdexvR0BuOkfAi6wa.O_Ica0k2O4KFcZyNfsJDU{opacity:1;transition-timing-function:ease-in;transform:translateX(0)}._3XArRVBsKuWegVHX9CQjH-{text-align:left}._3cjCphgls6DH-irkVaA0GM{padding:2px 0;width:100%}._3cjCphgls6DH-irkVaA0GM._2SI6K-u7PZ8koDfUmq7jlz{max-height:300px;overflow:hidden;position:relative}._3cjCphgls6DH-irkVaA0GM._2SI6K-u7PZ8koDfUmq7jlz:after{content:" ";position:absolute;bottom:0;left:0;height:20px;width:100%;background:linear-gradient(180deg,hsla(0,0%,100%,0) 0,var(--newRedditTheme-highlight))}.JchsqHyN3thfSnN8dUM3{margin-left:0;padding:2px}.JchsqHyN3thfSnN8dUM3:before{content:none}.ZvAy-PJfJmB8pzQxpz1sS{-ms-flex-item-align:start;align-self:flex-start}._3GfQMgsm3HGd3838lwqCST{position:relative;display:block;border-radius:50%;box-sizing:border-box}._3GfQMgsm3HGd3838lwqCST._3GfQMgsm3HGd3838lwqCST{height:28px;min-height:28px;min-width:28px;width:28px;border:0;margin:6px 0 0;-ms-flex-item-align:start;align-self:flex-start;font-size:28px;line-height:1}.zAxFYkzSByRTsKWHEMfFF.zAxFYkzSByRTsKWHEMfFF{height:20px;min-height:20px;min-width:20px;width:20px;border:0;margin:10px 0 0;-ms-flex-item-align:start;align-self:flex-start;font-size:20px;line-height:1}._13ScjOmi6dGdJw0JAonQEr{border-radius:50%;border:none}._3yYNickUtSp9utejxh7dFL{border:1px solid #2390d3}.PjnQ0fgBT0oSZ9nR8HeaJ{position:absolute;width:16px;height:16px;top:-6px;right:-6px;cursor:pointer}.kB7GZ7EzNg1Msq-nEnY0z{margin:6px -1px -2px 9px;max-height:40px;min-width:24px;text-align:center;z-index:3}._2m5vzALl8kQdr9kwIFUo5t{height:20px}._22nWXKAY6OzAfK5GcUqWV2{padding:2px}._3tw__eCCe7j-epNCKGXUKk{border-radius:4px;border:1px solid transparent;box-sizing:border-box;max-width:800px;width:calc(100% - 56px);padding:0;-ms-flex-item-align:start;align-self:flex-start;margin-left:6px}._3tw__eCCe7j-epNCKGXUKk._2R8NbVFaqNnBbuA7o2osje{opacity:.5}._3tw__eCCe7j-epNCKGXUKk._2zA6eSGIr_oQU7np0uNqoB{background-color:rgba(255,88,91,.05);border:2px solid #ff585b;margin-top:-4px;padding-left:4px;padding-top:4px}._3tw__eCCe7j-epNCKGXUKk.t8jgOblBrQTKWHnVy0zGD{background-color:rgba(255,214,53,.05);border:2px solid #ffd635;margin-top:-4px;max-width:808px;padding-left:4px;padding-right:4px;padding-top:4px}._3tw__eCCe7j-epNCKGXUKk._1vvFtxiq5874iIdCUYlL-d{border:1px solid var(--newCommunityTheme-postIcon)}._3tw__eCCe7j-epNCKGXUKk._2ym9uYDdCxu8P4UFCLNCgE{background-color:var(--newCommunityTheme-activeAlpha10)}.P8SGAKMtRxNwlmLz1zdJu{background:transparent;border-radius:4px;display:-ms-flexbox;display:flex;margin-left:-23px;position:relative;transition:color .5s,fill .5s,background 1s;padding:8px 0 0 8px;-ms-flex-align:center;align-items:center}.P8SGAKMtRxNwlmLz1zdJu._1z5rdmX8TDr6mqwNv7A70U{margin-top:8px}.P8SGAKMtRxNwlmLz1zdJu._1Sy9NCNbLA9uJZj-qgUrMG{background:var(--newCommunityTheme-buttonAlpha05)}.P8SGAKMtRxNwlmLz1zdJu._1z5rdmX8TDr6mqwNv7A70U{margin-top:16px}.P8SGAKMtRxNwlmLz1zdJu._1z5rdmX8TDr6mqwNv7A70U ._3tw__eCCe7j-epNCKGXUKk{margin-left:8px}.P8SGAKMtRxNwlmLz1zdJu._1z5rdmX8TDr6mqwNv7A70U ._3GfQMgsm3HGd3838lwqCST{height:28px;min-height:28px;min-width:28px;width:28px;border:0;margin:6px 0 0;-ms-flex-item-align:start;align-self:flex-start;font-size:28px;line-height:1}.P8SGAKMtRxNwlmLz1zdJu._1z5rdmX8TDr6mqwNv7A70U .zAxFYkzSByRTsKWHEMfFF{height:20px;min-height:20px;min-width:20px;width:20px;border:0;margin:10px 0 0;-ms-flex-item-align:start;align-self:flex-start;font-size:20px;line-height:1}.P8SGAKMtRxNwlmLz1zdJu._3nqqnHjXPJkfr8j5t_I85P{margin:0;padding:0}.P8SGAKMtRxNwlmLz1zdJu ._1nGapmdexvR0BuOkfAi6wa:hover+._3tw__eCCe7j-epNCKGXUKk ._1S45SPAIb30fsXtEcKPSdt{opacity:1}.P8SGAKMtRxNwlmLz1zdJu ._1S45SPAIb30fsXtEcKPSdt{margin-left:0;min-height:18px;margin-bottom:6px}.P8SGAKMtRxNwlmLz1zdJu ._1S45SPAIb30fsXtEcKPSdt._3LqBzV8aCO9tge99jHiUGy{margin-top:10px}.P8SGAKMtRxNwlmLz1zdJu ._1S45SPAIb30fsXtEcKPSdt._3c9Go6433BnvYx8_7MkPnt{margin-bottom:0}.P8SGAKMtRxNwlmLz1zdJu._2ym9uYDdCxu8P4UFCLNCgE{background-color:var(--newCommunityTheme-activeAlpha10)}._2jhbZV6mVCM5Ma7Z376DW2{position:relative}._2jhbZV6mVCM5Ma7Z376DW2:before{border-left:2px solid var(--newCommunityTheme-line);bottom:0;content:" ";left:-22px;position:absolute;top:1px}._2CkgPEY8ljDZH3np9UY1ws{visibility:hidden;position:absolute;left:-99999px;top:0}
._2IpBiHtzKzIxk2fKI4UOv1{font-size:12px;font-weight:400;line-height:16px;color:var(--newRedditTheme-metaText);display:-ms-flexbox;display:flex}._vaFo96phV6L5Hltvwcox{display:block;margin-right:12px}._vaFo96phV6L5Hltvwcox:last-of-type{margin-right:0}
.icon._1-Dnj_BC9slzHImx9Qex6x{color:var(--newRedditTheme-button);font-size:12px;width:12px}._3Wz607wX-KXslTUjYvTZWi._3Wz607wX-KXslTUjYvTZWi,._3xeOZ4NlqvpwzbB5E8QC6r,._1wxi9M8fCejzbsH0YGSer2{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-flow:row wrap;flex-flow:row wrap}._305seOZmrgus3clHOXCmfs{font-size:12px;font-weight:400;line-height:16px;color:var(--newRedditTheme-metaText);color:var(--newRedditTheme-bodyText)}._305seOZmrgus3clHOXCmfs:hover{text-decoration:underline}._2QZLJe3l7lBGN9JNI51gn9{font-weight:700}.id5ExZR7GqiUypGICnSYs.id5ExZR7GqiUypGICnSYs{border-radius:100%;height:20px;margin-right:4px;vertical-align:middle;width:20px}.id5ExZR7GqiUypGICnSYs._3dUPuwEf-ssCOozUxvm-HX{height:32px;width:32px;font-size:32px;line-height:1}._2vYQV4h1KDa5M62EoOG3t-{margin:0 0 0 4px}._3zxBrqnz24HT1z7OOcRXCS{font-size:12px;font-weight:400;line-height:16px;color:var(--newRedditTheme-metaText)}._3-fo1J0EWS8TawiUkoZ9DH{margin-right:4px}.icon._3hvmfTpZq_W24eaylznBmS{border-radius:9999px;color:#0079d3}.icon._3hvmfTpZq_W24eaylznBmS._15ad3usdVw8bRqdw2I-vhN{background-color:#0079d3;color:#fff}.icon._3hvmfTpZq_W24eaylznBmS._35xBFzll_c4A2_N9fEuuuY{filter:blur(6px)}._3d8GzWNAiVF7ncwmjHXlNf{display:contents}
._3qUPSbrS00ULxlso5V3tIN{font-size:12px;font-weight:500;line-height:16px;display:inline-block;margin-right:8px;text-transform:uppercase;white-space:nowrap}._3qUPSbrS00ULxlso5V3tIN:last-of-type{margin-right:0}.icon._1fMbGLM3cAHfas4PNZTps4{font-size:12px;line-height:16px;margin-right:4px}._1fMbGLM3cAHfas4PNZTps4.Ap9gKlmTQdcI17NgCE4yQ{width:12px;height:12px;margin-right:4px;vertical-align:middle}._2cvv3TnzlFQHZE4upgevMn{color:var(--newRedditTheme-quarantine)}._2cvv3TnzlFQHZE4upgevMn ._1fMbGLM3cAHfas4PNZTps4{fill:var(--newRedditTheme-quarantine)}._1-dYjh5S-IQybef811XyCF{color:var(--newRedditTheme-nsfw)}._1-dYjh5S-IQybef811XyCF ._1fMbGLM3cAHfas4PNZTps4{fill:var(--newRedditTheme-nsfw)}._1P0ASR__enq34IxkSim2Rk{color:var(--newRedditTheme-checkbox)}._1P0ASR__enq34IxkSim2Rk ._1fMbGLM3cAHfas4PNZTps4{fill:var(--newRedditTheme-checkbox)}
._2dkUkgRYbhbpU_2O2Wc5am{cursor:pointer;overflow:hidden;position:relative;border:thin solid var(--newRedditTheme-postLine);margin-top:-1px;max-width:100%}._2dkUkgRYbhbpU_2O2Wc5am:hover{border:thin solid var(--newRedditTheme-postIcon);z-index:1}._28efb5XEIggTEMzT5v9i61{border-radius:4px 4px 0 0;margin-top:0}._1rd6n9Xvtg4-5Vw7E3NhEh._1rd6n9Xvtg4-5Vw7E3NhEh{margin-bottom:0}._2i5O0KNpb9tDq0bsNOZB_Q{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column}._37TF67KpZQl9SHbiAhz3mf{padding-top:16px;padding-bottom:4px}._1nfcZWg35_OmccxqivQ1EN{padding-bottom:4px}._19FzInkloQSdrf0rh3Omen{display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between}.HNL__wz5plDpzJe5Lnn{padding-top:8px;padding-bottom:16px}.a6Bzb7gqvN3mqBOAEyFIv{font-size:12px;font-weight:400;line-height:16px;margin:0;white-space:nowrap;color:var(--newRedditTheme-linkText);fill:var(--newRedditTheme-linkText)}.a6Bzb7gqvN3mqBOAEyFIv:visited{color:var(--newRedditTheme-linkTextWithBody);fill:var(--newRedditTheme-linkTextWithBody)}._1FT0e6kh1BBb_oALAMW_l7{font-size:16px;font-weight:500;line-height:20px}._1-SZ3VwLjbFwTzaZvU8FBX{color:var(--posttitletextcolor);display:inline;word-wrap:break-word}a:visited ._1-SZ3VwLjbFwTzaZvU8FBX{color:var(--postTitleLink-VisitedLinkColor)}._2r9BZFotuBbLYnijAaskeZ{transition:filter .5s;height:98px;width:138px;border:none;border-radius:4px}._2r9BZFotuBbLYnijAaskeZ.rIj9lvusQvb0-Mf16X6ZL{background-size:cover;filter:blur(60px)}.PrfaR-luawcEBK2dhGuDp{border-radius:4px;-ms-flex:1;flex:1;height:100%;width:100%;overflow:hidden;position:relative;vertical-align:bottom}.Gk-MlLujgqsaX1n-sGa_O{display:none;padding-left:8px}@media (min-width:320px){.Gk-MlLujgqsaX1n-sGa_O{display:-ms-flexbox;display:flex;-ms-flex:0 0 138px;flex:0 0 138px;height:98px}}@media (min-width:375px){.Gk-MlLujgqsaX1n-sGa_O{display:-ms-flexbox;display:flex;-ms-flex:0 0 138px;flex:0 0 138px;height:98px}}@media (min-width:414px){.Gk-MlLujgqsaX1n-sGa_O{display:-ms-flexbox;display:flex;-ms-flex:0 0 138px;flex:0 0 138px;height:98px}}@media (min-width:478px){.Gk-MlLujgqsaX1n-sGa_O{display:-ms-flexbox;display:flex;-ms-flex:0 0 138px;flex:0 0 138px;height:98px}}._1Nh8xLEUG3orjY1k1aijj{background-color:var(--newRedditTheme-search-syntaxHighlightBackgroundColor);color:var(--newRedditTheme-search-syntaxHighlightColor)}._2n04GrCyhhQf-Kshn7akmH{padding-left:16px;padding-right:16px}._1yBpz1MEPxxYTxjlEilGtB{padding-right:4px}._1SAKlLic4t9BBtiiE-Z6ob{visibility:hidden;position:absolute;left:-99999px;top:0}.nbO8VWsMIB-Mv-tIa37NF{--posttitletextcolor:var(--newRedditTheme-titleText);--postTitle-VisitedLinkColor:var(--newRedditTheme-titleText);--postTitleLink-VisitedLinkColor:var(--newRedditTheme-titleText)}.UcytmAhLeRTIrWR81xl4P{position:relative}._1AKeAGcglmBjK1SUUXNFti{display:inline}
._2lwxooVpRNqH_bjx-Nm4m4{padding:0 16px}._1nhxJR41hD8jXWqUVy3wTT{display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between}._1HsM08P8HBGOIPATQsthMA{margin-bottom:12px}._1i_lg5WToFS_KM8bSao5FB,._1HsM08P8HBGOIPATQsthMA{color:var(--newRedditTheme-titleText)}._1i_lg5WToFS_KM8bSao5FB{border-radius:4px;background-color:var(--newRedditTheme-highlight);font-size:14px;margin:0 12px 12px;padding:4px 8px 8px}.q6Rzyt18sGpgOFFoG9gUg{margin-bottom:12px}._3bkDvRYnc0SodO59dk5n3p{margin-top:8px}._3Yys9Taiw4B3XiXhmbLrra._3Yys9Taiw4B3XiXhmbLrra{display:block;font-size:12px;font-weight:400;margin:0 0 4px 8px;min-height:0;padding:0;text-align:left}i._14gjyiBw0XSVan9XLN7ER-{background-color:var(--newRedditTheme-metaText);border-radius:4px;color:#fff;font-size:10px;height:10px;line-height:10px;margin-left:12px;padding:4px;width:10px}
._2u_haOaI877DTCSOfFouuF{background-color:var(--newRedditTheme-postTransparent20);border-bottom:thin solid var(--newRedditTheme-postLine);display:-ms-flexbox;display:flex;width:100vw;max-width:100%}@media (min-width:640px){._2u_haOaI877DTCSOfFouuF{width:calc(100vw - 48px)}}@media (min-width:960px){._2u_haOaI877DTCSOfFouuF{width:100%}}._2Uv1IcU4LjDH6OqbNZ0BwO{padding:0 32px}.yNjWq2s_3V0N5m9u-Bx-D{height:150px}.-fCtQc5X_zwd1tnX_0s4W{height:20px;width:100px}.tSwYm_NW9-rD1G91vZi4d{padding:8px 32px}
._3BWq3z8_9gA3oThgYXnngR{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;margin-top:-1px;padding:16px}._3BWq3z8_9gA3oThgYXnngR:not(.iwmtpuJa21jtA4y_LuOVI){border:thin solid var(--newCommunityTheme-postLine);padding:16px}._3BWq3z8_9gA3oThgYXnngR.YLZe4_XS9hOtObp1VjEF-{border-radius:4px 4px 0 0}._3BWq3z8_9gA3oThgYXnngR.iwmtpuJa21jtA4y_LuOVI{border-bottom:thin solid var(--newCommunityTheme-postLine);padding-bottom:16px}.ei8_Bq_te0jjwNIqmk8Tw{-ms-flex-align:center;align-items:center;display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between}.YLZe4_XS9hOtObp1VjEF-{padding-top:16px}._2YBzxh6YUsSdcmbcJ-kE5L,.icon._2YBzxh6YUsSdcmbcJ-kE5L{font-size:36px;height:36px;max-height:36px;max-width:36px;overflow:hidden;width:36px;line-height:normal;-ms-flex-negative:0;flex-shrink:0}._2YBzxh6YUsSdcmbcJ-kE5L.iwmtpuJa21jtA4y_LuOVI,.icon._2YBzxh6YUsSdcmbcJ-kE5L.iwmtpuJa21jtA4y_LuOVI{width:32px;height:32px;font-size:32px;line-height:1}._1Nla8vW02K39sy0E826Iug{-ms-flex-positive:1;flex-grow:1;padding:0 8px;overflow:hidden;overflow-wrap:break-word}._1nTSkRaTteYjCY91DwVEF3{display:-ms-flexbox;display:flex;-ms-flex-align:baseline;align-items:baseline}._1nTSkRaTteYjCY91DwVEF3.iwmtpuJa21jtA4y_LuOVI{-ms-flex-direction:column;flex-direction:column}._2torGbn_fNOMbGw3UAasPl{font-size:12px;font-weight:500;line-height:16px;color:var(--newRedditTheme-bodyText);font-weight:700}._2torGbn_fNOMbGw3UAasPl.iwmtpuJa21jtA4y_LuOVI{max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}._2torGbn_fNOMbGw3UAasPl:hover{text-decoration:underline}._3CUjJH8t2eFynKUAv1ER7C{font-size:12px;font-weight:400;line-height:16px;color:var(--newRedditTheme-metaText)}._3sOM1thDS-RiUzmUb8yzxN{margin:0 0 0 4px;width:-webkit-fit-content;width:fit-content}._3JYXhJlwZCvjZTBplEncbq{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:18px;color:var(--newRedditTheme-metaText)}._3JYXhJlwZCvjZTBplEncbq.iwmtpuJa21jtA4y_LuOVI{margin-top:4px}._3llSmEBMCJTcO537oPxHIH{-ms-flex-negative:0;flex-shrink:0;width:88px}._1QstT010Ns0i6YkU4n5O25{margin-left:4px}._1QstT010Ns0i6YkU4n5O25.iwmtpuJa21jtA4y_LuOVI{margin-left:0}
._2-tXnoxd32Utasnz79k34{-ms-flex-align:center;align-items:center;box-sizing:border-box;border-bottom:thin solid var(--newCommunityTheme-postLine);display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;margin-top:-1px;max-width:100%;padding:16px;width:100%}._2-tXnoxd32Utasnz79k34._2PlcVxaNCQS2-GyaX_mhOA{width:auto}@media (min-width:640px){._2-tXnoxd32Utasnz79k34._2PlcVxaNCQS2-GyaX_mhOA{width:auto}}._3yGdKsP-cHl-Cb_SH-PyXp{border-radius:9999px;height:36px;width:36px}.Lsafh1CsbqQ8tiuBPTucl{-ms-flex-positive:1;flex-grow:1;padding:0 8px}._1TKuN8SZONE4tjAoEul8sp{display:-ms-flexbox;display:flex}._1TKuN8SZONE4tjAoEul8sp._2PlcVxaNCQS2-GyaX_mhOA{-ms-flex-direction:column;flex-direction:column}._1TKuN8SZONE4tjAoEul8sp._2PlcVxaNCQS2-GyaX_mhOA :first-child{margin-bottom:4px}._11V3zVIqp59I7JvzWnky0w{height:16px;width:50px}._2GNPL8YTca77gPEWlF9nDb{height:16px;width:100px}._3C8z4MmIB_gou30f3ojB0V{height:28px;margin-top:4px;width:100%}._14X6ixd8jgBYsNSxRPXTbL{border-radius:9999px;height:32px;width:88px}
.GdWkLdr7ToYAI7A1BuDdw{font-size:12px;font-weight:700;line-height:16px}.GdWkLdr7ToYAI7A1BuDdw,._2UJq3kiv6y_oSPPmQyFMxy{color:var(--newRedditTheme-titleText)}._2UJq3kiv6y_oSPPmQyFMxy{border-radius:4px;background-color:var(--newRedditTheme-highlight);cursor:pointer;padding:8px}._2nHutt97wCf1b9Txz8_Y67{border-top:1px solid var(--newRedditTheme-placeholder);padding:16px 0}._2nHutt97wCf1b9Txz8_Y67.B1l5QN6o0c-5KGYHlANBw{border-top:none}.vz6ezPSNwnMTVPF3HcJiw{margin-right:4px}._6PV9rgxHCsT7DD2OrVvJ0{padding-left:4px}._3jLdjJWF8IlmuZ7sysSq0g{margin-top:8px}._3KLHXM3DEshAA3TDpGD_4a{margin:0 48px 4px}.tuXecQytAjq5ReXeDFhPI{color:var(--newCommunityTheme-metaText)}._3bUukUiGtOzLXmGTBi1yXx{font-size:12px;font-weight:400;line-height:16px}._3SUyRHeYoSqKJ0It_8jTAQ{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center}._1UhP-2TSDqqzDUVoNfS4Nm{padding:0 4px}._3DCfB-ynh0K_m_xbYTL_Ne{border-radius:100%;font-size:20px;height:20px;width:20px}
*>._2kqt-kRLvKQ1Kqi8OjMEa7{margin-bottom:24px}:last-child>._2kqt-kRLvKQ1Kqi8OjMEa7{margin-bottom:0}
._2mO8vClBdPxiJ30y_C6od2{background:var(--newRedditTheme-post);border-radius:4px;box-shadow:0 2px 4px 0 rgba(0,0,0,.06);max-width:100%}._1hYBlRBooHG-eY5iAHen-R{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;color:var(--newRedditTheme-actionIcon)}._1LvQXvsxpSVi-JRudk3e4e{background:rgba(0,0,0,.1);height:1px;margin-top:4px;width:100%}._3MfNPE_vLKliHPkiYMAtZm{margin-top:8px}._1mLDB-TFHMY0SRGTRD-ipK{margin-top:24px}.DMHO9Pay4I5LSwZTtE4TY{font-size:12px;font-weight:700;letter-spacing:.5px;line-height:24px;text-transform:uppercase;color:var(--newRedditTheme-button);display:block;margin-top:16px}
._1MTbwSHIISfMYM16YhZ8kN{margin-bottom:16px}
._365FiUZ11efXHV7l7fNp6K{display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;text-align:center;transform:translateY(-100%)}
._1G4yU68P50vRZ4USXfaceV{background-color:var(--newCommunityTheme-widgetColors-sidebarWidgetBackgroundColor);color:var(--newCommunityTheme-widgetColors-sidebarWidgetTextColor);fill:var(--newCommunityTheme-widgetColors-sidebarWidgetTextColor);border:1px solid var(--newCommunityTheme-widgetColors-sidebarWidgetBorderColor);border-radius:4px;overflow:visible;word-wrap:break-word}._1G4yU68P50vRZ4USXfaceV._2mtWlchu4uQf339v56bSha{cursor:pointer}._1G4yU68P50vRZ4USXfaceV._2QeqBqfT5UbHBoViZUt-wX{background-color:var(--newRedditTheme-widgetColors-sidebarWidgetBackgroundColor);border-color:var(--newRedditTheme-widgetColors-sidebarWidgetBorderColor);color:var(--newRedditTheme-bodyText);fill:var(--newRedditTheme-bodyText)}._1G4yU68P50vRZ4USXfaceV._1lvCNVth3dt5y8lu3vT95L{position:relative}._1G4yU68P50vRZ4USXfaceV._1lvCNVth3dt5y8lu3vT95L:after{content:"";background:linear-gradient(180deg,transparent,var(--newRedditTheme-widgetColors-sidebarWidgetBackgroundColor));height:70px;width:100%;position:absolute;bottom:30px;right:0}._ZhON3a3vplThB8NFwuJn{font-size:10px;font-weight:700;letter-spacing:.5px;line-height:12px;text-transform:uppercase;background-color:var(--newCommunityTheme-widgetColors-sidebarWidgetHeaderColor);border-radius:3px 3px 0 0;color:var(--newCommunityTheme-widgetColors-sidebarWidgetTitleColor);display:-ms-flexbox;display:flex;fill:var(--newCommunityTheme-widgetColors-sidebarWidgetTitleColor);padding:0 12px 12px}._ZhON3a3vplThB8NFwuJn._2mtWlchu4uQf339v56bSha{cursor:pointer}._ZhON3a3vplThB8NFwuJn h2{font-size:14px;font-weight:500;line-height:18px;font-weight:700;text-transform:none}._ZhON3a3vplThB8NFwuJn a:not([disabled]),._ZhON3a3vplThB8NFwuJn button:not([disabled]){border-radius:2px}._ZhON3a3vplThB8NFwuJn a:not([disabled]):focus,._ZhON3a3vplThB8NFwuJn a:not([disabled]):hover,._ZhON3a3vplThB8NFwuJn button:not([disabled]):focus,._ZhON3a3vplThB8NFwuJn button:not([disabled]):hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}._ZhON3a3vplThB8NFwuJn a[disabled],._ZhON3a3vplThB8NFwuJn button[disabled]{cursor:not-allowed}._2sggAEfRQLyoAl4J__5twU{padding:12px 0 0}.TmgZY6tDcdErbE5d7E0HJ{padding:12px}._3RPJ8hHnfFohktLZca18J6{padding:0}.r5dzQq7dgZyAmve8abbbt{overflow:hidden}._3dbp6Cm9uKkkIBr9EsU-qS{margin-bottom:4px}
._1uqw13duLAypklZz9JuxH5{-ms-flex-align:center;align-items:center;background:var(--newCommunityTheme-inactive);border:1px solid transparent;border-radius:24px;cursor:pointer;display:-ms-flexbox;display:flex;-ms-flex:1;flex:1;height:48px;margin:8px 2px;overflow-wrap:anywhere}._1uqw13duLAypklZz9JuxH5:hover{background:var(--newCommunityTheme-field)}._1uqw13duLAypklZz9JuxH5.C0ynfBku9Az2wYA9j1_PA{background:#ffede5;border:1px solid #d93a00;fill:#d93a00}._1uqw13duLAypklZz9JuxH5._3JYkv3aRJq9WBVU_Qu_O3K{background:#340e00;border:1px solid #d93a00;fill:#d93a00}._1uqw13duLAypklZz9JuxH5 ._2go248Acx87AyaspT-IqC3{display:-ms-flexbox;display:flex;-ms-flex:1;flex:1;-ms-flex-pack:end;justify-content:flex-end;-webkit-user-select:none;-ms-user-select:none;user-select:none}._1uqw13duLAypklZz9JuxH5 ._2go248Acx87AyaspT-IqC3 .Nqikdy52FO7Ok8SC7YbBy{height:18px;width:18px;margin-right:17px}._1uqw13duLAypklZz9JuxH5 ._3qzPnI-sCnXtXXzmiLCUzt{-ms-flex:1;flex:1}._1uqw13duLAypklZz9JuxH5 ._5Rt2rPaHLuyB5smTxh9cS{font-size:16px;font-weight:500;overflow:hidden;text-overflow:ellipsis;line-height:20px;max-height:20px;display:-webkit-inline-box;-webkit-line-clamp:1;white-space:normal;-webkit-box-orient:vertical;display:flex;justify-content:center;flex:4}._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O{-ms-flex-align:center;align-items:center;border-radius:9999px;box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;position:relative;text-align:center;width:auto;font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:unset;line-height:17px;text-transform:unset;min-height:32px;min-width:32px;padding:4px 16px}._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O ._1ym0rG9P61fqq5EGeggDEg,._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O i.icon._1ym0rG9P61fqq5EGeggDEg{display:inline-block;padding:0 8px 0 0;height:20px;width:20px;font-size:20px;line-height:20px}._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O ._1ym0rG9P61fqq5EGeggDEg._1wilU6X1e2oYYu84p5M0Bn,._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O i.icon._1ym0rG9P61fqq5EGeggDEg._1wilU6X1e2oYYu84p5M0Bn{float:left}._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O ._1ym0rG9P61fqq5EGeggDEg._1N6ONFJor0MYB1AANfCh8M,._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O i.icon._1ym0rG9P61fqq5EGeggDEg._1N6ONFJor0MYB1AANfCh8M{float:right}._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O:nth-child(4n+0){width:150px}._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O:nth-child(4n+1){width:75px}._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O:nth-child(4n+2){width:120px}._1uqw13duLAypklZz9JuxH5 ._3gtRwVx6uS2xZaynYajI9O:nth-child(4n+3){width:175px}._2GUwrGUdKWdruRBy2ogOPv{padding-bottom:85px}.sKUGLH9bgXYnkNvi71PD6{margin-bottom:24px}._34OOuEVRtCgQHxTw6Bm_SM{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px;font-weight:600;margin:16px 0 8px;text-align:center}._2NBWDPVfLgJchMUSilY9hq{-ms-flex-align:center;align-items:center;-ms-flex-direction:column;flex-direction:column;width:270px;height:223px;background:var(--newRedditTheme-body);box-shadow:0 16px 32px rgba(0,0,0,.25),0 12px 12px rgba(0,0,0,.15);border-radius:8px;position:fixed;bottom:100px;right:50px;z-index:200}._1D3-VzG8d-pAsDFC2aDEqX,._2NBWDPVfLgJchMUSilY9hq{display:-ms-flexbox;display:flex}._1D3-VzG8d-pAsDFC2aDEqX{-ms-flex-pack:end;justify-content:flex-end;padding:17px 17px 0 235px}.Z2DAjXDKT-rjUoOgPeR9b{cursor:pointer;width:16px;height:16px}._6pr2vYjViLknuzg7J_4II{font-size:16px;font-weight:400;line-height:20px;font-weight:600;padding:0 30px 6px;width:200px}._1j479fpdJDH2JNDpssXW8Z,._6pr2vYjViLknuzg7J_4II{font-family:Noto Sans,Arial,sans-serif;color:var(--newRedditTheme-bodyText);text-align:center}._1j479fpdJDH2JNDpssXW8Z{padding-bottom:16px}.piSYz03CLXLD5jdQwPjUy,._1j479fpdJDH2JNDpssXW8Z{font-size:12px;line-height:16px;font-weight:400}.piSYz03CLXLD5jdQwPjUy{font-family:Noto Sans,Arial,sans-serif;background:var(--newRedditTheme-button);border:1px solid transparent;border-radius:24px;color:var(--newRedditTheme-body);cursor:pointer;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;font-weight:600;height:32px;width:230px}.piSYz03CLXLD5jdQwPjUy.Fssd937Pdx1KOrc1lhBS5{background:var(--newRedditTheme-inactive);color:var(--newRedditTheme-bodyText);margin-top:8px}
._3Y8af3R9_DE3lpXa6Hq5Ab{background-color:transparent;color:grey;padding:8px}._3Y8af3R9_DE3lpXa6Hq5Ab a{margin:0 4px}._2wqyhtudP4weVGsZdVXJgt{margin-top:16px}._1KrMye71CT332tKKKUWAj6{display:-ms-flexbox;display:flex;padding-top:8px;padding-bottom:8px;margin-left:12px;margin-right:12px}._1KrMye71CT332tKKKUWAj6:not(:last-of-type){border-bottom:1px solid #e9ebed}._3f2nSSsPBqVDV6Sz82qgrR{display:-ms-flexbox;display:flex;-ms-flex-flow:column nowrap;flex-flow:column nowrap;width:50%;padding:0 4px}._3Eyh3vRo5o4IfzVZXhaWAG{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px;display:inline-block;text-decoration:none;text-transform:capitalize;margin-top:3px;margin-bottom:3px}._3GijmRx58E2GzbuzKVHDex{text-transform:none}._34dh2eyzMvJfjCBLeoWiDD{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:16px;display:-ms-flexbox;display:flex;padding:12px}
._1oRQu-aolgpPPJDblUGTw5{-ms-flex:1 1 auto;flex:1 1 auto;position:relative;width:inherit}._3Tc8YYRhVDX9vlR0XePZfH{margin-top:45px}._3Tc8YYRhVDX9vlR0XePZfH,.xTKAJNhaO7iI3cnAQ1PpJ{position:-webkit-sticky;position:sticky}.xTKAJNhaO7iI3cnAQ1PpJ{bottom:0}._1vYrJH5uc57mZQJPN4l34E{top:57px}._1vYrJH5uc57mZQJPN4l34E,._2s8GkMW_LrglF6lvNpBQgE{position:-webkit-sticky;position:sticky}._2s8GkMW_LrglF6lvNpBQgE{top:105px}._2Fh9XKrAUp6CQHSgW98LEb{top:101px}
._2NAcQAOfOGlsoihoqpSHTh{padding-top:4px;width:100%}._1nkSNshm5FPoOguxeVwxcD{display:-ms-flexbox;display:flex;margin-left:auto}.ij57zT3Rtmsew_4V8vYmY{display:block;margin-bottom:3px;margin-right:5px;max-width:100%;overflow:hidden;text-overflow:ellipsis}.ij57zT3Rtmsew_4V8vYmY.l8B49A4v1dhWGGEwM7vYA{display:inline-block;max-width:97%}.ij57zT3Rtmsew_4V8vYmY._1Dpo5nORF-CHLCeoDHpZuR{padding-bottom:8px}._3b9QdopIknN9AuNvj2kI9X{margin-right:0;max-width:100%}.ij57zT3Rtmsew_4V8vYmY.XUSGYTFEMdkVpqVqn1ZsC ._3b9QdopIknN9AuNvj2kI9X{position:relative}.ij57zT3Rtmsew_4V8vYmY.XUSGYTFEMdkVpqVqn1ZsC ._3b9QdopIknN9AuNvj2kI9X button{position:absolute;right:12px}.qHKWh5t-0ZHqZ00w567bU{overflow:hidden;margin-bottom:5px;transition:max-height .3s ease-out}._1Uh_u9ypgpntBJ_2RC1Ge3{padding:0 12px}
._3W4fKI_ey_jDfiIO7ElMuP{cursor:pointer;overflow:hidden;position:relative;border-radius:4px;margin-bottom:12px;border:thin solid var(--newCommunityTheme-postLine)}._3W4fKI_ey_jDfiIO7ElMuP:hover{border:thin solid var(--newRedditTheme-postIcon);z-index:1}._2IeaiLn4GyfAXKD1TLrIS1._2IeaiLn4GyfAXKD1TLrIS1{margin-bottom:0}._3zoWB97jg8GAUJCl4XA57a{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column}._3xctgCPJ_3knmtE3O9TQzE{padding:16px}._3CAq9fn45Es59QdDzgtbhZ{padding:0 16px;margin-bottom:16px}.oNxebZMPvUlTJIOtprxhP{padding:8px 16px}._1eIKxpeFNBTQ699qAcQRbd{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-pack:center;justify-content:center;height:225px;border-radius:4px;max-width:100%;padding:0 16px;margin-bottom:16px;overflow:hidden}._1eIKxpeFNBTQ699qAcQRbd._3IElQYxAJq_0qRyeyMDc_K{margin-bottom:0}._1eIKxpeFNBTQ699qAcQRbd.Tzfi4PWE-V9cQ78MJ3GkX{overflow:initial;height:inherit}._1eIKxpeFNBTQ699qAcQRbd._1yoxdnJLJUmMiTSTn_QkNJ{height:auto}._1zcwL6v8t8G0OHvf5D4WW-{display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;-ms-flex-align:center;align-items:center;height:100%;width:100%}._2ZlSdmjvWREfUPvdtzIAN_{position:relative}._2dnz6aKPWeFF1opQ_XsTYW{-webkit-mask-image:none;mask-image:none;overflow:hidden}._2oliTAoFFxS1mse-sOZinV{font-size:12px;font-weight:400;line-height:16px;bottom:0;padding:10px;position:absolute;right:0;white-space:nowrap;color:var(--newCommunityTheme-linkText);fill:var(--newCommunityTheme-linkText)}._2oliTAoFFxS1mse-sOZinV:visited{color:var(--newCommunityTheme-linkTextWithBody);fill:var(--newCommunityTheme-linkTextWithBody)}._2oliTAoFFxS1mse-sOZinV:hover{text-decoration:underline}.p35vRG-PK5zfK-G5gjGAr{margin:0 16px;background-color:inherit;border-bottom:1px solid var(--newCommunityTheme-field)}._16eWoJfxv365opQYh3dOAJ{margin:0}._16eWoJfxv365opQYh3dOAJ._1fSEjc0jhvt02_0z07145y{color:var(--newRedditTheme-bodyText);fill:var(--newRedditTheme-bodyText)}.BMx4T197BjzZgmRjegR7y{position:relative;background-color:var(--newCommunityTheme-field);border:1px solid transparent;color:var(--newCommunityTheme-button);fill:var(--newCommunityTheme-button)}.BMx4T197BjzZgmRjegR7y:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-button);opacity:0}.BMx4T197BjzZgmRjegR7y:hover:before{opacity:.08}.BMx4T197BjzZgmRjegR7y:focus{outline:none}.BMx4T197BjzZgmRjegR7y:focus:before{opacity:.16}.BMx4T197BjzZgmRjegR7y._28VWbryTIGJPb62Ey50lm8:before,.BMx4T197BjzZgmRjegR7y:active:before{opacity:.24}.BMx4T197BjzZgmRjegR7y:disabled,.BMx4T197BjzZgmRjegR7y[data-disabled],.BMx4T197BjzZgmRjegR7y[disabled]{cursor:not-allowed;filter:grayscale(1);background:none;color:var(--newCommunityTheme-buttonAlpha50);fill:var(--newCommunityTheme-buttonAlpha50)}.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o{position:relative;background-color:var(--newCommunityTheme-field);border:1px solid transparent;color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-button);opacity:0}.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o:hover:before{opacity:.08}.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o:focus{outline:none}.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o:focus:before{opacity:.16}.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o._28VWbryTIGJPb62Ey50lm8:before,.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o:active:before{opacity:.24}.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o:disabled,.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o[data-disabled],.BMx4T197BjzZgmRjegR7y.n1f3mSINfKiMWmz1fdi1o[disabled]{cursor:not-allowed;filter:grayscale(1);background:none;color:var(--newRedditTheme-buttonAlpha50);fill:var(--newRedditTheme-buttonAlpha50)}
.cmR5BF4NpBUm3DBMZCmJS{-ms-flex-align:center;align-items:center;border-radius:9999px;box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;text-align:center;width:auto;position:relative;background-color:var(--newCommunityTheme-button);border:none;color:var(--newCommunityTheme-body);fill:var(--newCommunityTheme-body);font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:unset;line-height:17px;text-transform:unset;min-height:32px;min-width:32px;padding:4px 16px}.cmR5BF4NpBUm3DBMZCmJS:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-body);opacity:0}.cmR5BF4NpBUm3DBMZCmJS:hover:before{opacity:.08}.cmR5BF4NpBUm3DBMZCmJS:focus{outline:none}.cmR5BF4NpBUm3DBMZCmJS:focus:before{opacity:.16}.cmR5BF4NpBUm3DBMZCmJS._2dj14FxV-bfkwopj1jV_fF:before,.cmR5BF4NpBUm3DBMZCmJS:active:before{opacity:.24}.cmR5BF4NpBUm3DBMZCmJS:disabled,.cmR5BF4NpBUm3DBMZCmJS[data-disabled],.cmR5BF4NpBUm3DBMZCmJS[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:var(--newCommunityTheme-buttonTinted80);color:var(--newCommunityTheme-bodyAlpha50);fill:var(--newCommunityTheme-bodyAlpha50)}.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D{position:relative;background-color:var(--newRedditTheme-button);border:none;color:var(--newRedditTheme-body);fill:var(--newRedditTheme-body)}.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-body);opacity:0}.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D:hover:before{opacity:.08}.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D:focus{outline:none}.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D:focus:before{opacity:.16}.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D._2dj14FxV-bfkwopj1jV_fF:before,.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D:active:before{opacity:.24}.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D:disabled,.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D[data-disabled],.cmR5BF4NpBUm3DBMZCmJS.C64b9palJF2n26mG_1q3D[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:var(--newRedditTheme-buttonTinted80);color:var(--newRedditTheme-bodyAlpha50);fill:var(--newRedditTheme-bodyAlpha50)}.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz{position:relative;background-color:#ff585b;border:none;color:var(--newCommunityTheme-body);fill:var(--newCommunityTheme-body)}.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-body);opacity:0}.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz:hover:before{opacity:.08}.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz:focus{outline:none}.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz:focus:before{opacity:.16}.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz._2dj14FxV-bfkwopj1jV_fF:before,.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz:active:before{opacity:.24}.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz:disabled,.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz[data-disabled],.cmR5BF4NpBUm3DBMZCmJS._1aqI4zAQaNw-k6Jp5j3WJz[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:#ff595c;color:var(--newCommunityTheme-bodyAlpha50);fill:var(--newCommunityTheme-bodyAlpha50)}.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD{position:relative;background-color:#ddbd37;border:none;color:var(--newCommunityTheme-body);fill:var(--newCommunityTheme-body)}.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-body);opacity:0}.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD:hover:before{opacity:.08}.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD:focus{outline:none}.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD:focus:before{opacity:.16}.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD._2dj14FxV-bfkwopj1jV_fF:before,.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD:active:before{opacity:.24}.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD:disabled,.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD[data-disabled],.cmR5BF4NpBUm3DBMZCmJS.Vi9jnbb9vJd6ugulSJIAD[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:#eede9b;color:var(--newCommunityTheme-bodyAlpha50);fill:var(--newCommunityTheme-bodyAlpha50)}.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je{--buttonText:#fff;position:relative;background-color:#ff4500;border:none;color:var(--buttonText);fill:var(--buttonText)}.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--buttonText);opacity:0}.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je:hover:before{opacity:.08}.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je:focus{outline:none}.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je:focus:before{opacity:.16}.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je._2dj14FxV-bfkwopj1jV_fF:before,.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je:active:before{opacity:.24}.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je:disabled,.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je[data-disabled],.cmR5BF4NpBUm3DBMZCmJS.ntawTzO-ZquMyaWgqE0je[disabled]{cursor:not-allowed;filter:grayscale(1);background-color:#ffa280;color:var(--newCommunityTheme-bodyAlpha50);fill:var(--newCommunityTheme-bodyAlpha50)}.cmR5BF4NpBUm3DBMZCmJS ._1V9TNuAloX-Z3moRIXc8tO,.cmR5BF4NpBUm3DBMZCmJS i.icon._1V9TNuAloX-Z3moRIXc8tO{display:inline-block;padding:0 8px 0 0;height:20px;width:20px;font-size:20px;line-height:20px}.cmR5BF4NpBUm3DBMZCmJS ._1V9TNuAloX-Z3moRIXc8tO.HjpiNF5rj_I6fiMfmW-X7,.cmR5BF4NpBUm3DBMZCmJS i.icon._1V9TNuAloX-Z3moRIXc8tO.HjpiNF5rj_I6fiMfmW-X7{float:left}.cmR5BF4NpBUm3DBMZCmJS ._1V9TNuAloX-Z3moRIXc8tO._1A_npZJAxjfyiijZ14jtzh,.cmR5BF4NpBUm3DBMZCmJS i.icon._1V9TNuAloX-Z3moRIXc8tO._1A_npZJAxjfyiijZ14jtzh{float:right}._2jNQT-6WbFOjX2hdDWV56w{background-color:var(--newCommunityTheme-field);opacity:1;color:var(--newRedditTheme-titleText);font-weight:700;padding:12px 20px}._2jNQT-6WbFOjX2hdDWV56w._2dj14FxV-bfkwopj1jV_fF:before{opacity:0}._2jNQT-6WbFOjX2hdDWV56w._1g3g98ViMb36cM-peU17Jk{background-color:transparent}._2jNQT-6WbFOjX2hdDWV56w:hover{background:linear-gradient(0deg,var(--newRedditTheme-menuButtonBackground-hover),var(--newRedditTheme-menuButtonBackground-hover)),var(--newCommunityTheme-field)}._2jNQT-6WbFOjX2hdDWV56w:disabled{background-color:transparent;opacity:.5}._2jNQT-6WbFOjX2hdDWV56w:active{background:linear-gradient(0deg,var(--newRedditTheme-menuButtonBackground-active),var(--newRedditTheme-menuButtonBackground-active)),var(--newCommunityTheme-field)}._2jNQT-6WbFOjX2hdDWV56w:active:before{opacity:0}
._21H_PIzpqfpibB_EcUDwpj{-ms-flex-align:center;align-items:center;margin-bottom:24px}._3XkfKrHLCXvnVsLyBJXzzv,._21H_PIzpqfpibB_EcUDwpj{display:-ms-flexbox;display:flex}._1gui9gwvmz0Ta6TaySS6jf{position:relative;margin-right:4px}._1nT46ChOZ3tgGqgs2CyMeJ{margin-left:auto}@media (max-width:960px){._10JrVcY3xBcUNO7dNh0Js2{display:none}}
.FIYolDqalszTnjjNfThfT{max-width:256px;white-space:normal;text-align:center}
._2ddpn_fVcA1SYZzLivK-SD{height:120px;width:100%}._2ymEyPXQM0ccuwfvIOMpnZ{padding:12px}._1vv6LrKIsjHuIJCCgIntnC{width:100%}._9jODC2-h7cM9Y6Duqs_W4{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:21px;margin-top:70px;text-align:center}._3lfTEmyI7x9ib1wz4e8RWP{background:var(--newCommunityTheme-body);border-radius:4px;box-sizing:border-box;color:var(--newCommunityTheme-bodyText);overflow:hidden;position:relative}._20axzOalQqYkHj-7Idfqun{height:126px;left:50%;position:absolute;top:57px;transform:translateX(-50%);width:70px}
._1FUNcfOeszr8eruqLxCMcR{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;height:100%}._1FUNcfOeszr8eruqLxCMcR>div:first-child{margin-top:0}
.DpriHZnFiOfa0afZpg8vf{background:var(--newCommunityTheme-post);border:thin solid var(--newCommunityTheme-postLine);border-radius:4px;box-shadow:0 2px 4px 0 rgba(0,0,0,.06);margin-bottom:16px;max-width:100%}._3n4VKjpr-iVnAmYcon-YbI{font-size:16px;line-height:20px;color:var(--newCommunityTheme-bodyText);padding:16px 16px 0}._3n4VKjpr-iVnAmYcon-YbI,._2tLIUcp3fYt74ZlVikNlz5{font-weight:500}._2tLIUcp3fYt74ZlVikNlz5{font-size:14px;line-height:18px;color:var(--newCommunityTheme-active);padding:16px}.YoadDFUejEmzEbJmjTvHn{color:var(--newCommunityTheme-bodyText);padding:16px}
.OGoNN0lGfOACQsVwIa1wo,._3yqn7UgWZCfM22Sk-rcBbs+._3yqn7UgWZCfM22Sk-rcBbs{margin-left:4px}.OGoNN0lGfOACQsVwIa1wo{vertical-align:middle}.OGoNN0lGfOACQsVwIa1wo._1ILOkGbdwmhXOmzBDCYXFT{transform:rotate(180deg)}.BZDMD8yWu5imupa73nqYE.BZDMD8yWu5imupa73nqYE{font-family:Noto Sans,Arial,sans-serif;font-size:12px;line-height:16px;font-weight:400;min-height:24px;height:24px;padding-left:12px;padding-right:8px}.BZDMD8yWu5imupa73nqYE.BZDMD8yWu5imupa73nqYE._1HyZhQLyitFqci_zC5jGCy{font-weight:700}._3RwR0q62tl_HktsM6eNnOn{margin-top:4px;border:initial;box-shadow:0 4px 12px hsla(0,0%,44.3%,.15)}
._iuAkxGWujgYETf2Xyv89{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:18px;min-width:120px;padding-left:12px;padding-right:12px;background-color:var(--newRedditTheme-post);border-color:var(--newRedditTheme-post)}._iuAkxGWujgYETf2Xyv89:hover{background:var(--newRedditTheme-buttonTinted20);border-color:var(--newRedditTheme-buttonTinted20);color:var(--newRedditTheme-postTinted20)}._iuAkxGWujgYETf2Xyv89:active{background:var(--newRedditTheme-button);color:var(--newRedditTheme-post)}._iuAkxGWujgYETf2Xyv89.hxyadGitKiIMfl81IVThw,._iuAkxGWujgYETf2Xyv89:active{border-color:var(--newRedditTheme-button)}
._3t6mNXBt6sQ7oZpTvfpI-D{padding:4px 16px}._3DJNcKXVcC9fp5NF4suS_j{margin-left:8px}
._3AmQ4JXJufVLUdOsC6v61i{display:-ms-flexbox;display:flex;margin-left:auto}._3AmQ4JXJufVLUdOsC6v61i+._3AmQ4JXJufVLUdOsC6v61i{margin-left:8px}.FGX7ywlMTix8BeUr5G7TE{height:10px;margin-left:4px;width:10px}._1fPZw9wLFaCEzhzp2Hkx18{background-color:var(--newCommunityTheme-body);height:46px;padding-left:16px;padding-right:16px;margin-bottom:8px;overflow:hidden}._1fPZw9wLFaCEzhzp2Hkx18:after,._1fPZw9wLFaCEzhzp2Hkx18:before{content:" ";display:table}._1fPZw9wLFaCEzhzp2Hkx18:after{clear:both}._26jxFFm8Z3TxPyZxoddAGy{margin-bottom:4px}
._1i7CStyaaHQU2aiG0GdpSA{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:18px;-ms-flex-align:center;align-items:center;background-color:var(--newRedditTheme-body);border-radius:4px;color:var(--newRedditTheme-titleText);display:-ms-flexbox;display:flex;height:42px;margin-bottom:12px;padding:0 16px}@media (max-width:640px){._1i7CStyaaHQU2aiG0GdpSA{border-bottom:1px solid var(--newRedditTheme-line);border-radius:0;margin-bottom:0}}._1i7CStyaaHQU2aiG0GdpSA._3-pePLWUAV_CAVhht1dfup{border-top:4px solid var(--newCommunityTheme-active);height:38px}._1i7CStyaaHQU2aiG0GdpSA._3Tphf4AA5J39saIlrB1SYD{background-color:transparent;border-bottom:none;border-top:none;height:auto;margin-bottom:0;padding:0 8px}._3swS56fqtrGcixPfTzK_Cl{height:20px;margin-left:4px;width:20px}.-V0kqUlRHvLoNRUAUmCy9{color:var(--newRedditTheme-linkText);display:inline;font-weight:700;margin-left:4px}.-V0kqUlRHvLoNRUAUmCy9._3-pePLWUAV_CAVhht1dfup{color:var(--newRedditTheme-titleText)}.icon.N0zmIZbfRSCGk2rUOGHSS{color:var(--newRedditTheme-linkText);margin-left:4px}.icon.N0zmIZbfRSCGk2rUOGHSS._3-pePLWUAV_CAVhht1dfup{color:var(--newRedditTheme-titleText)}
.eZLYleuk3b8ykGiskfpo3{max-width:1024px;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;margin:0 auto}._3Up38k81YNBWQoW1ovMU88{padding:24px 0 0;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;max-width:calc(100% - 48px);-ms-flex-positive:1;flex-grow:1}@media (min-width:640px){._3Up38k81YNBWQoW1ovMU88{padding:24px 24px 0}}._2lzCpzHH0OvyFsvuESLurr{display:-ms-flexbox;display:flex;padding-top:8px}._2lzCpzHH0OvyFsvuESLurr,._1BJGsKulUQfhJyO19XsBph{width:100%;max-width:100%}@media (min-width:960px){._1BJGsKulUQfhJyO19XsBph._3SktesklDBwXt2pEl0sHY8{-ms-flex:1 1 640px;flex:1 1 640px;max-width:640px}}._2iRJ8DI-3RTbsXRSDXE5ZG{display:none}@media (min-width:960px){._2iRJ8DI-3RTbsXRSDXE5ZG{display:block;-ms-flex:0 0 312px;flex:0 0 312px;margin-left:24px;max-width:312px}}
._13NhOjx-Siom7MKe3Dex5y{fill:var(--newCommunityTheme-actionIcon)}
._2n96dzZYei5koZIof4hNGb{background-color:var(--newCommunityTheme-body);border-radius:4px;border:1px solid var(--newCommunityTheme-postLine);display:block;margin-bottom:12px;padding:16px}._2_60e51mes8qIV48MFyxwe{font-size:18px;font-weight:500;line-height:22px;color:#0079d3;margin:4px 0;text-transform:uppercase}._1ADicmI89099yV3e3zrjUD{font-size:12px;font-weight:400;line-height:16px;color:var(--newCommunityTheme-metaText);padding:8px 0 16px}._1vGOSBVzbAH3jn-PrQ2qY5{display:inline-block}._1KlaD5sga3um3ZmSli7uwr{cursor:pointer;fill:var(--newCommunityTheme-metaText);height:16px;margin:0 0 0 auto;width:16px}._1vyFrq5zn33vVTIC_LlCmR{fill:#0079d3;height:20px;padding-right:8px;width:20px}
._1hUjYWB4NLdPs1k_qx-f0u{margin-bottom:24px}._1hUjYWB4NLdPs1k_qx-f0u a[role=button]{display:inline}
._35ky2Wm3TP6kFdIh-DOxmA{width:inherit}._79QamRjUfUQIFHxCnTvSZ{margin-top:24px}@media (min-width:calc(960px + 1px)){._79QamRjUfUQIFHxCnTvSZ{display:none}}
._1VDJFxZ-XJSB8yo1UyJzsi{-ms-flex-align:center;align-items:center;background:var(--newRedditTheme-post);border:thin solid var(--newRedditTheme-postLine);border-radius:4px;box-sizing:border-box;color:var(--newRedditTheme-bodyText);display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;-ms-flex-pack:justify;justify-content:space-between;padding:24px 16px;text-align:center}@media (min-width:640px){._1VDJFxZ-XJSB8yo1UyJzsi{width:calc(100vw - 48px)}}@media (min-width:960px){._1VDJFxZ-XJSB8yo1UyJzsi{max-width:100%}._1VDJFxZ-XJSB8yo1UyJzsi._3C2YoevK_DDUuAyafjSuUs{width:auto}}.kKE_PXkpQNWEX-RiwWuTA{font-size:20px;font-weight:500;line-height:24px;padding:16px 0}._1tEoY-vmgG3yWH6hCdgy3p{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:18px;color:var(--newRedditTheme-metaText)}.e6PSfRI3_H3v8fgbIqj-x{width:134px;height:126px}._3FKXXAcRW_DvCNr6yMbF73{color:var(--newCommunityTheme-linkText)}._3FKXXAcRW_DvCNr6yMbF73:hover{text-decoration:underline}._2LEtmNuEePPvFdDfwPmBcx{padding:0 48px 40px}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/CollectionCommentsPage~SearchResults.34071d8a7f9938b08a4f_.css.map*/</style><style class="" data-href="chunkCSS/SearchResults.689e8a5b9b9e375db180_.css">._1oQyIsiPHYt6nx7VOmd1sz:focus{outline:none}
._2A5FemPDmjHjEjpCkaUK2h{color:var(--newCommunityTheme-actionIcon);border-top:1px solid var(--newCommunityTheme-line)}.nGJGslkMB0gn9S2lxUphf.nGJGslkMB0gn9S2lxUphf{border-top:none;color:var(--newRedditTheme-bodyText)}.SnpDpl5eEAD07JaiyJbpr{height:12px;margin-top:-6px;padding-right:4px;vertical-align:middle;width:12px}
._3IEDcFIIs_TeXsZtKZGzUd{font-size:12px;font-weight:400;line-height:16px;background:transparent;border-radius:0;color:#ff585b;cursor:pointer;margin:0;padding:0;vertical-align:middle}._3IEDcFIIs_TeXsZtKZGzUd:focus{outline:none}.smOzqVIOoNqmSJcyBX2N6{margin-left:4px;padding-right:2px;vertical-align:middle;white-space:pre-wrap;text-align:left;line-height:12px}._1rNBkuuOkN2SorEXyRkYjB{border-radius:2px;-ms-flex-align:center;align-items:center;border:none;display:-ms-flexbox;display:flex;margin:4px 8px 4px 0;padding:4px;text-decoration:none;text-transform:capitalize}._1rNBkuuOkN2SorEXyRkYjB:focus,._1rNBkuuOkN2SorEXyRkYjB:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}._1rNBkuuOkN2SorEXyRkYjB:disabled{opacity:.5}._1rNBkuuOkN2SorEXyRkYjB:focus:disabled,._1rNBkuuOkN2SorEXyRkYjB:hover:disabled{background-color:transparent}._2T9IigN7CfZvuc5KSKs2hx:disabled{color:#46d160;fill:#46d160}._2OvUr_pd3kddsNP_f35S28:disabled{color:#ff585b;fill:#ff585b}
._1HjNIJegwQhOyUoxHZNWnm{display:inline-block;margin:0;white-space:nowrap}.YoaDbMbI8PpFFWQbD_Uwq{width:16px}.YoaDbMbI8PpFFWQbD_Uwq path{width:24px;fill:grey}._3cJNzWW-kTTUFiqoBkRMRk{font-size:12px;font-weight:700;line-height:16px;display:-ms-flexbox;display:flex}
._28noJDp6DzFWESejYQdpcD{display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center}
.ehsOqYO6dxn_Pf9Dzwu37{margin-top:0;overflow:visible}._2pFdCpgBihIaYh9DSMWBIu{height:24px}._2pFdCpgBihIaYh9DSMWBIu.uMPgOFYlCc5uvpa2Lbteu{border-radius:2px}._2pFdCpgBihIaYh9DSMWBIu.uMPgOFYlCc5uvpa2Lbteu:focus,._2pFdCpgBihIaYh9DSMWBIu.uMPgOFYlCc5uvpa2Lbteu:hover{background-color:var(--newRedditTheme-navIconFaded10);outline:none}._38GxRFSqSC-Z2VLi5Xzkjy{color:var(--newCommunityTheme-actionIcon)}._2DO72U0b_6CUw3msKGrnnT{border-top:none;color:var(--newCommunityTheme-metaText);cursor:pointer;padding:8px 16px 8px 8px;text-transform:none}._2DO72U0b_6CUw3msKGrnnT:hover{background-color:#0079d3;border:none;color:var(--newCommunityTheme-body);fill:var(--newCommunityTheme-body)}
.PWY92ySDjTYrTAiutq4ty{margin-top:0}._2snJGyyGyyH38duHobOUKE{border-top:none;color:var(--newCommunityTheme-metaText);padding:8px 16px 8px 8px}._1GObrri0j7y_9IWiGUfPjp{font-size:14px}._1PhtucoKocd-ADJ-JDEoiC,._1m76BHzDzRsM1te7HBxUqd{font-size:12px}._3MSdPVJwGxrpakz-e1MQhO{font-size:14px}.T4VmKX-IOkP4UG-B4jUR-{box-shadow:none;z-index:55}
._3YRHtGWABKh4OVO3s5gJwt{-ms-flex:0 0;flex:0 0;margin-right:0}._1IPWlMFPB_zPPajVPKk5Dy{-ms-flex:1 1 100%;flex:1 1 100%;overflow:hidden;width:100%}._2CUZHyZpRYmdvLE9tOI-2L{display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row}
.icon._3Ebr0mkLD0A7HiowzExNW-{margin-right:10px;vertical-align:middle}._2eawLPCtwzvTZhWKtaUgZQ{font-size:14px;font-weight:500;line-height:18px;background-color:var(--newCommunityTheme-body);box-sizing:border-box;color:var(--newCommunityTheme-bodyText);fill:#0079d3;height:40px;padding:10px 8px;width:100%}._2eawLPCtwzvTZhWKtaUgZQ:hover{color:var(--newCommunityTheme-body);background-color:#0079d3;fill:var(--newCommunityTheme-body)}._2eawLPCtwzvTZhWKtaUgZQ ._34Odk7t6y-rCPxPcYJa4Nw{-ms-flex-align:center;align-items:center}._3LyKu57c-QkPvlFvAgWop5{cursor:pointer;color:var(--newCommunityTheme-actionIcon);text-transform:capitalize;background-color:var(--newCommunityTheme-body);border-top:1px solid var(--newCommunityTheme-line);display:block;white-space:nowrap}._3LyKu57c-QkPvlFvAgWop5:hover{background-color:var(--newRedditTheme-highlight);border-color:var(--newRedditTheme-line);color:var(--newRedditTheme-bodyText)}
._2j4blQAaYrPKIhe5jBJ9c8{display:inline-block;vertical-align:text-bottom;width:16px;height:16px;line-height:16px}
._3FJq-cq7boH_EAWZsUPWY0{font-family:Noto Sans,Arial,sans-serif;font-size:12px;font-weight:400;line-height:18px;padding:.5em .75em;border-radius:4px;color:var(--newRedditTheme-bodyText)}._3FJq-cq7boH_EAWZsUPWY0 ._1QOFlf2Sv2RU3pPqUKD6UD{font-size:.95em;height:auto;width:auto;line-height:1;margin-right:.5em}._14wV0QXuPq6IJL_pdl8sQs{background-color:var(--newCommunityTheme-inactive)}
._2AfJEqW9tv4b_kolKEuS9K{background-color:var(--newCommunityTheme-body);border-radius:4px;box-sizing:border-box;color:var(--newCommunityTheme-bodyText);width:350px}.p4QfstubN5cRxd-gy8gFH{font-size:16px;font-weight:500;line-height:20px;padding:11px 16px;border-bottom:1px solid var(--newCommunityTheme-line)}._2V3KEAhexNh-mP3TbrVClC{font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:400;line-height:21px;max-height:50vh;overflow-wrap:break-word;overflow:auto;padding:16px}._1fcbQFwN65ik28DNmWnpX4{background:var(--newCommunityTheme-line);-ms-flex-direction:row-reverse;flex-direction:row-reverse;padding:8px 5px}.zcMEJWBL7q-mYGOPSpjN-{margin-left:5px}
._2hGJP-9xfXBXd0wqhBLHhY{font-size:12px;font-weight:400;line-height:16px;color:red;padding-top:4px;text-align:right;display:-ms-flexbox;display:flex}._3h_9YwxjuOr77VhScPrjCI{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}._1Y0BrhDgcSTeSYvmSPYepI{text-decoration:underline;cursor:pointer;padding-left:4px}
._3rtq7SfSLd-e5fAEgn373L{color:var(--newCommunityTheme-metaText)}._3rtq7SfSLd-e5fAEgn373L>i{color:var(--newCommunityTheme-button)}._1j5EnaNrX7PuyCnmpT-8o0{color:var(--newCommunityTheme-metaText)}.BGfronFwr_0rXxOJmxp10{color:#ff4500}._3NIcD2Vr2xrSAq08U14kCy{font-size:12px;font-weight:400;line-height:16px;-ms-flex-align:center;align-items:center;display:-ms-inline-flexbox;display:inline-flex;vertical-align:middle}.LEz3F0HfvMpdo96occzKU,._3ArSA7Spw15WyF9ld4p6ZJ{font-size:16px;line-height:16px;margin-right:4px}._27_KVVxYHZ7v44CE2vg8bT{display:inline-block;height:12px;vertical-align:middle;width:60px}
._1yF34mDRcD_ii0n-Ak0OdI{background-color:var(--newCommunityTheme-widgetColors-sidebarWidgetTitleColor);border-radius:4px;border:1px solid var(--newCommunityTheme-widgetColors-sidebarWidgetTitleColor);box-sizing:border-box;color:var(--newCommunityTheme-widgetColors-sidebarWidgetHeaderColor);margin:0 10px 0 16px;max-width:92px;overflow:hidden;padding:4px 14px;text-transform:uppercase;white-space:nowrap;font-size:12px;font-weight:400;line-height:16px;font-weight:700}._1yF34mDRcD_ii0n-Ak0OdI:focus,._1yF34mDRcD_ii0n-Ak0OdI:hover{outline:none}._1yF34mDRcD_ii0n-Ak0OdI.gBrTiaH_Z7HT5D96vnUfJ{background-color:var(--newCommunityTheme-widgetColors-sidebarWidgetHeaderColor);border:1px solid var(--newCommunityTheme-widgetColors-sidebarWidgetTitleColor);color:var(--newCommunityTheme-widgetColors-sidebarWidgetTitleColor)}._1yF34mDRcD_ii0n-Ak0OdI.gBrTiaH_Z7HT5D96vnUfJ._1iTFEDTdpF-KFmOZvDuGHH{background-color:var(--newCommunityTheme-body);border:1px solid var(--newCommunityTheme-button);color:var(--newCommunityTheme-button)}._1yF34mDRcD_ii0n-Ak0OdI._1iTFEDTdpF-KFmOZvDuGHH{background-color:var(--newCommunityTheme-button);border:1px solid var(--newCommunityTheme-body);color:var(--newCommunityTheme-body)}
._2A1Ng1fBxjU-qYqbEJn_sm{margin:0 8px 8px}._55hUWVhbF34AzbWr7SAMi{-ms-flex-align:center;align-items:center;border-bottom:1px solid var(--newCommunityTheme-line);box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-flow:row wrap;flex-flow:row wrap;height:40px;-ms-flex-pack:justify;justify-content:space-between;width:100%}._55hUWVhbF34AzbWr7SAMi ._2XCKBYzBTZpjOAFEWv1tSy{margin:0}._2gNxoOe_xKaMk0mmYMQCGs{margin:0 3px 3px 10px}._2gNxoOe_xKaMk0mmYMQCGs ._55hUWVhbF34AzbWr7SAMi{height:30px}
.LniF5nGHFXZ6i7_mQiEaT{display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between;-ms-flex-align:center;align-items:center;background-color:var(--newCommunityTheme-field);min-height:48px;position:relative}.LniF5nGHFXZ6i7_mQiEaT._3JgLF82C_0NM3uN8pOyJTu{border-radius:0;background:none}.LniF5nGHFXZ6i7_mQiEaT._3JgLF82C_0NM3uN8pOyJTu._3LUqJuEsn44ivYFDMegLQG{border-bottom:1px solid var(--newCommunityTheme-flair)}.LniF5nGHFXZ6i7_mQiEaT._3JgLF82C_0NM3uN8pOyJTu._3LUqJuEsn44ivYFDMegLQG,.LniF5nGHFXZ6i7_mQiEaT._3JgLF82C_0NM3uN8pOyJTu._2n1stnecLcYB2e1RjBwSq_{border-top:1px solid var(--newCommunityTheme-flair)}.LniF5nGHFXZ6i7_mQiEaT._3JgLF82C_0NM3uN8pOyJTu._2EVJbBkxJortsXpkuVWaPA{border-bottom:1px solid var(--newCommunityTheme-flair)}
._2pjSQOdNtYd1I2W0Z1Im8I{background-color:transparent;margin:4px 8px;white-space:nowrap;-ms-flex-negative:0;flex-shrink:0}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_){font-size:12px;letter-spacing:.5px;line-height:24px;text-transform:uppercase;border:1px solid transparent;border-radius:4px;letter-spacing:1px;text-decoration:none;-ms-flex-align:center;align-items:center;border-radius:9999px;box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;text-align:center;width:auto;font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:unset;line-height:17px;text-transform:unset;min-height:32px;min-width:32px;padding:4px 16px;position:relative;border:1px solid var(--newCommunityTheme-button);color:var(--newCommunityTheme-button);fill:var(--newCommunityTheme-button)}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_) ._2W1YFyYH_CTGX4_5OEBs2Q,._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_) i.icon._2W1YFyYH_CTGX4_5OEBs2Q{display:inline-block;padding:0 8px 0 0;height:20px;width:20px;font-size:20px;line-height:20px}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_) ._2W1YFyYH_CTGX4_5OEBs2Q.p8bIdnQ5pQUQRETAyCoa5,._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_) i.icon._2W1YFyYH_CTGX4_5OEBs2Q.p8bIdnQ5pQUQRETAyCoa5{float:left}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_) ._2W1YFyYH_CTGX4_5OEBs2Q._36ucS75syCWwJ_ee7IieXZ,._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_) i.icon._2W1YFyYH_CTGX4_5OEBs2Q._36ucS75syCWwJ_ee7IieXZ{float:right}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_):before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newCommunityTheme-button);opacity:0}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_):hover:before{opacity:.04}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_):focus{outline:none}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_):focus:before{opacity:.08}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).NPw0Z_HL-yJPXnZ3mpWEA:before,._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_):active:before{opacity:.16}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_):disabled,._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)[data-disabled],._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)[disabled]{cursor:not-allowed;filter:grayscale(1);border-color:var(--newCommunityTheme-buttonAlpha50);color:var(--newCommunityTheme-buttonAlpha50);fill:var(--newCommunityTheme-buttonAlpha50)}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO{position:relative;border:1px solid var(--newRedditTheme-button);color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-button);opacity:0}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO:hover:before{opacity:.04}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO:focus{outline:none}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO:focus:before{opacity:.08}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO.NPw0Z_HL-yJPXnZ3mpWEA:before,._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO:active:before{opacity:.16}._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO:disabled,._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO[data-disabled],._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_).OGOshepc50ul-kJHrocIO[disabled]{cursor:not-allowed;filter:grayscale(1);border-color:var(--newRedditTheme-buttonAlpha50);color:var(--newRedditTheme-buttonAlpha50);fill:var(--newRedditTheme-buttonAlpha50)}.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD{--newRedditTheme-button:#0f1a1c;position:relative;background-color:var(--newCommunityTheme-field);border:1px solid transparent;color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-button);opacity:0}.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:hover:before{opacity:.08}.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:focus{outline:none}.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:focus:before{opacity:.16}.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD.NPw0Z_HL-yJPXnZ3mpWEA:before,.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:active:before{opacity:.24}.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:disabled,.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD[data-disabled],.theme-light ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD[disabled]{cursor:not-allowed;filter:grayscale(1);background:none;color:var(--newRedditTheme-buttonAlpha50);fill:var(--newRedditTheme-buttonAlpha50)}.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD{--newRedditTheme-button:#0f1a1c;position:relative;background-color:var(--newCommunityTheme-button);border:1px solid transparent;color:var(--newRedditTheme-button);fill:var(--newRedditTheme-button)}.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-button);opacity:0}.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:hover:before{opacity:.08}.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:focus{outline:none}.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:focus:before{opacity:.16}.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD.NPw0Z_HL-yJPXnZ3mpWEA:before,.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:active:before{opacity:.24}.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD:disabled,.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD[data-disabled],.theme-dark ._2pjSQOdNtYd1I2W0Z1Im8I:not(.O3tUaKrd54EXILNilEqF_)._2sQjgE-zw2MQovQiJwdvVD[disabled]{cursor:not-allowed;filter:grayscale(1);background:none;color:var(--newRedditTheme-buttonAlpha50);fill:var(--newRedditTheme-buttonAlpha50)}._2pjSQOdNtYd1I2W0Z1Im8I:hover{text-decoration:none}._2pjSQOdNtYd1I2W0Z1Im8I._33VrFkg3gJpkL8AlPfcHUE{height:27px}._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_{-ms-flex-align:center;align-items:center;border-radius:9999px;box-sizing:border-box;display:-ms-flexbox;display:flex;-ms-flex-pack:center;justify-content:center;text-align:center;width:auto;font-family:Noto Sans,Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:unset;line-height:17px;text-transform:unset;min-height:32px;min-width:32px;padding:4px 16px;background-color:var(--newRedditTheme-flair);color:var(--newRedditTheme-bodyText);position:relative}._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_ ._2W1YFyYH_CTGX4_5OEBs2Q,._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_ i.icon._2W1YFyYH_CTGX4_5OEBs2Q{display:inline-block;padding:0 8px 0 0;height:20px;width:20px;font-size:20px;line-height:20px}._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_ ._2W1YFyYH_CTGX4_5OEBs2Q.p8bIdnQ5pQUQRETAyCoa5,._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_ i.icon._2W1YFyYH_CTGX4_5OEBs2Q.p8bIdnQ5pQUQRETAyCoa5{float:left}._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_ ._2W1YFyYH_CTGX4_5OEBs2Q._36ucS75syCWwJ_ee7IieXZ,._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_ i.icon._2W1YFyYH_CTGX4_5OEBs2Q._36ucS75syCWwJ_ee7IieXZ{float:right}._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;border-radius:9999px;background:var(--newRedditTheme-bodyText);opacity:0}._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_:hover:before{opacity:.08}._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_:focus{outline:none}._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_:focus:before{opacity:.16}._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_.NPw0Z_HL-yJPXnZ3mpWEA:before,._2pjSQOdNtYd1I2W0Z1Im8I.O3tUaKrd54EXILNilEqF_:active:before{opacity:.24}

/*# sourceMappingURL=https://www.redditstatic.com/desktop2x/chunkCSS/SearchResults.689e8a5b9b9e375db180_.css.map*/</style><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/ShortcutWrapper.890ced71e0ce5e711fad.js"></script><link rel="stylesheet" type="text/css" href="https://www.redditstatic.com/desktop2x/chunkCSS/BottomSheetUpsellWrapper.45e905d89131597b00ee_.css"><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/BottomSheetUpsellWrapper.b7e4e0f2aa81bc1e76a9.js"></script><link rel="stylesheet" type="text/css" href="https://www.redditstatic.com/desktop2x/chunkCSS/BottomCellWrapper.61d5a3a7c68a3068b2c4_.css"><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/BottomCellWrapper.b9310f2cc0442873701d.js"></script><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/webvitals.f626f135e0d2366368b7.js"></script><link rel="stylesheet" type="text/css" href="https://www.redditstatic.com/desktop2x/chunkCSS/EmailVerificationModals.5428cd864a6fbd694c2b_.css"><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/EmailVerificationModals.27977d9808b12fc1a571.js"></script><link rel="stylesheet" type="text/css" href="https://www.redditstatic.com/desktop2x/chunkCSS/SubredditHovercard.5ab6e2179408710d3b9a_.css"><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/SubredditHovercard.d12783c89d74426a0843.js"></script><link rel="stylesheet" type="text/css" href="https://www.redditstatic.com/desktop2x/chunkCSS/AuthorHovercard.4710a5224ab146323625_.css"><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/AuthorHovercard.c2f293230200f6ef9097.js"></script><link rel="stylesheet" type="text/css" href="https://www.redditstatic.com/desktop2x/chunkCSS/CountryPage~Frontpage~ModListing~Multireddit~ProfileComments~ProfileOverview~ProfilePosts~Subreddit.e72fce90a7f3165091b9_.css"><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/CountryPage~Frontpage~ModListing~Multireddit~ProfileComments~ProfileOverview~ProfilePosts~Subreddit.74516b7060044f67e198.js"></script><link rel="stylesheet" type="text/css" href="https://www.redditstatic.com/desktop2x/chunkCSS/CountryPage~Multireddit~reddit-components-AdHocMultiredditSidebar.6f4f9d16e46e81610dd5_.css"><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/CountryPage~Multireddit~reddit-components-AdHocMultiredditSidebar.d46f31114cb24b1ec840.js"></script><link rel="stylesheet" type="text/css" href="https://www.redditstatic.com/desktop2x/chunkCSS/CountryPage~Multireddit.5b4859e7fe033befa5ae_.css"><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/CountryPage~Multireddit.db47526d23740ec3540e.js"></script><link rel="stylesheet" type="text/css" href="https://www.redditstatic.com/desktop2x/chunkCSS/Multireddit.6bedea13e6c6fc3d563a_.css"><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/Multireddit.126c07025cf61eb4c585.js"></script><script charset="utf-8" src="https://www.redditstatic.com/desktop2x/PushNotifications.ec99e90146e634d877ee.js"></script></head>
  
    <body>
      <script>__perfMark('app_html_start');</script>
      <div id="2x-container"><div class="_1VP69d9lk-Wk9zokOaylL  theme-beta" style="--background:#FFFFFF;--canvas:#DAE0E6"><div tabindex="-1"></div><div class="hciOr5UGrnYrZxB11tX9s" id="SHORTCUT_FOCUSABLE_DIV" tabindex="-1"><style>:root { --newCommunityTheme-actionIcon: #878A8C;--newCommunityTheme-actionIconAlpha20: rgba(135,138,140,0.2);--newCommunityTheme-actionIconAlpha50: rgba(135,138,140,0.5);--newCommunityTheme-actionIconShaded80: #6c6e70;--newCommunityTheme-actionIconTinted80: #9fa1a3;--newCommunityTheme-active: #0079D3;--newCommunityTheme-activeAlpha10: rgba(0,121,211,0.1);--newCommunityTheme-activeAlpha20: rgba(0,121,211,0.2);--newCommunityTheme-activeAlpha50: rgba(0,121,211,0.5);--newCommunityTheme-activeLight60: #33a8ff;--newCommunityTheme-activeShaded80: #0060a8;--newCommunityTheme-activeShaded90: #006cbd;--newCommunityTheme-activeTinted05: #f2f8fc;--newCommunityTheme-backgroundImage: initial;--newCommunityTheme-backgroundImagePosition: cover;--newCommunityTheme-banner-backgroundColor: #33a8ff;--newCommunityTheme-banner-backgroundImage: initial;--newCommunityTheme-banner-backgroundImagePosition: cover;--newCommunityTheme-banner-communityNameFormat: slashtag;--newCommunityTheme-banner-height: 64;--newCommunityTheme-banner-iconColor: #0079D3;--newCommunityTheme-banner-iconDimensions-borderRadius: 24;--newCommunityTheme-banner-iconDimensions-customSize: 32;--newCommunityTheme-banner-iconDimensions-padding: 6;--newCommunityTheme-banner-iconDimensions-size: 24;--newCommunityTheme-banner-iconImage: initial;--newCommunityTheme-banner-lineHeight: 38;--newCommunityTheme-banner-positionedImage: initial;--newCommunityTheme-banner-positionedImageAlignment: left;--newCommunityTheme-banner-positionedImageHeight: 48;--newCommunityTheme-banner-secondaryBannerPositionedImage: initial;--newCommunityTheme-body: #FFFFFF;--newCommunityTheme-bodyAlpha50: rgba(255,255,255,0.5);--newCommunityTheme-bodyAlpha70: rgba(255,255,255,0.7);--newCommunityTheme-bodyAlpha80: rgba(255,255,255,0.8);--newCommunityTheme-bodyFade: #FFFFFF00;--newCommunityTheme-bodyShaded80: #ccc;--newCommunityTheme-bodyText: #1c1c1c;--newCommunityTheme-bodyTextAlpha03: rgba(28,28,28,0.03);--newCommunityTheme-bodyTextAlpha20: rgba(28,28,28,0.2);--newCommunityTheme-bodyTextShaded20: #050505;--newCommunityTheme-bodyTextTinted20: #d1d1d1;--newCommunityTheme-bodyTinted50: #fff;--newCommunityTheme-bodyTinted80: #fff;--newCommunityTheme-button: #0079D3;--newCommunityTheme-buttonAlpha05: rgba(0,121,211,0.05);--newCommunityTheme-buttonAlpha10: rgba(0,121,211,0.1);--newCommunityTheme-buttonAlpha20: rgba(0,121,211,0.2);--newCommunityTheme-buttonAlpha40: rgba(0,121,211,0.4);--newCommunityTheme-buttonAlpha50: rgba(0,121,211,0.5);--newCommunityTheme-buttonAlpha80: rgba(0,121,211,0.8);--newCommunityTheme-buttonShaded80: #0060a8;--newCommunityTheme-buttonTinted20: #cce4f6;--newCommunityTheme-buttonTinted50: #7fbce9;--newCommunityTheme-buttonTinted80: #3293db;--newCommunityTheme-canvas: #DAE0E6;--newCommunityTheme-canvasImgPosition: cover;--newCommunityTheme-canvasImgUrl: initial;--newCommunityTheme-checkbox: #000000;--newCommunityTheme-errorText: #FF0000;--newCommunityTheme-field: #F6F7F8;--newCommunityTheme-fieldFade: #F6F7F800;--newCommunityTheme-flair: #EDEFF1;--newCommunityTheme-highlight: #e5f1fa;--newCommunityTheme-inactive: #EDEFF1;--newCommunityTheme-invertFilter: invert(0);--newCommunityTheme-lightText: #FFFFFF;--newCommunityTheme-lightTextAlpha75: rgba(255,255,255,0.75);--newCommunityTheme-line: #EDEFF1;--newCommunityTheme-lineShaded80: #bdbfc0;--newCommunityTheme-lineShaded90: #d5d7d8;--newCommunityTheme-lineShadedNinety: #d5d7d8;--newCommunityTheme-linkText: #0079D3;--newCommunityTheme-linkTextAlpha80: rgba(0,121,211,0.5);--newCommunityTheme-linkTextShaded80: #0060a8;--newCommunityTheme-linkTextTinted80: #3293db;--newCommunityTheme-linkTextWithBody: #3f9ade;--newCommunityTheme-menu: #FFFFFF;--newCommunityTheme-menuActiveText: #0079D3;--newCommunityTheme-menuButtonBackground-active: rgba(0,0,0,0.08);--newCommunityTheme-menuButtonBackground-focus: rgba(0,0,0,0.12);--newCommunityTheme-menuButtonBackground-hover: rgba(0,0,0,0.04);--newCommunityTheme-menuInactiveText: #0079D3;--newCommunityTheme-metaText: #7c7c7c;--newCommunityTheme-monospaceColor: #FF006D;--newCommunityTheme-navBar-activeLink: #0079D3;--newCommunityTheme-navBar-activeSubmenuCaret: #0079D3;--newCommunityTheme-navBar-activeSubmenuLink: #0079D3;--newCommunityTheme-navBar-backgroundColor: #dbf0ff;--newCommunityTheme-navBar-backgroundImage: initial;--newCommunityTheme-navBar-hoverLink: #0079D3;--newCommunityTheme-navBar-inactiveLink: #0079D3;--newCommunityTheme-navBar-inactiveSubmenuCaret: #33a8ff;--newCommunityTheme-navBar-inactiveSubmenuLink: #33a8ff;--newCommunityTheme-navBar-submenuBackgroundColor: #dbf0ff;--newCommunityTheme-navIcon: #1A1A1B;--newCommunityTheme-navIconFaded10: rgba(26,26,27,0.1);--newCommunityTheme-nsfwBlocking-bgcolor: #edeff1;--newCommunityTheme-nsfwBlocking-color: #030303;--newCommunityTheme-nsfwBlocking-contentTitleBgColor: #f6f7f8;;--newCommunityTheme-nsfwBlocking-mainCtaBgColor: #fff;--newCommunityTheme-orangeRed: #FF4500;--newCommunityTheme-pageHeader: #0079D3;--newCommunityTheme-placeholder: #d6d6d6;--newCommunityTheme-placeholderImage: initial;--newCommunityTheme-placeholderImagePosition: cover;--newCommunityTheme-post: #FFFFFF;--newCommunityTheme-postError: #ffe5e5;--newCommunityTheme-postFlairText: #1A1A1B;--newCommunityTheme-postIcon: #898989;--newCommunityTheme-postLine: #ccc;--newCommunityTheme-postLineShaded80: #a3a3a3;--newCommunityTheme-postLineShaded90: #b7b7b7;--newCommunityTheme-postTinted20: #fff;--newCommunityTheme-postTransparent20: rgba(255,255,255,0.8);--newCommunityTheme-primaryButtonShadedEighty: #0060a8;--newCommunityTheme-primaryButtonTintedEighty: #3293db;--newCommunityTheme-primaryButtonTintedFifty: #7fbce9;--newCommunityTheme-primaryButtonTintedSixty: #66aee4;--newCommunityTheme-report: #fff7e5;--newCommunityTheme-textTransparentizedEighty: rgba(26,26,27,0.2);--newCommunityTheme-titleText: #222222;--newCommunityTheme-voteIcons-downvoteActive: initial;--newCommunityTheme-voteIcons-downvoteInactive: initial;--newCommunityTheme-voteIcons-upvoteActive: initial;--newCommunityTheme-voteIcons-upvoteInactive: initial;--newCommunityTheme-voteText-base: #898989;--newCommunityTheme-voteText-downvote: #7193FF;--newCommunityTheme-voteText-downvoteShaded80: #5a75cc;--newCommunityTheme-voteText-downvoteTinted80: #8da8ff;--newCommunityTheme-voteText-upvote: #FF4500;--newCommunityTheme-voteText-upvoteShaded80: #cc3700;--newCommunityTheme-voteText-upvoteTinted80: #ff6a32;--newCommunityTheme-widgetColors-lineColor: rgba(26,26,27,0.07);--newCommunityTheme-widgetColors-sidebarWidgetBackgroundColor: #FFFFFF;--newCommunityTheme-widgetColors-sidebarWidgetBorderColor: #ccc;--newCommunityTheme-widgetColors-sidebarWidgetHeaderColor: #FFFFFF;--newCommunityTheme-widgetColors-sidebarWidgetHeaderColorAlpha60: rgba(255,255,255,0.6);--newCommunityTheme-widgetColors-sidebarWidgetTextColor: #1A1A1B;--newCommunityTheme-widgetColors-sidebarWidgetTextColorShaded80: #141415;--newCommunityTheme-widgetColors-sidebarWidgetTitleColor: #1A1A1B;--newRedditTheme-actionIcon: #878A8C;--newRedditTheme-actionIconAlpha20: rgba(135,138,140,0.2);--newRedditTheme-actionIconAlpha50: rgba(135,138,140,0.5);--newRedditTheme-actionIconShaded80: #6c6e70;--newRedditTheme-actionIconTinted80: #9fa1a3;--newRedditTheme-active: #24A0ED;--newRedditTheme-activeAlpha10: rgba(36,160,237,0.1);--newRedditTheme-activeAlpha20: rgba(36,160,237,0.2);--newRedditTheme-activeAlpha50: rgba(36,160,237,0.5);--newRedditTheme-activeLight60: #42adf0;--newRedditTheme-activeShaded80: #1c80bd;--newRedditTheme-activeShaded90: #2090d5;--newRedditTheme-activeTinted05: #f4fafe;--newRedditTheme-banner-backgroundColor: #24A0ED;--newRedditTheme-banner-backgroundImage: initial;--newRedditTheme-banner-backgroundImagePosition: cover;--newRedditTheme-banner-communityNameFormat: slashtag;--newRedditTheme-banner-height: 64;--newRedditTheme-banner-iconColor: #24A0ED;--newRedditTheme-banner-iconDimensions-borderRadius: 24;--newRedditTheme-banner-iconDimensions-customSize: 32;--newRedditTheme-banner-iconDimensions-padding: 6;--newRedditTheme-banner-iconDimensions-size: 24;--newRedditTheme-banner-iconImage: initial;--newRedditTheme-banner-lineHeight: 38;--newRedditTheme-banner-positionedImage: initial;--newRedditTheme-banner-positionedImageAlignment: cover;--newRedditTheme-banner-positionedImageHeight: 48;--newRedditTheme-banner-secondaryBannerPositionedImage: initial;--newRedditTheme-body: #FFFFFF;--newRedditTheme-bodyAlpha50: rgba(255,255,255,0.5);--newRedditTheme-bodyAlpha70: rgba(255,255,255,0.7);--newRedditTheme-bodyAlpha80: rgba(255,255,255,0.8);--newRedditTheme-bodyFade: #FFFFFF00;--newRedditTheme-bodyShaded80: #ccc;--newRedditTheme-bodyText: #1c1c1c;--newRedditTheme-bodyTextAlpha03: rgba(28,28,28,0.03);--newRedditTheme-bodyTextAlpha20: rgba(28,28,28,0.2);--newRedditTheme-bodyTextShaded20: #050505;--newRedditTheme-bodyTextTinted20: #d1d1d1;--newRedditTheme-bodyTinted50: #fff;--newRedditTheme-bodyTinted80: #fff;--newRedditTheme-button: #0079D3;--newRedditTheme-buttonAlpha05: rgba(0,121,211,0.05);--newRedditTheme-buttonAlpha10: rgba(0,121,211,0.1);--newRedditTheme-buttonAlpha20: rgba(0,121,211,0.2);--newRedditTheme-buttonAlpha40: rgba(0,121,211,0.4);--newRedditTheme-buttonAlpha50: rgba(0,121,211,0.5);--newRedditTheme-buttonAlpha80: rgba(0,121,211,0.8);--newRedditTheme-buttonShaded80: #0060a8;--newRedditTheme-buttonTinted20: #cce4f6;--newRedditTheme-buttonTinted50: #7fbce9;--newRedditTheme-buttonTinted80: #3293db;--newRedditTheme-canvas: #DAE0E6;--newRedditTheme-checkbox: #000000;--newRedditTheme-errorText: #FF0000;--newRedditTheme-field: #F6F7F8;--newRedditTheme-fieldFade: #F6F7F800;--newRedditTheme-flair: #EDEFF1;--newRedditTheme-highlight: #e9f5fd;--newRedditTheme-inactive: #EDEFF1;--newRedditTheme-invertFilter: invert(0);--newRedditTheme-lightText: #FFFFFF;--newRedditTheme-lightTextAlpha75: rgba(255,255,255,0.75);--newRedditTheme-line: #EDEFF1;--newRedditTheme-lineShaded80: #bdbfc0;--newRedditTheme-lineShaded90: #d5d7d8;--newRedditTheme-linkText: #0079D3;--newRedditTheme-linkTextAlpha80: rgba(0,121,211,0.5);--newRedditTheme-linkTextShaded80: #0060a8;--newRedditTheme-linkTextTinted80: #3293db;--newRedditTheme-linkTextWithBody: #3f9ade;--newRedditTheme-menu: #FFFFFF;--newRedditTheme-menuActiveText: #0079D3;--newRedditTheme-menuButtonBackground-active: rgba(0,0,0,0.08);--newRedditTheme-menuButtonBackground-focus: rgba(0,0,0,0.12);--newRedditTheme-menuButtonBackground-hover: rgba(0,0,0,0.04);--newRedditTheme-menuInactiveText: #0079D3;--newRedditTheme-metaText: #7c7c7c;--newRedditTheme-metaTextAlpha50: rgba(120,124,126,0.5);--newRedditTheme-metaTextShaded80: #606364;--newRedditTheme-monospaceColor: #FF006D;--newRedditTheme-navBar-activeLink: #E9F5FD;--newRedditTheme-navBar-activeSubmenuCaret: #24A0ED;--newRedditTheme-navBar-activeSubmenuLink: #24A0ED;--newRedditTheme-navBar-backgroundColor: #24A0ED;--newRedditTheme-navBar-backgroundImage: initial;--newRedditTheme-navBar-hoverLink: #E9F5FD;--newRedditTheme-navBar-inactiveLink: #EDEFF1;--newRedditTheme-navBar-inactiveSubmenuCaret: #42adf0;--newRedditTheme-navBar-inactiveSubmenuLink: #42adf0;--newRedditTheme-navBar-submenuBackgroundColor: #def1fc;--newRedditTheme-navIcon: #1A1A1B;--newRedditTheme-navIconFaded10: rgba(26,26,27,0.1);--newRedditTheme-nsfw: #ff585b;--newRedditTheme-nsfwBlocking-bgcolor: #edeff1;--newRedditTheme-nsfwBlocking-color: #030303;--newRedditTheme-nsfwBlocking-contentTitleBgColor: #f6f7f8;;--newRedditTheme-nsfwBlocking-mainCtaBgColor: #fff;--newRedditTheme-orangeRed: #FF4500;--newRedditTheme-pageHeader: #0079D3;--newRedditTheme-placeholder: #d6d6d6;--newRedditTheme-post: #FFFFFF;--newRedditTheme-postError: #ffe5e5;--newRedditTheme-postFlairText: #1A1A1B;--newRedditTheme-postIcon: #898989;--newRedditTheme-postLine: #ccc;--newRedditTheme-postLineShaded80: #a3a3a3;--newRedditTheme-postLineShaded90: #b7b7b7;--newRedditTheme-postTinted20: #fff;--newRedditTheme-postTransparent20: rgba(255,255,255,0.8);--newRedditTheme-quarantine: #ffb000;--newRedditTheme-report: #fff7e5;--newRedditTheme-search-syntaxHighlightBackgroundColor: #E9F5FD;--newRedditTheme-search-syntaxHighlightColor: #1A1A1A;--newRedditTheme-titleText: #1A1A1B;--newRedditTheme-upsell-appleIcon: #000000;--newRedditTheme-upsell-ssoButtonBorderColor: #D3D6DA;--newRedditTheme-upsell-ssoButtonTextColor: #3D4043;--newRedditTheme-voteIcons-downvoteActive: initial;--newRedditTheme-voteIcons-downvoteInactive: initial;--newRedditTheme-voteIcons-upvoteActive: initial;--newRedditTheme-voteIcons-upvoteInactive: initial;--newRedditTheme-voteText-base: #898989;--newRedditTheme-voteText-downvote: #7193FF;--newRedditTheme-voteText-downvoteShaded80: #5a75cc;--newRedditTheme-voteText-downvoteTinted80: #8da8ff;--newRedditTheme-voteText-upvote: #FF4500;--newRedditTheme-voteText-upvoteShaded80: #cc3700;--newRedditTheme-voteText-upvoteTinted80: #ff6a32;--newRedditTheme-widgetColors-lineColor: rgba(26,26,27,0.07);--newRedditTheme-widgetColors-sidebarWidgetBackgroundColor: #FFFFFF;--newRedditTheme-widgetColors-sidebarWidgetBorderColor: #ccc;--newRedditTheme-widgetColors-sidebarWidgetHeaderColor: #FFFFFF;--newRedditTheme-widgetColors-sidebarWidgetHeaderColorAlpha60: rgba(255,255,255,0.6);--newRedditTheme-widgetColors-sidebarWidgetTextColor: #1A1A1B;--newRedditTheme-widgetColors-sidebarWidgetTextColorShaded80: #141415;--newRedditTheme-widgetColors-sidebarWidgetTitleColor: #1A1A1B;--subredditContext-emojiHeight: initial;--subredditContext-emojiWidth: initial; }</style><div class=""><header data-redditstyle="true" class="_1tvdSTbdxaK-BnUbzUIqIY _2GyPfdsi-MbQFyHRECo9GO cx1ohrUAq6ARaXTX2u8YN   flex-grow-0 flex-shrink-0 top-0 left-0 right-0 fixed z-[80] "><div class="_2vkeRJojnV7cb9pMlPHy7d a35Fm2MurU14xdNybLiZp "><div class="_3dnbqz69WJTFCss8wl7Wlk"><span class="_1RIl585IYPW6cmNXwgRz0J">Press J to jump to the feed. Press question mark to learn the rest of the keyboard shortcuts</span><div class="_32Xa3voy05uAFz3ZnopP_S " data-testid="jump-to-content"><button role="button" tabindex="0" class="_3KaTO_3YaHK3SMocnu8jV9 _2iuoyPiKHN3kfOoeIQalDT _3zbhtNO0bdck0oYbYRhjMC HNozj_dKjQZ59ZsfEegz8 " style="margin-left: -500px;">Jump to content</button><div class="_1Bt_cwKVUG30M9eNB-9rU4 "></div></div><a aria-label="Home" class="_30BbATRhFv3V83DHNDjJAO" href="/?feed=home"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" class="_1O4jTk-dZ-VIxsCuYB6OR8 "><g><circle fill="#FF4500" cx="10" cy="10" r="10"></circle><path fill="#FFF" d="M16.67,10A1.46,1.46,0,0,0,14.2,9a7.12,7.12,0,0,0-3.85-1.23L11,4.65,13.14,5.1a1,1,0,1,0,.13-0.61L10.82,4a0.31,0.31,0,0,0-.37.24L9.71,7.71a7.14,7.14,0,0,0-3.9,1.23A1.46,1.46,0,1,0,4.2,11.33a2.87,2.87,0,0,0,0,.44c0,2.24,2.61,4.06,5.83,4.06s5.83-1.82,5.83-4.06a2.87,2.87,0,0,0,0-.44A1.46,1.46,0,0,0,16.67,10Zm-10,1a1,1,0,1,1,1,1A1,1,0,0,1,6.67,11Zm5.81,2.75a3.84,3.84,0,0,1-2.47.77,3.84,3.84,0,0,1-2.47-.77,0.27,0.27,0,0,1,.38-0.38A3.27,3.27,0,0,0,10,14a3.28,3.28,0,0,0,2.09-.61A0.27,0.27,0,1,1,12.48,13.79Zm-0.18-1.71a1,1,0,1,1,1-1A1,1,0,0,1,12.29,12.08Z"></path></g></svg><svg class="_1bWuGs_1sq4Pqy099x_yy-" viewBox="0 0 57 18" xmlns="http://www.w3.org/2000/svg"><g fill="#1c1c1c"><path d="M54.63,16.52V7.68h1a1,1,0,0,0,1.09-1V6.65a1,1,0,0,0-.93-1.12H54.63V3.88a1.23,1.23,0,0,0-1.12-1.23,1.2,1.2,0,0,0-1.27,1.11V5.55h-1a1,1,0,0,0-1.09,1v.07a1,1,0,0,0,.93,1.12h1.13v8.81a1.19,1.19,0,0,0,1.19,1.19h0a1.19,1.19,0,0,0,1.25-1.12A.17.17,0,0,0,54.63,16.52Z"></path><circle fill="#FF4500" cx="47.26" cy="3.44" r="2.12"></circle><path d="M48.44,7.81a1.19,1.19,0,1,0-2.38,0h0v8.71a1.19,1.19,0,0,0,2.38,0Z"></path><path d="M30.84,1.19A1.19,1.19,0,0,0,29.65,0h0a1.19,1.19,0,0,0-1.19,1.19V6.51a4.11,4.11,0,0,0-3-1.21c-3.1,0-5.69,2.85-5.69,6.35S22.28,18,25.42,18a4.26,4.26,0,0,0,3.1-1.23,1.17,1.17,0,0,0,1.47.8,1.2,1.2,0,0,0,.85-1.05ZM25.41,15.64c-1.83,0-3.32-1.77-3.32-4s1.48-4,3.32-4,3.31,1.78,3.31,4-1.47,3.95-3.3,3.95Z"></path><path d="M43.28,1.19A1.19,1.19,0,0,0,42.09,0h0a1.18,1.18,0,0,0-1.18,1.19h0V6.51a4.15,4.15,0,0,0-3-1.21c-3.1,0-5.69,2.85-5.69,6.35S34.72,18,37.86,18A4.26,4.26,0,0,0,41,16.77a1.17,1.17,0,0,0,1.47.8,1.19,1.19,0,0,0,.85-1.05ZM37.85,15.64c-1.83,0-3.31-1.77-3.31-4s1.47-4,3.31-4,3.31,1.78,3.31,4-1.47,3.95-3.3,3.95Z"></path><path d="M17.27,12.44a1.49,1.49,0,0,0,1.59-1.38v-.15a4.81,4.81,0,0,0-.1-.85A5.83,5.83,0,0,0,13.25,5.3c-3.1,0-5.69,2.85-5.69,6.35S10.11,18,13.25,18a5.66,5.66,0,0,0,4.39-1.84,1.23,1.23,0,0,0-.08-1.74l-.11-.09a1.29,1.29,0,0,0-1.58.17,3.91,3.91,0,0,1-2.62,1.12A3.54,3.54,0,0,1,10,12.44h7.27Zm-4-4.76a3.41,3.41,0,0,1,3.09,2.64H10.14A3.41,3.41,0,0,1,13.24,7.68Z"></path><path d="M7.68,6.53a1.19,1.19,0,0,0-1-1.18A4.56,4.56,0,0,0,2.39,6.91V6.75A1.2,1.2,0,0,0,0,6.75v9.77a1.23,1.23,0,0,0,1.12,1.24,1.19,1.19,0,0,0,1.26-1.1.66.66,0,0,0,0-.14v-5A3.62,3.62,0,0,1,5.81,7.7a4.87,4.87,0,0,1,.54,0h.24A1.18,1.18,0,0,0,7.68,6.53Z"></path></g></svg></a><div aria-label="Start typing to filter your communities or use up and down to select." class="_3jiriKeNer8y0-1r6oWIFM _3rS8YTDjcT7fs0k9W4rxDG" role="navigation"><button class="h-jI8r2f9ozTNqu_2TBeY" tabindex="0"><span class="_1GieMuLljOrqnVpRAwz7VP"><h1 class="_eYtD2XCVieq6emjKBH3m">Subreddit Results</h1></span><img alt="Subreddit Icon" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" class="_34CfAAowTqdbNDYXz5tBTW _3fvJBCH6c6P0NvMwoqK9MJ " style="background-color: rgb(148, 224, 68);"><i class="_3CG2U_hX3HI-ibl5v2RCq1 icon icon-caret_down"></i></button></div><div class="_1iqnOY2Y57wmetu8MAjiId"><div class="_1blFGqU8stoZgWSZ8MQNpf _3jiriKeNer8y0-1r6oWIFM _2dlTXDaX9JuL0bekTwhV18 " id="SearchDropdown"><div class="_1DeR7_QiQnu2UK0e2dDfYD"><form action="/search/" autocomplete="off" class="_1ugesNSGtWAUEmFe-hdnyI" method="get" role="search"><label class="_1t0x2fnX0IYp1-sp47CSHI" for="header-search-bar"><div aria-hidden="true" class="cNtxQ5c1PdvcDe82u_yz9"><i class="_3ylUT2QX58nnEl8r4H26ys icon icon-search"></i></div><span aria-live="assertive" class="_1RIl585IYPW6cmNXwgRz0J">Search within r/androidapps</span></label><div class="_3LO_LEpMLN8-uaedpg6nl4 _2Xr7MVf-5monsBWevLifeW" data-testid="search-scope-pill"><div data-testid="search-scope-pill-text" class="_3CUdiRoAXQxoYJ-UeFCjPS _2SVIoeexI3lRGCH0NAYAMx XuI5nsPhP6eDNKSKFz-e4"><img alt="Subreddit Icon" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" class="_34CfAAowTqdbNDYXz5tBTW _2me05I1oHEys1gUyyDWswt _3WmD5z1Jh2YlJtFiczfOPQ " style="background-color: rgb(0, 121, 211);">r/androidapps<button aria-label="Remove community search filter" class="_1xMEc-Wt4Qb0j1YKfgnaV- fHi-ixYo4c6B0nG6gLHfT" data-testid="search-scope-pill-button" id="search-scope-pill-button" type="button"><i class="WBGmEslY0knAV_FJ6nxJG icon icon-clear"></i></button></div></div><input type="search" class="_1K7ubH9z5v9E6C19j2fjQU" id="header-search-bar" name="q" placeholder="Search Reddit" value="photo"></form><button aria-label="Remove search bar text" id="search-bar-dismiss-button" class="_3XsEUsC3uEaiEi63QWpAM" data-testid="search-bar-dismiss-button"><i class="icon icon-clear"></i></button></div></div></div></div><div class="_2u8LqkbMtzd0lpblMFbJq5"><div class="_19oWd7e3z7-ztUGzdIoCR7"><div class="_1JBkpB_FOZMZ7IPr3FyNfH"><button role="button" tabindex="0" class="_3Wg53T10KuuPmyWOMWsY2F Z_HUY3BUsGOBOtdmH94ZS _2iuoyPiKHN3kfOoeIQalDT _2tU8R9NTqhvBrhoNAXWWcP HNozj_dKjQZ59ZsfEegz8 _1tPpYVD73ugqp4k-VMFRki _2Z-LWN_PrkTncEM_mPuEW5"><i class="_1mvTX6krm3Q2d1CSyUm28s _1vXK1WOmrEh97U366xznqT  icon icon-qr_code"></i>Get App</button><a role="button" tabindex="0" href="https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2Fr%2Fandroidapps%2Fsearch%2F%3Fq%3Dphoto%26sort%3Dnew" class="_3Wg53T10KuuPmyWOMWsY2F Z_HUY3BUsGOBOtdmH94ZS q_unSaY23rpdd3lDvGZ- _2iuoyPiKHN3kfOoeIQalDT _10BQ7pjWbeYP63SAPNS8Ts HNozj_dKjQZ59ZsfEegz8 _2Z-LWN_PrkTncEM_mPuEW5">Log In</a></div><div id="email-verification-tooltip-id" class="XZK-LTFT5CgGo9MvPQQsy U3FRqDA_Qhr4icbaNXSuf"><div id="change-username-tooltip-id" class="XZK-LTFT5CgGo9MvPQQsy _20HfCAFz3ot1MW1o29ZoGZ"></div><div class="header-user-dropdown"><button aria-expanded="false" aria-haspopup="true" id="USER_DROPDOWN_ID" class="_10K5i7NW6qcm-UoCtpB3aK _1pA8z73SZ1olP5KMKFN4_Z _18X7KoiaLuKbuLqg4zE8BH _22SL37yETIW414yUiZj27w"><span class="DFKWwVItcycZV1bKUOyay"><span class="_3KfbpxpA8Esu_3UHTmIvfw _22SL37yETIW414yUiZj27w"><i class="_3-lF5kPDkSGfnVUW_GtvUV icon icon-user"></i></span><i class="_3x3dhQasGAuYcXVQ02QUzy icon icon-caret_down"></i></span><span class="_1RIl585IYPW6cmNXwgRz0J">User account menu</span></button></div></div></div></div></div></header><div class="_1C1Dn0NhEGQkEA9tDGKKSH  OEQgz7Lkj--3zFaLL7BUF _1HWVXJoazfrENIGlRprCVp _2elztvdigLcbcRyu_4wcFW"><img class="_3BcAFuYpz37S0WFvgyWCUN" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAE9 0lEQVRoQ9WYW0hlZRTHf94TIXXAYRQzQwmFQQSVYSZ6UlESH+whRxMDX6IHJ1AQCXFQkSFUCIUeCkETUx/CF1FB8ClNpFFEX8T UKWkyxgFngjRvJ9Z278Pe57Yv51Kul33O3mut7/9fa32X9UVxwyXqhuMn0gR+BbJ0QfsU+CaYIEaSgEuAulzKQ3lGR0fLzzngA 6ckIkpAA68HGxWlQHCMw7Ghg4i5AhBIBE4d+HTO3OZgscB5bW0tk5OTbtPV1VXu3bv3v8/AZ8DXwAmQODw8TFNTE0dHR6SlpWl kHFeCY0MLGSgE1lW9D4Fp4AdAfmvyO5BpwZdflVATuF5ijJIAnAUDMpBtuAhIYa+GC7RhFQvxIFoGQh2YiJXQR8AU8C6wE+Lg+ HQXjkhFNAvhICCREhLh8m3IRLgGEQIXgGxgmqwA3wHfqt9CUmGhIvAe8KMDRPGyQzuwc5sES+AXIEe8tbS0MDAwYAnL2dkZt2/ f5tWrV5p+nNOsmBH4EmjzgeoKiE5ISOD01NEZzO3y6uqKmJgY7X8S8DdwB/hDffkx8L2/yPgj0AwMipGAfPjwIS9fvmRmZsbtx 9fJ0lL4/Sitra1RVFQUyMUn6hwyncTPgLcrKyuZm5Ne41ok3SkpKVRVVRmIBAPal63aH7gbH9GJj4/n/FyZKk+AL/R2nhmQqDf v7++TnZ3t1uvu7ubx48dsbGxQUFAQasxe/pKSkpQ5Ijg0SUxM1MrVgFn/R35fNTQ0MDY25jZ8/fo1ycnJHB8fK89Iya1bt9ja2 iIjI8M9pJYd/R6jJ2DoWTUrMRocHKS5WaZFZEWifnIibcS1TE1NKfPRLwH5ODEx4TY4PDwkKysLWfb+K6mpqWF6WlqJa/HsoQ0 ZCPXKEg7SISOQk5PD3t6eAePFxYV+TTfFr6tpRXd0dJTGxsaAdgEJLC0t8eDBA8WBbDDqvY2Xw9jYWC4vL5X3vb29jIyMsLNzf Xq2mkUNfGdnJ11dXVppBLRva2ujr6+vF+hwl5QOnUsAa8BkAF9gdnd3yc3N5e7du2xubhrIic3CwgJlZWWm0ZcgSMb0Ivb3799 neXnZy97XCmSYzerMvtJA+yPga6MxRWtDQUgJOU9Rx5U7mToDaQ9FWbPekPLRbRwGlbq6OsNKZQNbUKr+bvB8nYX+kd1bDlieK Q4KQZDGdggoc9HOhAyETXZTqWk5tebn51NeXu6Iil0CcpS9Y3VF0SNKTU1Vjh1WRGpdPaQFVC8uLubp06ey7HlNDn/HaeV2wS4 Bz3XdCgkrY6h+ZX3/yWtyBxjEVVJSglzAWpUwE/AZ7EAdme15sL29TV5enlW+dHR00NPTE1C/tLSUxcVF2fKV1tVOBt4B9trb2 3nyRPoIa2InCzbKx2+gzXpi21kQmlZIyF5jpqd+l/74T3/hMyPgaEl98eKF0lH5k/X1dQoL5fbdv1RXV0vr+jNQEkjPCgFHJMR IQEobqklmZiYHBwemtSh99+zsrJJMM2VTBZ0DpZwqKiqYn5838+v4e1xcnHYCsITNkpIOzbZ688zz589JT093DNTTcGVlRTmJq jd871t1bJeA5lfOwcptVH9/P62trVbH89IbHx9HLhJUsY3HtoEHgt+At7R39fX1CCAzGRoa4tGjR3q1N4G/zOx8fQ+WgN7n58B XNkAIgyEb+j5VQ0kgWCyO7G88gX8BA0iEQE02M2MAAAAASUVORK5CYII="><span class="_2hQKVL2Pm4yfkiqifapnBp">Found the internet!</span><i class="_1E59q-NCGBwN0Aq_bPsPKb icon icon-refresh_fill"></i></div></div><style>:root { --newCommunityTheme-actionIcon: #878A8C;--newCommunityTheme-actionIconAlpha20: rgba(135,138,140,0.2);--newCommunityTheme-actionIconAlpha50: rgba(135,138,140,0.5);--newCommunityTheme-actionIconShaded80: #6c6e70;--newCommunityTheme-actionIconTinted80: #9fa1a3;--newCommunityTheme-active: #0079D3;--newCommunityTheme-activeAlpha10: rgba(0,121,211,0.1);--newCommunityTheme-activeAlpha20: rgba(0,121,211,0.2);--newCommunityTheme-activeAlpha50: rgba(0,121,211,0.5);--newCommunityTheme-activeLight60: #33a8ff;--newCommunityTheme-activeShaded80: #0060a8;--newCommunityTheme-activeShaded90: #006cbd;--newCommunityTheme-activeTinted05: #f2f8fc;--newCommunityTheme-backgroundImage: initial;--newCommunityTheme-backgroundImagePosition: cover;--newCommunityTheme-banner-backgroundColor: #33a8ff;--newCommunityTheme-banner-backgroundImage: initial;--newCommunityTheme-banner-backgroundImagePosition: cover;--newCommunityTheme-banner-communityNameFormat: slashtag;--newCommunityTheme-banner-height: 64;--newCommunityTheme-banner-iconColor: #0079D3;--newCommunityTheme-banner-iconDimensions-borderRadius: 24;--newCommunityTheme-banner-iconDimensions-customSize: 32;--newCommunityTheme-banner-iconDimensions-padding: 6;--newCommunityTheme-banner-iconDimensions-size: 24;--newCommunityTheme-banner-iconImage: initial;--newCommunityTheme-banner-lineHeight: 38;--newCommunityTheme-banner-positionedImage: initial;--newCommunityTheme-banner-positionedImageAlignment: left;--newCommunityTheme-banner-positionedImageHeight: 48;--newCommunityTheme-banner-secondaryBannerPositionedImage: initial;--newCommunityTheme-body: #FFFFFF;--newCommunityTheme-bodyAlpha50: rgba(255,255,255,0.5);--newCommunityTheme-bodyAlpha70: rgba(255,255,255,0.7);--newCommunityTheme-bodyAlpha80: rgba(255,255,255,0.8);--newCommunityTheme-bodyFade: #FFFFFF00;--newCommunityTheme-bodyShaded80: #ccc;--newCommunityTheme-bodyText: #1c1c1c;--newCommunityTheme-bodyTextAlpha03: rgba(28,28,28,0.03);--newCommunityTheme-bodyTextAlpha20: rgba(28,28,28,0.2);--newCommunityTheme-bodyTextShaded20: #050505;--newCommunityTheme-bodyTextTinted20: #d1d1d1;--newCommunityTheme-bodyTinted50: #fff;--newCommunityTheme-bodyTinted80: #fff;--newCommunityTheme-button: #0079D3;--newCommunityTheme-buttonAlpha05: rgba(0,121,211,0.05);--newCommunityTheme-buttonAlpha10: rgba(0,121,211,0.1);--newCommunityTheme-buttonAlpha20: rgba(0,121,211,0.2);--newCommunityTheme-buttonAlpha40: rgba(0,121,211,0.4);--newCommunityTheme-buttonAlpha50: rgba(0,121,211,0.5);--newCommunityTheme-buttonAlpha80: rgba(0,121,211,0.8);--newCommunityTheme-buttonShaded80: #0060a8;--newCommunityTheme-buttonTinted20: #cce4f6;--newCommunityTheme-buttonTinted50: #7fbce9;--newCommunityTheme-buttonTinted80: #3293db;--newCommunityTheme-canvas: #DAE0E6;--newCommunityTheme-canvasImgPosition: cover;--newCommunityTheme-canvasImgUrl: initial;--newCommunityTheme-checkbox: #000000;--newCommunityTheme-errorText: #FF0000;--newCommunityTheme-field: #F6F7F8;--newCommunityTheme-fieldFade: #F6F7F800;--newCommunityTheme-flair: #EDEFF1;--newCommunityTheme-highlight: #e5f1fa;--newCommunityTheme-inactive: #EDEFF1;--newCommunityTheme-invertFilter: invert(0);--newCommunityTheme-lightText: #FFFFFF;--newCommunityTheme-lightTextAlpha75: rgba(255,255,255,0.75);--newCommunityTheme-line: #EDEFF1;--newCommunityTheme-lineShaded80: #bdbfc0;--newCommunityTheme-lineShaded90: #d5d7d8;--newCommunityTheme-lineShadedNinety: #d5d7d8;--newCommunityTheme-linkText: #0079D3;--newCommunityTheme-linkTextAlpha80: rgba(0,121,211,0.5);--newCommunityTheme-linkTextShaded80: #0060a8;--newCommunityTheme-linkTextTinted80: #3293db;--newCommunityTheme-linkTextWithBody: #3f9ade;--newCommunityTheme-menu: #FFFFFF;--newCommunityTheme-menuActiveText: #0079D3;--newCommunityTheme-menuButtonBackground-active: rgba(0,0,0,0.08);--newCommunityTheme-menuButtonBackground-focus: rgba(0,0,0,0.12);--newCommunityTheme-menuButtonBackground-hover: rgba(0,0,0,0.04);--newCommunityTheme-menuInactiveText: #0079D3;--newCommunityTheme-metaText: #7c7c7c;--newCommunityTheme-monospaceColor: #FF006D;--newCommunityTheme-navBar-activeLink: #0079D3;--newCommunityTheme-navBar-activeSubmenuCaret: #0079D3;--newCommunityTheme-navBar-activeSubmenuLink: #0079D3;--newCommunityTheme-navBar-backgroundColor: #dbf0ff;--newCommunityTheme-navBar-backgroundImage: initial;--newCommunityTheme-navBar-hoverLink: #0079D3;--newCommunityTheme-navBar-inactiveLink: #0079D3;--newCommunityTheme-navBar-inactiveSubmenuCaret: #33a8ff;--newCommunityTheme-navBar-inactiveSubmenuLink: #33a8ff;--newCommunityTheme-navBar-submenuBackgroundColor: #dbf0ff;--newCommunityTheme-navIcon: #1A1A1B;--newCommunityTheme-navIconFaded10: rgba(26,26,27,0.1);--newCommunityTheme-nsfwBlocking-bgcolor: #edeff1;--newCommunityTheme-nsfwBlocking-color: #030303;--newCommunityTheme-nsfwBlocking-contentTitleBgColor: #f6f7f8;;--newCommunityTheme-nsfwBlocking-mainCtaBgColor: #fff;--newCommunityTheme-orangeRed: #FF4500;--newCommunityTheme-pageHeader: #0079D3;--newCommunityTheme-placeholder: #d6d6d6;--newCommunityTheme-placeholderImage: initial;--newCommunityTheme-placeholderImagePosition: cover;--newCommunityTheme-post: #FFFFFF;--newCommunityTheme-postError: #ffe5e5;--newCommunityTheme-postFlairText: #1A1A1B;--newCommunityTheme-postIcon: #898989;--newCommunityTheme-postLine: #ccc;--newCommunityTheme-postLineShaded80: #a3a3a3;--newCommunityTheme-postLineShaded90: #b7b7b7;--newCommunityTheme-postTinted20: #fff;--newCommunityTheme-postTransparent20: rgba(255,255,255,0.8);--newCommunityTheme-primaryButtonShadedEighty: #0060a8;--newCommunityTheme-primaryButtonTintedEighty: #3293db;--newCommunityTheme-primaryButtonTintedFifty: #7fbce9;--newCommunityTheme-primaryButtonTintedSixty: #66aee4;--newCommunityTheme-report: #fff7e5;--newCommunityTheme-textTransparentizedEighty: rgba(26,26,27,0.2);--newCommunityTheme-titleText: #222222;--newCommunityTheme-voteIcons-downvoteActive: initial;--newCommunityTheme-voteIcons-downvoteInactive: initial;--newCommunityTheme-voteIcons-upvoteActive: initial;--newCommunityTheme-voteIcons-upvoteInactive: initial;--newCommunityTheme-voteText-base: #898989;--newCommunityTheme-voteText-downvote: #7193FF;--newCommunityTheme-voteText-downvoteShaded80: #5a75cc;--newCommunityTheme-voteText-downvoteTinted80: #8da8ff;--newCommunityTheme-voteText-upvote: #FF4500;--newCommunityTheme-voteText-upvoteShaded80: #cc3700;--newCommunityTheme-voteText-upvoteTinted80: #ff6a32;--newCommunityTheme-widgetColors-lineColor: rgba(26,26,27,0.07);--newCommunityTheme-widgetColors-sidebarWidgetBackgroundColor: #FFFFFF;--newCommunityTheme-widgetColors-sidebarWidgetBorderColor: #ccc;--newCommunityTheme-widgetColors-sidebarWidgetHeaderColor: #FFFFFF;--newCommunityTheme-widgetColors-sidebarWidgetHeaderColorAlpha60: rgba(255,255,255,0.6);--newCommunityTheme-widgetColors-sidebarWidgetTextColor: #1A1A1B;--newCommunityTheme-widgetColors-sidebarWidgetTextColorShaded80: #141415;--newCommunityTheme-widgetColors-sidebarWidgetTitleColor: #1A1A1B;--newRedditTheme-actionIcon: #878A8C;--newRedditTheme-actionIconAlpha20: rgba(135,138,140,0.2);--newRedditTheme-actionIconAlpha50: rgba(135,138,140,0.5);--newRedditTheme-actionIconShaded80: #6c6e70;--newRedditTheme-actionIconTinted80: #9fa1a3;--newRedditTheme-active: #24A0ED;--newRedditTheme-activeAlpha10: rgba(36,160,237,0.1);--newRedditTheme-activeAlpha20: rgba(36,160,237,0.2);--newRedditTheme-activeAlpha50: rgba(36,160,237,0.5);--newRedditTheme-activeLight60: #42adf0;--newRedditTheme-activeShaded80: #1c80bd;--newRedditTheme-activeShaded90: #2090d5;--newRedditTheme-activeTinted05: #f4fafe;--newRedditTheme-banner-backgroundColor: #24A0ED;--newRedditTheme-banner-backgroundImage: initial;--newRedditTheme-banner-backgroundImagePosition: cover;--newRedditTheme-banner-communityNameFormat: slashtag;--newRedditTheme-banner-height: 64;--newRedditTheme-banner-iconColor: #24A0ED;--newRedditTheme-banner-iconDimensions-borderRadius: 24;--newRedditTheme-banner-iconDimensions-customSize: 32;--newRedditTheme-banner-iconDimensions-padding: 6;--newRedditTheme-banner-iconDimensions-size: 24;--newRedditTheme-banner-iconImage: initial;--newRedditTheme-banner-lineHeight: 38;--newRedditTheme-banner-positionedImage: initial;--newRedditTheme-banner-positionedImageAlignment: cover;--newRedditTheme-banner-positionedImageHeight: 48;--newRedditTheme-banner-secondaryBannerPositionedImage: initial;--newRedditTheme-body: #FFFFFF;--newRedditTheme-bodyAlpha50: rgba(255,255,255,0.5);--newRedditTheme-bodyAlpha70: rgba(255,255,255,0.7);--newRedditTheme-bodyAlpha80: rgba(255,255,255,0.8);--newRedditTheme-bodyFade: #FFFFFF00;--newRedditTheme-bodyShaded80: #ccc;--newRedditTheme-bodyText: #1c1c1c;--newRedditTheme-bodyTextAlpha03: rgba(28,28,28,0.03);--newRedditTheme-bodyTextAlpha20: rgba(28,28,28,0.2);--newRedditTheme-bodyTextShaded20: #050505;--newRedditTheme-bodyTextTinted20: #d1d1d1;--newRedditTheme-bodyTinted50: #fff;--newRedditTheme-bodyTinted80: #fff;--newRedditTheme-button: #0079D3;--newRedditTheme-buttonAlpha05: rgba(0,121,211,0.05);--newRedditTheme-buttonAlpha10: rgba(0,121,211,0.1);--newRedditTheme-buttonAlpha20: rgba(0,121,211,0.2);--newRedditTheme-buttonAlpha40: rgba(0,121,211,0.4);--newRedditTheme-buttonAlpha50: rgba(0,121,211,0.5);--newRedditTheme-buttonAlpha80: rgba(0,121,211,0.8);--newRedditTheme-buttonShaded80: #0060a8;--newRedditTheme-buttonTinted20: #cce4f6;--newRedditTheme-buttonTinted50: #7fbce9;--newRedditTheme-buttonTinted80: #3293db;--newRedditTheme-canvas: #DAE0E6;--newRedditTheme-checkbox: #000000;--newRedditTheme-errorText: #FF0000;--newRedditTheme-field: #F6F7F8;--newRedditTheme-fieldFade: #F6F7F800;--newRedditTheme-flair: #EDEFF1;--newRedditTheme-highlight: #e9f5fd;--newRedditTheme-inactive: #EDEFF1;--newRedditTheme-invertFilter: invert(0);--newRedditTheme-lightText: #FFFFFF;--newRedditTheme-lightTextAlpha75: rgba(255,255,255,0.75);--newRedditTheme-line: #EDEFF1;--newRedditTheme-lineShaded80: #bdbfc0;--newRedditTheme-lineShaded90: #d5d7d8;--newRedditTheme-linkText: #0079D3;--newRedditTheme-linkTextAlpha80: rgba(0,121,211,0.5);--newRedditTheme-linkTextShaded80: #0060a8;--newRedditTheme-linkTextTinted80: #3293db;--newRedditTheme-linkTextWithBody: #3f9ade;--newRedditTheme-menu: #FFFFFF;--newRedditTheme-menuActiveText: #0079D3;--newRedditTheme-menuButtonBackground-active: rgba(0,0,0,0.08);--newRedditTheme-menuButtonBackground-focus: rgba(0,0,0,0.12);--newRedditTheme-menuButtonBackground-hover: rgba(0,0,0,0.04);--newRedditTheme-menuInactiveText: #0079D3;--newRedditTheme-metaText: #7c7c7c;--newRedditTheme-metaTextAlpha50: rgba(120,124,126,0.5);--newRedditTheme-metaTextShaded80: #606364;--newRedditTheme-monospaceColor: #FF006D;--newRedditTheme-navBar-activeLink: #E9F5FD;--newRedditTheme-navBar-activeSubmenuCaret: #24A0ED;--newRedditTheme-navBar-activeSubmenuLink: #24A0ED;--newRedditTheme-navBar-backgroundColor: #24A0ED;--newRedditTheme-navBar-backgroundImage: initial;--newRedditTheme-navBar-hoverLink: #E9F5FD;--newRedditTheme-navBar-inactiveLink: #EDEFF1;--newRedditTheme-navBar-inactiveSubmenuCaret: #42adf0;--newRedditTheme-navBar-inactiveSubmenuLink: #42adf0;--newRedditTheme-navBar-submenuBackgroundColor: #def1fc;--newRedditTheme-navIcon: #1A1A1B;--newRedditTheme-navIconFaded10: rgba(26,26,27,0.1);--newRedditTheme-nsfw: #ff585b;--newRedditTheme-nsfwBlocking-bgcolor: #edeff1;--newRedditTheme-nsfwBlocking-color: #030303;--newRedditTheme-nsfwBlocking-contentTitleBgColor: #f6f7f8;;--newRedditTheme-nsfwBlocking-mainCtaBgColor: #fff;--newRedditTheme-orangeRed: #FF4500;--newRedditTheme-pageHeader: #0079D3;--newRedditTheme-placeholder: #d6d6d6;--newRedditTheme-post: #FFFFFF;--newRedditTheme-postError: #ffe5e5;--newRedditTheme-postFlairText: #1A1A1B;--newRedditTheme-postIcon: #898989;--newRedditTheme-postLine: #ccc;--newRedditTheme-postLineShaded80: #a3a3a3;--newRedditTheme-postLineShaded90: #b7b7b7;--newRedditTheme-postTinted20: #fff;--newRedditTheme-postTransparent20: rgba(255,255,255,0.8);--newRedditTheme-quarantine: #ffb000;--newRedditTheme-report: #fff7e5;--newRedditTheme-search-syntaxHighlightBackgroundColor: #E9F5FD;--newRedditTheme-search-syntaxHighlightColor: #1A1A1A;--newRedditTheme-titleText: #1A1A1B;--newRedditTheme-upsell-appleIcon: #000000;--newRedditTheme-upsell-ssoButtonBorderColor: #D3D6DA;--newRedditTheme-upsell-ssoButtonTextColor: #3D4043;--newRedditTheme-voteIcons-downvoteActive: initial;--newRedditTheme-voteIcons-downvoteInactive: initial;--newRedditTheme-voteIcons-upvoteActive: initial;--newRedditTheme-voteIcons-upvoteInactive: initial;--newRedditTheme-voteText-base: #898989;--newRedditTheme-voteText-downvote: #7193FF;--newRedditTheme-voteText-downvoteShaded80: #5a75cc;--newRedditTheme-voteText-downvoteTinted80: #8da8ff;--newRedditTheme-voteText-upvote: #FF4500;--newRedditTheme-voteText-upvoteShaded80: #cc3700;--newRedditTheme-voteText-upvoteTinted80: #ff6a32;--newRedditTheme-widgetColors-lineColor: rgba(26,26,27,0.07);--newRedditTheme-widgetColors-sidebarWidgetBackgroundColor: #FFFFFF;--newRedditTheme-widgetColors-sidebarWidgetBorderColor: #ccc;--newRedditTheme-widgetColors-sidebarWidgetHeaderColor: #FFFFFF;--newRedditTheme-widgetColors-sidebarWidgetHeaderColorAlpha60: rgba(255,255,255,0.6);--newRedditTheme-widgetColors-sidebarWidgetTextColor: #1A1A1B;--newRedditTheme-widgetColors-sidebarWidgetTextColorShaded80: #141415;--newRedditTheme-widgetColors-sidebarWidgetTitleColor: #1A1A1B;--subredditContext-emojiHeight: initial;--subredditContext-emojiWidth: initial; }</style><div class=""><div class="_1nxEQl5D2Bx2jxDILRHemb   " id="AppRouter-main-content" aria-hidden="false"><div><div class="qYj03fU5CXf5t2Fc5iSvg ListingLayout-outerContainer "><div class="_2wxsLGNmMLx6sEMLJyn2o9 ListingLayout-backgroundContainer" style="--pseudo-before-background:#DAE0E6"></div><div class="_3ozFtOe6WpJEMUtxDOIvtU"><div class="eZLYleuk3b8ykGiskfpo3"><div class="_3Up38k81YNBWQoW1ovMU88"><div><div data-testid="search-results-nav" class="_21H_PIzpqfpibB_EcUDwpj"><div class="_3XkfKrHLCXvnVsLyBJXzzv" role="tablist"><a class="_1gui9gwvmz0Ta6TaySS6jf" data-testid="tab_posts" aria-selected="true" role="tab" href="/r/androidapps/search/?q=photo&amp;type=link"><button class="cmR5BF4NpBUm3DBMZCmJS _2jNQT-6WbFOjX2hdDWV56w _2dj14FxV-bfkwopj1jV_fF">Posts</button></a><a class="_1gui9gwvmz0Ta6TaySS6jf" data-testid="tab_comments" aria-selected="false" role="tab" href="/r/androidapps/search/?q=photo&amp;type=comment"><div class="_2J_zB4R1FH2EjGMkQjedwc u6HtAZu8_LKL721-EnKuR" style="position: absolute; left: 50%; top: 100%; background-color: rgb(0, 109, 198); transform: translateX(-50%); white-space: nowrap;">Now you can search comments!<div class="_1jsc29CjRXZWjd2tr0Ji0Y" style="border-left: 4px solid transparent; border-right: 4px solid transparent; top: -3px; left: 50%; transform: translateX(-50%); border-bottom: 3px solid rgb(0, 109, 198);"></div></div><button class="cmR5BF4NpBUm3DBMZCmJS _2jNQT-6WbFOjX2hdDWV56w _1g3g98ViMb36cM-peU17Jk">Comments</button></a><a class="_1gui9gwvmz0Ta6TaySS6jf" data-testid="tab_communities" aria-selected="false" role="tab" href="/r/androidapps/search/?q=photo&amp;type=sr"><button class="cmR5BF4NpBUm3DBMZCmJS _2jNQT-6WbFOjX2hdDWV56w _1g3g98ViMb36cM-peU17Jk">Communities</button></a><a class="_1gui9gwvmz0Ta6TaySS6jf" data-testid="tab_people" aria-selected="false" role="tab" href="/r/androidapps/search/?q=photo&amp;type=user"><button class="cmR5BF4NpBUm3DBMZCmJS _2jNQT-6WbFOjX2hdDWV56w _1g3g98ViMb36cM-peU17Jk">People</button></a></div><div class="_10JrVcY3xBcUNO7dNh0Js2"><a class="_1i7CStyaaHQU2aiG0GdpSA _3Tphf4AA5J39saIlrB1SYD " data-testid="search-switcher-link" href="/search/?q=photo"><span>Show results from</span><p class="-V0kqUlRHvLoNRUAUmCy9 ">all of Reddit</p><i class="N0zmIZbfRSCGk2rUOGHSS  icon icon-forward"></i></a></div></div><div data-testid="search-results-subnav" class="XZK-LTFT5CgGo9MvPQQsy _26jxFFm8Z3TxPyZxoddAGy"><div class="_3yqn7UgWZCfM22Sk-rcBbs"><button data-testid="search-results-filter-sort" class="cmR5BF4NpBUm3DBMZCmJS _2jNQT-6WbFOjX2hdDWV56w _1g3g98ViMb36cM-peU17Jk BZDMD8yWu5imupa73nqYE _1HyZhQLyitFqci_zC5jGCy">New<i class="OGoNN0lGfOACQsVwIa1wo icon icon-caret_down"></i></button><div id="search-results-sort"></div></div></div><div class="_79QamRjUfUQIFHxCnTvSZ"><a class="_1i7CStyaaHQU2aiG0GdpSA _3Tphf4AA5J39saIlrB1SYD " data-testid="search-switcher-link" href="/search/?q=photo"><span>Show results from</span><p class="-V0kqUlRHvLoNRUAUmCy9 ">all of Reddit</p><i class="N0zmIZbfRSCGk2rUOGHSS  icon icon-forward"></i></a></div></div><div class="_2lzCpzHH0OvyFsvuESLurr _3SktesklDBwXt2pEl0sHY8"><div class="_1BJGsKulUQfhJyO19XsBph _3SktesklDBwXt2pEl0sHY8"><div tabindex="0"></div><div class="_1MTbwSHIISfMYM16YhZ8kN"><div class="_2mO8vClBdPxiJ30y_C6od2" data-testid="posts-list"><div><div data-scroller-first=""><div><div class="_2dkUkgRYbhbpU_2O2Wc5am _28efb5XEIggTEMzT5v9i61" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_141vuwu" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_141vuwu--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_141vuwu"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/outerzenith/">u/outerzenith</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">11 hours ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_141vuwu nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_141vuwu.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/141vuwu/photo_editor_that_gives_filter_editing_capability/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m"><span class="_1Nh8xLEUG3orjY1k1aijj">Photo</span> editor that gives filter / editing capability similar to iPhone?</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22REQUEST%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">REQUEST</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">2 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">1 comment</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_140nz1p" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_140nz1p--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_140nz1p"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/I-am-ocean/">u/I-am-ocean</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">2 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_140nz1p nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_140nz1p.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/140nz1p/island_android_app_cloner_how_to_transfer_files/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Island Android app cloner, how to transfer files out of cloned work profile file manager?</h3></div></a></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">2 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">5 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_140k5xt" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_140k5xt--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_140k5xt"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/Salty_Poetry7323/">u/Salty_Poetry7323</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">2 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_140k5xt nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_140k5xt.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/140k5xt/photos_gone_after_deleting_whatsapp/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Photos gone after deleting Whatsapp</h3></div></a></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">1 upvote</span><span class="_vaFo96phV6L5Hltvwcox">3 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13yl90s" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13yl90s--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13yl90s"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/MMFSdjw/">u/MMFSdjw</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">4 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13yl90s nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13yl90s.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13yl90s/image_viewer_with_proper_sorting/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Image viewer with proper sorting</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">4 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">3 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13yk092" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13yk092--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13yk092"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/Hotchipsandpepsi/">u/Hotchipsandpepsi</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">4 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13yk092 nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13yk092.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13yk092/is_there_a_good_automatic_cropping_tool_for/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Is there a good automatic cropping tool for borders I can download?</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">4 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">0 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13xyavq" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13xyavq--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13xyavq"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/noneabove1182/">u/noneabove1182</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">4 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13xyavq nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13xyavq.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13xyavq/are_there_any_gallery_apps_that_handle_burst/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Are there ANY gallery apps that handle burst shots as well as Google photos?</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22REQUEST%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">REQUEST</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">5 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">8 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13xvfnt" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13xvfnt--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13xvfnt"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/odukle/">u/odukle</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">4 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13xvfnt nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13xvfnt.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13xvfnt/generate_really_cool_captions_for_your_photos_in/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Generate really cool captions for your photos in seconds using this GPT powered app</h3></div></a></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">0 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">0 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13xry4m" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13xry4m--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13xry4m"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/gigimarzo/">u/gigimarzo</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">5 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13xry4m nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13xry4m.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13xry4m/app_for_organizing_photos_and_videos_starting/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">App for "organizing" photos and videos starting from the date in the file name, not from the metadata!</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22REQUEST%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">REQUEST</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">4 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">2 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13xdn8m" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13xdn8m--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13xdn8m"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/sashatinkoff/">u/sashatinkoff</a></div></div><div><span class="_1jNPl3YUk6zbpLWdjaJT1r " style="background-color:#EDEFF1;color:#1A1A1B">(DEV) Selfie Timelapse App</span></div><span data-testid="post_timestamp" data-click-id="timestamp">5 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13xdn8m nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13xdn8m.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13xdn8m/summer_23_promo_codes/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Summer 23 Promo codes</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22DEV%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">DEV</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">11 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">47 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13xbfr2" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13xbfr2--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13xbfr2"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/iam_asdy/">u/iam_asdy</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">5 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13xbfr2 nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13xbfr2.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13xbfr2/any_open_source_photo_editing_apk_is_there/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Any open source <span class="_1Nh8xLEUG3orjY1k1aijj">photo</span> editing apk is there?</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">1 upvote</span><span class="_vaFo96phV6L5Hltvwcox">1 comment</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13wt13m" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13wt13m--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13wt13m"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/Own_Statistician5421/">u/Own_Statistician5421</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">6 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13wt13m nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13wt13m.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13wt13m/looking_for_an_app_to_switch_the_function_of_a/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">looking for an app to switch the function of a remote shutter</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">1 upvote</span><span class="_vaFo96phV6L5Hltvwcox">2 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13waii9" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13waii9--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13waii9"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/Rimwulf/">u/Rimwulf</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">6 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13waii9 nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13waii9.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13waii9/im_trying_to_remember_an_app_that_uses_your/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">I'm trying to remember an app that uses your devices as cloud storage instead of a remote server but can't remember what it was called.</h3></div></a></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">47 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">31 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13vurdk" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13vurdk--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13vurdk"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/ionhowto/">u/ionhowto</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">7 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13vurdk nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13vurdk.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13vurdk/find_the_difference_game_android_wifes_indie_dev/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Find The Difference Game - Android - Wife's Indie [DEV]</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22DEV%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">DEV</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">5 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">12 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13vtz4o" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13vtz4o--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13vtz4o"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/El_Muchacho_Grande/">u/El_Muchacho_Grande</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">7 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13vtz4o nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13vtz4o.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13vtz4o/app_to_import_and_tag_paper_recipes/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">App to import and tag paper recipes</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">0 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">3 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13tk3df" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13tk3df--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13tk3df"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/Kayato601/">u/Kayato601</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">9 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13tk3df nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13tk3df.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13tk3df/gallery_app/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Gallery app</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">3 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">3 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13t2x1h" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13t2x1h--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13t2x1h"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/Alex_Spin/">u/Alex_Spin</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">10 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13t2x1h nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13t2x1h.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13t2x1h/looking_for_an_app_to_get_my_phones_network/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Looking for an app to get my phone's network activity</h3></div></a></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">4 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">5 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13rfuk7" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13rfuk7--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13rfuk7"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/Sagezu/">u/Sagezu</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">12 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13rfuk7 nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13rfuk7.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13rfuk7/accidentally_cleared_40_gb_of_photos_from_samsung/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Accidentally cleared 40 gb of photos from samsung gallery</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">10 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">11 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13rclz3" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13rclz3--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13rclz3"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/kuzyn007/">u/kuzyn007</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">12 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13rclz3 nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13rclz3.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13rclz3/auto_generate_local_albums/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Auto generate local albums</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">3 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">0 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13qzgqd" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13qzgqd--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13qzgqd"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/Gilgeam/">u/Gilgeam</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">12 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13qzgqd nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13qzgqd.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13qzgqd/messaging_service_with_complete_export_capability/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Messaging service with complete export capability and iOS support?</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">3 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">1 comment</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13pp96g" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13pp96g--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13pp96g"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/UnavailableUsername_/">u/UnavailableUsername_</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">14 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13pp96g nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13pp96g.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13pp96g/looking_for_an_app_to_take_user_fingerprints_so_i/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Looking for an app to take user fingerprints so i can save them as images/png.</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22REQUEST%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">REQUEST</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">0 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">2 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13pkpqp" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13pkpqp--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13pkpqp"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/winnixxl/">u/winnixxl</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">14 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13pkpqp nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13pkpqp.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13pkpqp/looking_for_app_to_label_and_upload_multiple/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Looking for App to Label and Upload multiple Photos and Videos</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22REQUEST%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">REQUEST</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">1 upvote</span><span class="_vaFo96phV6L5Hltvwcox">0 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13p2kjd" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13p2kjd--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13p2kjd"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/Ninomalbinho/">u/Ninomalbinho</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">15 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13p2kjd nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13p2kjd.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13p2kjd/amazon_photos_on_android_tv/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Amazon Photos on Android TV ?</h3></div></a></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">1 upvote</span><span class="_vaFo96phV6L5Hltvwcox">1 comment</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13olal1" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13olal1--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13olal1"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/souless_android/">u/souless_android</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">15 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13olal1 nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13olal1.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13olal1/what_happens_to_photos_resized_in_samsung_builtin/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">what happens to photos resized in Samsung built-in gallery app</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">5 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">1 comment</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13n2zdv" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13n2zdv--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13n2zdv"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/cmdr_cathode/">u/cmdr_cathode</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">17 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13n2zdv nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13n2zdv.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13n2zdv/app_for_singletap_smb_share/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">App for single-tap SMB Share?</h3></div></a></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">0 upvotes</span><span class="_vaFo96phV6L5Hltvwcox">3 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div><div><div><div class="_2dkUkgRYbhbpU_2O2Wc5am" data-adclicklocation="background" data-click-id="background" data-testid="post-container" id="t3_13my2xg" tabindex="-1"><div class="_1poyrkZ7g36PawDueRza-J" style="background:#FFFFFF" data-adclicklocation="background" data-click-id="background"><div class="_2i5O0KNpb9tDq0bsNOZB_Q" data-click-id="body"><div class="_2n04GrCyhhQf-Kshn7akmH _37TF67KpZQl9SHbiAhz3mf _3xeOZ4NlqvpwzbB5E8QC6r _3zxBrqnz24HT1z7OOcRXCS"><div class="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi"><a class="_3d8GzWNAiVF7ncwmjHXlNf" data-testid="subreddit_icon_link" href="/r/androidapps/"><img alt="Subreddit Icon" class="id5ExZR7GqiUypGICnSYs" role="presentation" src="https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&amp;s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c" style="background-color: rgb(148, 224, 68);"></a><a class="_305seOZmrgus3clHOXCmfs" data-testid="subreddit-name" data-click-id="subreddit" href="/r/androidapps/">r/androidapps</a><div class="_3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi" id="SubredditInfoTooltip--t3_13my2xg--androidapps"></div></div><span class="_3LS4zudUBagjFS7HjWJYxo _37gsGHa8DMRAxBmQS-Ppg8" role="presentation">•</span><div class="_3xeOZ4NlqvpwzbB5E8QC6r"><span class="_3-fo1J0EWS8TawiUkoZ9DH">Posted by</span><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t3_13my2xg"><a class="_3-fo1J0EWS8TawiUkoZ9DH _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" data-click-id="user" data-testid="post_author_link_icon" href="/user/thekashnerd/">u/thekashnerd</a></div></div><span data-testid="post_timestamp" data-click-id="timestamp">17 days ago</span></div></div><div class="_2n04GrCyhhQf-Kshn7akmH _19FzInkloQSdrf0rh3Omen"><div class="_2i5O0KNpb9tDq0bsNOZB_Q"><div class="t3_13my2xg nbO8VWsMIB-Mv-tIa37NF" data-adclicklocation="title"><style>
        .t3_13my2xg.nbO8VWsMIB-Mv-tIa37NF {
          --postTitle-VisitedLinkColor: #9b9b9b;
          --postTitleLink-VisitedLinkColor: #9b9b9b;
          --postBodyLink-VisitedLinkColor: #989898;
        }
      </style><div class="_1SAKlLic4t9BBtiiE-Z6ob">
            <img alt="" src="https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png" style="width: 1px; height: 1px;" onload="(__markFirstPostVisible || function(){})();">
          </div><div><a href="/r/androidapps/comments/13my2xg/is_there_a_camera_app_that_sorts_photos/"><div class="_1AKeAGcglmBjK1SUUXNFti _1-SZ3VwLjbFwTzaZvU8FBX _1FT0e6kh1BBb_oALAMW_l7 _1yBpz1MEPxxYTxjlEilGtB" data-testid="post-title" style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">Is there a camera app that sorts photos</h3></div></a><div class="_1AKeAGcglmBjK1SUUXNFti"><a href="/r/androidapps/?f=flair_name%3A%22QUESTION%22"><span class="_1jNPl3YUk6zbpLWdjaJT1r _2VqfzH0dZ9dIl3XWNxs42y aJrgrewN9C8x1Fusdx4hh _1Dl-kvSxyJMWO9nuoTof8N " style="background-color:#EDEFF1;color:#1A1A1B">QUESTION</span></a></div></div></div></div></div><div class="_2IpBiHtzKzIxk2fKI4UOv1 _2n04GrCyhhQf-Kshn7akmH HNL__wz5plDpzJe5Lnn"><span class="_vaFo96phV6L5Hltvwcox">1 upvote</span><span class="_vaFo96phV6L5Hltvwcox">0 comments</span><span class="_vaFo96phV6L5Hltvwcox">0 awards</span></div></div></div></div></div></div></div><div class="_1mLDB-TFHMY0SRGTRD-ipK _2486DvSWPD-F9xM1LaS9AZ"><div class="-epve_JNERIUWcWNKZJF6"><div class="_2dzkHWoQ7wLdDsEAwyw1NL"><div class="_1cE9WBao1CSNnKKQd97erN _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="dXH0UqIq_Mtkd24573Rs5 _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div></div><div class="_1NHO6pCrlHfrC6Q-_d-3kZ"><div class="aHlABuIzfJ3NbabTwjGN8 _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="_22TlQsT52A1DMzjuJNEb7b"><div class="_1wEL9K8jt2pgaYL1hhQt_P _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div></div></div><div class="_2ztqeqAwKeO-Fwjjpm3ou2"><div class="hKjLaaNx-nWjCGihE3wwZ _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="hKjLaaNx-nWjCGihE3wwZ _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="hKjLaaNx-nWjCGihE3wwZ _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div></div></div></div><div class="_1mLDB-TFHMY0SRGTRD-ipK _2486DvSWPD-F9xM1LaS9AZ"><div class="-epve_JNERIUWcWNKZJF6"><div class="_2dzkHWoQ7wLdDsEAwyw1NL"><div class="_1cE9WBao1CSNnKKQd97erN _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="dXH0UqIq_Mtkd24573Rs5 _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div></div><div class="_1NHO6pCrlHfrC6Q-_d-3kZ"><div class="aHlABuIzfJ3NbabTwjGN8 _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="_22TlQsT52A1DMzjuJNEb7b"><div class="_1wEL9K8jt2pgaYL1hhQt_P _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div></div></div><div class="_2ztqeqAwKeO-Fwjjpm3ou2"><div class="hKjLaaNx-nWjCGihE3wwZ _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="hKjLaaNx-nWjCGihE3wwZ _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="hKjLaaNx-nWjCGihE3wwZ _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div></div></div></div><div class="_1mLDB-TFHMY0SRGTRD-ipK _2486DvSWPD-F9xM1LaS9AZ"><div class="-epve_JNERIUWcWNKZJF6"><div class="_2dzkHWoQ7wLdDsEAwyw1NL"><div class="_1cE9WBao1CSNnKKQd97erN _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="dXH0UqIq_Mtkd24573Rs5 _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div></div><div class="_1NHO6pCrlHfrC6Q-_d-3kZ"><div class="aHlABuIzfJ3NbabTwjGN8 _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="_22TlQsT52A1DMzjuJNEb7b"><div class="_1wEL9K8jt2pgaYL1hhQt_P _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div></div></div><div class="_2ztqeqAwKeO-Fwjjpm3ou2"><div class="hKjLaaNx-nWjCGihE3wwZ _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="hKjLaaNx-nWjCGihE3wwZ _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div><div class="hKjLaaNx-nWjCGihE3wwZ _3giTODNeZ-Po90u8Ghs4aI fzTkuBRFT8iIn1XnJX_Yn _34yMY7-6MNnz3utfjExvIq"></div></div></div></div></div></div></div><div class="_2iRJ8DI-3RTbsXRSDXE5ZG"><div data-testid="search-results-sidebar" class="_1FUNcfOeszr8eruqLxCMcR _35ky2Wm3TP6kFdIh-DOxmA"><div class="DpriHZnFiOfa0afZpg8vf" data-testid="communities-list"><h4 class="_3n4VKjpr-iVnAmYcon-YbI">Communities</h4><p class="YoadDFUejEmzEbJmjTvHn">No results</p></div><div class="DpriHZnFiOfa0afZpg8vf" data-testid="authors-list"><h4 class="_3n4VKjpr-iVnAmYcon-YbI">People</h4><p class="YoadDFUejEmzEbJmjTvHn">No results</p></div><div class="_1oRQu-aolgpPPJDblUGTw5"><div class=""><div class="_3Y8af3R9_DE3lpXa6Hq5Ab"><div class="_1KrMye71CT332tKKKUWAj6"><div class="_3f2nSSsPBqVDV6Sz82qgrR"><a href="https://www.redditinc.com/policies/user-agreement" class="_3Eyh3vRo5o4IfzVZXhaWAG">User Agreement</a><a href="https://www.redditinc.com/policies/privacy-policy" class="_3Eyh3vRo5o4IfzVZXhaWAG">Privacy policy</a></div><div class="_3f2nSSsPBqVDV6Sz82qgrR"><a href="https://www.redditinc.com/policies/content-policy" class="_3Eyh3vRo5o4IfzVZXhaWAG">Content policy</a><a href="https://www.redditinc.com/policies/moderator-guidelines" class="_3Eyh3vRo5o4IfzVZXhaWAG">Moderator Code of Conduct</a></div></div><div class="_34dh2eyzMvJfjCBLeoWiDD">Reddit, Inc. © 2023. All rights reserved.</div></div></div><div class="_3Tc8YYRhVDX9vlR0XePZfH _365FiUZ11efXHV7l7fNp6K" style="top:calc(100vh - 8px)"><button role="button" tabindex="0" class="_2iuoyPiKHN3kfOoeIQalDT _2tU8R9NTqhvBrhoNAXWWcP HNozj_dKjQZ59ZsfEegz8 _2Z-LWN_PrkTncEM_mPuEW5">Back to Top</button></div></div></div></div></div></div></div></div></div></div></div></div><style>.subredditvars-r-androidapps { --newCommunityTheme-actionIcon: #878A8C;--newCommunityTheme-actionIconAlpha20: rgba(135,138,140,0.2);--newCommunityTheme-actionIconAlpha50: rgba(135,138,140,0.5);--newCommunityTheme-actionIconShaded80: #6c6e70;--newCommunityTheme-actionIconTinted80: #9fa1a3;--newCommunityTheme-active: #94E044;--newCommunityTheme-activeAlpha10: rgba(148,224,68,0.1);--newCommunityTheme-activeAlpha20: rgba(148,224,68,0.2);--newCommunityTheme-activeAlpha50: rgba(148,224,68,0.5);--newCommunityTheme-activeLight60: #9be250;--newCommunityTheme-activeShaded80: #76b336;--newCommunityTheme-activeShaded90: #85c93d;--newCommunityTheme-activeTinted05: #f9fdf5;--newCommunityTheme-backgroundImage: initial;--newCommunityTheme-backgroundImagePosition: cover;--newCommunityTheme-banner-backgroundColor: #9be250;--newCommunityTheme-banner-backgroundImage: url("https://styles.redditmedia.com/t5_2reen/styles/bannerBackgroundImage_dj49qrqgwan71.jpg?format=pjpg&s=68811497e761345ad55a9ac8637ef525b5e9993b");--newCommunityTheme-banner-backgroundImagePosition: cover;--newCommunityTheme-banner-communityNameFormat: slashtag;--newCommunityTheme-banner-height: 128;--newCommunityTheme-banner-iconColor: #94E044;--newCommunityTheme-banner-iconDimensions-borderRadius: 32;--newCommunityTheme-banner-iconDimensions-customSize: 52;--newCommunityTheme-banner-iconDimensions-padding: 10;--newCommunityTheme-banner-iconDimensions-size: 36;--newCommunityTheme-banner-iconImage: url("https://styles.redditmedia.com/t5_2reen/styles/communityIcon_vfxkxkkdwan71.jpg?format=pjpg&s=33b70ce76f77eb00dce3a326204df5a5bb3c8a9c");--newCommunityTheme-banner-lineHeight: 60;--newCommunityTheme-banner-positionedImage: initial;--newCommunityTheme-banner-positionedImageAlignment: left;--newCommunityTheme-banner-positionedImageHeight: 112;--newCommunityTheme-banner-secondaryBannerPositionedImage: initial;--newCommunityTheme-body: #FFFFFF;--newCommunityTheme-bodyAlpha50: rgba(255,255,255,0.5);--newCommunityTheme-bodyAlpha70: rgba(255,255,255,0.7);--newCommunityTheme-bodyAlpha80: rgba(255,255,255,0.8);--newCommunityTheme-bodyFade: #FFFFFF00;--newCommunityTheme-bodyShaded80: #ccc;--newCommunityTheme-bodyText: #1c1c1c;--newCommunityTheme-bodyTextAlpha03: rgba(28,28,28,0.03);--newCommunityTheme-bodyTextAlpha20: rgba(28,28,28,0.2);--newCommunityTheme-bodyTextShaded20: #050505;--newCommunityTheme-bodyTextTinted20: #d1d1d1;--newCommunityTheme-bodyTinted50: #fff;--newCommunityTheme-bodyTinted80: #fff;--newCommunityTheme-button: #73AD34;--newCommunityTheme-buttonAlpha05: rgba(115,173,52,0.05);--newCommunityTheme-buttonAlpha10: rgba(115,173,52,0.1);--newCommunityTheme-buttonAlpha20: rgba(115,173,52,0.2);--newCommunityTheme-buttonAlpha40: rgba(115,173,52,0.4);--newCommunityTheme-buttonAlpha50: rgba(115,173,52,0.5);--newCommunityTheme-buttonAlpha80: rgba(115,173,52,0.8);--newCommunityTheme-buttonShaded80: #5c8a29;--newCommunityTheme-buttonTinted20: #e3eed6;--newCommunityTheme-buttonTinted50: #b9d699;--newCommunityTheme-buttonTinted80: #8fbd5c;--newCommunityTheme-canvas: #DAE0E6;--newCommunityTheme-canvasImgPosition: cover;--newCommunityTheme-canvasImgUrl: initial;--newCommunityTheme-checkbox: #000000;--newCommunityTheme-errorText: #FF0000;--newCommunityTheme-field: #F6F7F8;--newCommunityTheme-fieldFade: #F6F7F800;--newCommunityTheme-flair: #EDEFF1;--newCommunityTheme-highlight: #f4fbec;--newCommunityTheme-inactive: #EDEFF1;--newCommunityTheme-invertFilter: invert(0);--newCommunityTheme-lightText: #FFFFFF;--newCommunityTheme-lightTextAlpha75: rgba(255,255,255,0.75);--newCommunityTheme-line: #EDEFF1;--newCommunityTheme-lineShaded80: #bdbfc0;--newCommunityTheme-lineShaded90: #d5d7d8;--newCommunityTheme-lineShadedNinety: #d5d7d8;--newCommunityTheme-linkText: #73AD34;--newCommunityTheme-linkTextAlpha80: rgba(115,173,52,0.5);--newCommunityTheme-linkTextShaded80: #5c8a29;--newCommunityTheme-linkTextTinted80: #8fbd5c;--newCommunityTheme-linkTextWithBody: #3f9ade;--newCommunityTheme-menu: #FFFFFF;--newCommunityTheme-menuActiveText: #0079D3;--newCommunityTheme-menuButtonBackground-active: rgba(0,0,0,0.08);--newCommunityTheme-menuButtonBackground-focus: rgba(0,0,0,0.12);--newCommunityTheme-menuButtonBackground-hover: rgba(0,0,0,0.04);--newCommunityTheme-menuInactiveText: #0079D3;--newCommunityTheme-metaText: #7c7c7c;--newCommunityTheme-monospaceColor: #FF006D;--newCommunityTheme-navBar-activeLink: #73AD34;--newCommunityTheme-navBar-activeSubmenuCaret: #94E044;--newCommunityTheme-navBar-activeSubmenuLink: #94E044;--newCommunityTheme-navBar-backgroundColor: #edfae0;--newCommunityTheme-navBar-backgroundImage: initial;--newCommunityTheme-navBar-hoverLink: #73AD34;--newCommunityTheme-navBar-inactiveLink: #94E044;--newCommunityTheme-navBar-inactiveSubmenuCaret: #9be250;--newCommunityTheme-navBar-inactiveSubmenuLink: #9be250;--newCommunityTheme-navBar-submenuBackgroundColor: #edfae0;--newCommunityTheme-navIcon: #1A1A1B;--newCommunityTheme-navIconFaded10: rgba(26,26,27,0.1);--newCommunityTheme-nsfwBlocking-bgcolor: #edeff1;--newCommunityTheme-nsfwBlocking-color: #030303;--newCommunityTheme-nsfwBlocking-contentTitleBgColor: #f6f7f8;;--newCommunityTheme-nsfwBlocking-mainCtaBgColor: #fff;--newCommunityTheme-orangeRed: #FF4500;--newCommunityTheme-pageHeader: #0079D3;--newCommunityTheme-placeholder: #d6d6d6;--newCommunityTheme-placeholderImage: initial;--newCommunityTheme-placeholderImagePosition: cover;--newCommunityTheme-post: #FFFFFF;--newCommunityTheme-postError: #ffe5e5;--newCommunityTheme-postFlairText: #1A1A1B;--newCommunityTheme-postIcon: #898989;--newCommunityTheme-postLine: #ccc;--newCommunityTheme-postLineShaded80: #a3a3a3;--newCommunityTheme-postLineShaded90: #b7b7b7;--newCommunityTheme-postTinted20: #fff;--newCommunityTheme-postTransparent20: rgba(255,255,255,0.8);--newCommunityTheme-primaryButtonShadedEighty: #76b336;--newCommunityTheme-primaryButtonTintedEighty: #a9e669;--newCommunityTheme-primaryButtonTintedFifty: #c9efa1;--newCommunityTheme-primaryButtonTintedSixty: #beec8e;--newCommunityTheme-report: #fff7e5;--newCommunityTheme-textTransparentizedEighty: rgba(26,26,27,0.2);--newCommunityTheme-titleText: #222222;--newCommunityTheme-voteIcons-downvoteActive: initial;--newCommunityTheme-voteIcons-downvoteInactive: initial;--newCommunityTheme-voteIcons-upvoteActive: initial;--newCommunityTheme-voteIcons-upvoteInactive: initial;--newCommunityTheme-voteText-base: #898989;--newCommunityTheme-voteText-downvote: #7193FF;--newCommunityTheme-voteText-downvoteShaded80: #5a75cc;--newCommunityTheme-voteText-downvoteTinted80: #8da8ff;--newCommunityTheme-voteText-upvote: #FF4500;--newCommunityTheme-voteText-upvoteShaded80: #cc3700;--newCommunityTheme-voteText-upvoteTinted80: #ff6a32;--newCommunityTheme-widgetColors-lineColor: rgba(26,26,27,0.07);--newCommunityTheme-widgetColors-sidebarWidgetBackgroundColor: #FFFFFF;--newCommunityTheme-widgetColors-sidebarWidgetBorderColor: #ccc;--newCommunityTheme-widgetColors-sidebarWidgetHeaderColor: #94E044;--newCommunityTheme-widgetColors-sidebarWidgetHeaderColorAlpha60: rgba(148,224,68,0.6);--newCommunityTheme-widgetColors-sidebarWidgetTextColor: #1A1A1B;--newCommunityTheme-widgetColors-sidebarWidgetTextColorShaded80: #141415;--newCommunityTheme-widgetColors-sidebarWidgetTitleColor: #1A1A1B;--newRedditTheme-actionIcon: #878A8C;--newRedditTheme-actionIconAlpha20: rgba(135,138,140,0.2);--newRedditTheme-actionIconAlpha50: rgba(135,138,140,0.5);--newRedditTheme-actionIconShaded80: #6c6e70;--newRedditTheme-actionIconTinted80: #9fa1a3;--newRedditTheme-active: #24A0ED;--newRedditTheme-activeAlpha10: rgba(36,160,237,0.1);--newRedditTheme-activeAlpha20: rgba(36,160,237,0.2);--newRedditTheme-activeAlpha50: rgba(36,160,237,0.5);--newRedditTheme-activeLight60: #42adf0;--newRedditTheme-activeShaded80: #1c80bd;--newRedditTheme-activeShaded90: #2090d5;--newRedditTheme-activeTinted05: #f4fafe;--newRedditTheme-banner-backgroundColor: #24A0ED;--newRedditTheme-banner-backgroundImage: initial;--newRedditTheme-banner-backgroundImagePosition: cover;--newRedditTheme-banner-communityNameFormat: slashtag;--newRedditTheme-banner-height: 64;--newRedditTheme-banner-iconColor: #24A0ED;--newRedditTheme-banner-iconDimensions-borderRadius: 24;--newRedditTheme-banner-iconDimensions-customSize: 32;--newRedditTheme-banner-iconDimensions-padding: 6;--newRedditTheme-banner-iconDimensions-size: 24;--newRedditTheme-banner-iconImage: initial;--newRedditTheme-banner-lineHeight: 38;--newRedditTheme-banner-positionedImage: initial;--newRedditTheme-banner-positionedImageAlignment: cover;--newRedditTheme-banner-positionedImageHeight: 48;--newRedditTheme-banner-secondaryBannerPositionedImage: initial;--newRedditTheme-body: #FFFFFF;--newRedditTheme-bodyAlpha50: rgba(255,255,255,0.5);--newRedditTheme-bodyAlpha70: rgba(255,255,255,0.7);--newRedditTheme-bodyAlpha80: rgba(255,255,255,0.8);--newRedditTheme-bodyFade: #FFFFFF00;--newRedditTheme-bodyShaded80: #ccc;--newRedditTheme-bodyText: #1c1c1c;--newRedditTheme-bodyTextAlpha03: rgba(28,28,28,0.03);--newRedditTheme-bodyTextAlpha20: rgba(28,28,28,0.2);--newRedditTheme-bodyTextShaded20: #050505;--newRedditTheme-bodyTextTinted20: #d1d1d1;--newRedditTheme-bodyTinted50: #fff;--newRedditTheme-bodyTinted80: #fff;--newRedditTheme-button: #0079D3;--newRedditTheme-buttonAlpha05: rgba(0,121,211,0.05);--newRedditTheme-buttonAlpha10: rgba(0,121,211,0.1);--newRedditTheme-buttonAlpha20: rgba(0,121,211,0.2);--newRedditTheme-buttonAlpha40: rgba(0,121,211,0.4);--newRedditTheme-buttonAlpha50: rgba(0,121,211,0.5);--newRedditTheme-buttonAlpha80: rgba(0,121,211,0.8);--newRedditTheme-buttonShaded80: #0060a8;--newRedditTheme-buttonTinted20: #cce4f6;--newRedditTheme-buttonTinted50: #7fbce9;--newRedditTheme-buttonTinted80: #3293db;--newRedditTheme-canvas: #DAE0E6;--newRedditTheme-checkbox: #000000;--newRedditTheme-errorText: #FF0000;--newRedditTheme-field: #F6F7F8;--newRedditTheme-fieldFade: #F6F7F800;--newRedditTheme-flair: #EDEFF1;--newRedditTheme-highlight: #e9f5fd;--newRedditTheme-inactive: #EDEFF1;--newRedditTheme-invertFilter: invert(0);--newRedditTheme-lightText: #FFFFFF;--newRedditTheme-lightTextAlpha75: rgba(255,255,255,0.75);--newRedditTheme-line: #EDEFF1;--newRedditTheme-lineShaded80: #bdbfc0;--newRedditTheme-lineShaded90: #d5d7d8;--newRedditTheme-linkText: #0079D3;--newRedditTheme-linkTextAlpha80: rgba(0,121,211,0.5);--newRedditTheme-linkTextShaded80: #0060a8;--newRedditTheme-linkTextTinted80: #3293db;--newRedditTheme-linkTextWithBody: #3f9ade;--newRedditTheme-menu: #FFFFFF;--newRedditTheme-menuActiveText: #0079D3;--newRedditTheme-menuButtonBackground-active: rgba(0,0,0,0.08);--newRedditTheme-menuButtonBackground-focus: rgba(0,0,0,0.12);--newRedditTheme-menuButtonBackground-hover: rgba(0,0,0,0.04);--newRedditTheme-menuInactiveText: #0079D3;--newRedditTheme-metaText: #7c7c7c;--newRedditTheme-metaTextAlpha50: rgba(120,124,126,0.5);--newRedditTheme-metaTextShaded80: #606364;--newRedditTheme-monospaceColor: #FF006D;--newRedditTheme-navBar-activeLink: #E9F5FD;--newRedditTheme-navBar-activeSubmenuCaret: #24A0ED;--newRedditTheme-navBar-activeSubmenuLink: #24A0ED;--newRedditTheme-navBar-backgroundColor: #24A0ED;--newRedditTheme-navBar-backgroundImage: initial;--newRedditTheme-navBar-hoverLink: #E9F5FD;--newRedditTheme-navBar-inactiveLink: #EDEFF1;--newRedditTheme-navBar-inactiveSubmenuCaret: #42adf0;--newRedditTheme-navBar-inactiveSubmenuLink: #42adf0;--newRedditTheme-navBar-submenuBackgroundColor: #def1fc;--newRedditTheme-navIcon: #1A1A1B;--newRedditTheme-navIconFaded10: rgba(26,26,27,0.1);--newRedditTheme-nsfw: #ff585b;--newRedditTheme-nsfwBlocking-bgcolor: #edeff1;--newRedditTheme-nsfwBlocking-color: #030303;--newRedditTheme-nsfwBlocking-contentTitleBgColor: #f6f7f8;;--newRedditTheme-nsfwBlocking-mainCtaBgColor: #fff;--newRedditTheme-orangeRed: #FF4500;--newRedditTheme-pageHeader: #0079D3;--newRedditTheme-placeholder: #d6d6d6;--newRedditTheme-post: #FFFFFF;--newRedditTheme-postError: #ffe5e5;--newRedditTheme-postFlairText: #1A1A1B;--newRedditTheme-postIcon: #898989;--newRedditTheme-postLine: #ccc;--newRedditTheme-postLineShaded80: #a3a3a3;--newRedditTheme-postLineShaded90: #b7b7b7;--newRedditTheme-postTinted20: #fff;--newRedditTheme-postTransparent20: rgba(255,255,255,0.8);--newRedditTheme-quarantine: #ffb000;--newRedditTheme-report: #fff7e5;--newRedditTheme-search-syntaxHighlightBackgroundColor: #E9F5FD;--newRedditTheme-search-syntaxHighlightColor: #1A1A1A;--newRedditTheme-titleText: #1A1A1B;--newRedditTheme-upsell-appleIcon: #000000;--newRedditTheme-upsell-ssoButtonBorderColor: #D3D6DA;--newRedditTheme-upsell-ssoButtonTextColor: #3D4043;--newRedditTheme-voteIcons-downvoteActive: initial;--newRedditTheme-voteIcons-downvoteInactive: initial;--newRedditTheme-voteIcons-upvoteActive: initial;--newRedditTheme-voteIcons-upvoteInactive: initial;--newRedditTheme-voteText-base: #898989;--newRedditTheme-voteText-downvote: #7193FF;--newRedditTheme-voteText-downvoteShaded80: #5a75cc;--newRedditTheme-voteText-downvoteTinted80: #8da8ff;--newRedditTheme-voteText-upvote: #FF4500;--newRedditTheme-voteText-upvoteShaded80: #cc3700;--newRedditTheme-voteText-upvoteTinted80: #ff6a32;--newRedditTheme-widgetColors-lineColor: rgba(26,26,27,0.07);--newRedditTheme-widgetColors-sidebarWidgetBackgroundColor: #FFFFFF;--newRedditTheme-widgetColors-sidebarWidgetBorderColor: #ccc;--newRedditTheme-widgetColors-sidebarWidgetHeaderColor: #FFFFFF;--newRedditTheme-widgetColors-sidebarWidgetHeaderColorAlpha60: rgba(255,255,255,0.6);--newRedditTheme-widgetColors-sidebarWidgetTextColor: #1A1A1B;--newRedditTheme-widgetColors-sidebarWidgetTextColorShaded80: #141415;--newRedditTheme-widgetColors-sidebarWidgetTitleColor: #1A1A1B;--subredditContext-isCommentsPage: initial;--subredditContext-isOverlay: initial; }</style><div class="subredditvars-r-androidapps"></div></div></div></div>
        <script>
          __perfMark('ads_dot_js_fetch_start');
        </script><script src="https://www.redditstatic.com/desktop2x/js/xads.js"></script><div id="a2ba06a4-a2ec-4182-b295-c15ffe5f1181" style="display: none;"></div><script>
          __perfMark('redux_json_start');
        </script><script>
          __perfMark('js_deps_fetch_start');
        </script><script id="whitespace__LOADABLE_REQUIRED_CHUNKS__" type="application/json">["CollectionCommentsPage~CommentsPage~CountryPage~FramedGild~GildModal~GovernanceReleaseNotesModal~Hap~a5d6a3b8","CollectionCommentsPage~CommentsPage~CountryPage~FramedGild~GildModal~GovernanceReleaseNotesModal~Hap~cb450973","CollectionCommentsPage~CommentsPage~CountryPage~Frontpage~GovernanceReleaseNotesModal~ModListing~Mod~e3d63e32","CollectionCommentsPage~CommentsPage~EconTopAwardersModal~ModQueuePages~ModerationPages~PostCreation~~bca2b657","CollectionCommentsPage~CommentsPage~GovernanceReleaseNotesModal~ModerationPages~PostCreation~Profile~9a5d9fab","CollectionCommentsPage~ProfileComments~ProfileOverview~ProfilePrivate~SearchResults","CollectionCommentsPage~SearchResults","SearchResults"]</script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/runtime~Reddit.06fbd78943f321491899.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/vendors~CommentsPage~ModerationPages~Reddit~reddit-components-ClassicPost~reddit-components-CompactP~d737df3e.31f8d07ab88edabff736.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/vendors~CommentsPage~Governance~ModListing~ModerationPages~Reddit~Subreddit.f468f4fbfe44aa5cfabf.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/vendors~Chat~Governance~Reddit.6921f706c26009a1fbb3.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/vendors~Reddit.fc8d4c49cc97b168c869.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/CommentsPage~Governance~Reddit~ReportFlow~Subreddit~reddit-components-BlankPost~reddit-components-Cl~5351df81.9f55115c90a0961eb901.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/Governance~Reddit~Subreddit~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compo~bd4baca2.f2e1cfa53fed5821c00e.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/Reddit~StandalonePostPage~reddit-components-ClassicPost~reddit-components-CompactPost~reddit-compone~9b425435.1be10e42f8dcef625f90.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/Reddit~RichTextEditor~reddit-components-MediumPost~reddit-components-NotificationUnit-Button~removal~87f825ba.1f6f4cdd3ba5ffd0749d.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/Governance~ModListing~Reddit~ReportFlow.92dc6832eb65b153b9f8.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/Chat~Governance~Reddit.daa21bfdc4bf6b1b0d2d.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/Governance~Reddit~SubredditForkingCTA.b7769f2f45dab828f630.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/Governance~ModListing~Reddit.20ff93da9585bdd58793.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/ModListing~Reddit~StandalonePostPage.bd37319a4f78703e6421.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/Governance~Reddit.ed393a9e80733c2bca28.js"></script><script async="" data-chunk="Reddit" src="https://www.redditstatic.com/desktop2x/Reddit.e0ee6b3e4f217f451152.js"></script><script async="" data-chunk="SearchResults" src="https://www.redditstatic.com/desktop2x/CollectionCommentsPage~CommentsPage~CountryPage~FramedGild~GildModal~GovernanceReleaseNotesModal~Hap~a5d6a3b8.958a4be1d4d5a2796018.js"></script><script async="" data-chunk="SearchResults" src="https://www.redditstatic.com/desktop2x/CollectionCommentsPage~CommentsPage~CountryPage~FramedGild~GildModal~GovernanceReleaseNotesModal~Hap~cb450973.f52b6cfcbc42ab04e7e9.js"></script><script async="" data-chunk="SearchResults" src="https://www.redditstatic.com/desktop2x/CollectionCommentsPage~CommentsPage~CountryPage~Frontpage~GovernanceReleaseNotesModal~ModListing~Mod~e3d63e32.ced754611777c94d5ae0.js"></script><script async="" data-chunk="SearchResults" src="https://www.redditstatic.com/desktop2x/CollectionCommentsPage~CommentsPage~EconTopAwardersModal~ModQueuePages~ModerationPages~PostCreation~~bca2b657.b2816f459a4c5f8ca74b.js"></script><script async="" data-chunk="SearchResults" src="https://www.redditstatic.com/desktop2x/CollectionCommentsPage~CommentsPage~GovernanceReleaseNotesModal~ModerationPages~PostCreation~Profile~9a5d9fab.2a227e2fccf72c7374f8.js"></script><script async="" data-chunk="SearchResults" src="https://www.redditstatic.com/desktop2x/CollectionCommentsPage~ProfileComments~ProfileOverview~ProfilePrivate~SearchResults.930cae2789eb6ed7a7b9.js"></script><script async="" data-chunk="SearchResults" src="https://www.redditstatic.com/desktop2x/CollectionCommentsPage~SearchResults.4d356568ad594a8d2d44.js"></script><script async="" data-chunk="SearchResults" src="https://www.redditstatic.com/desktop2x/SearchResults.67903249620c41190639.js"></script>
        <div id="acceptabletest" class="promotedlink" style="width: 1px; height: 1px; position: absolute; left: -1e+06px; top: 0px; display: block;">Advertisement</div>
        <div id="adblocktest" class="AdHeader AdUnit adsense-ads HeaderAd SidebarAd VerticalAd _has-ads ad--content ad-adsense ad-banner adsense-ads googads ad-banner-content ad-BANNER googleAd googlead hasads leftAd native-ad ADBAR ad-medium post-ad promoad rectad sidebar-ad small-ad sponsorAd sponsorPost" style="width: 1px; height: 1px; position: absolute; left: -1000%;"></div>
        <script id="datadome-bot-detection">!function(a,b,c,d,e,f){a.ddjskey=e;a.ddoptions=f||null;var m=b.createElement(c),n=b.getElementsByTagName(c)[0];m.async=1,m.src=d,n.parentNode.insertBefore(m,n)}(window,document,"script","https://www.redditstatic.com/js/tags-slim.js","288922D4BE1987530B4E5D4A17952C", { ajaxListenerPath: ["reddit.com/api", "gql.reddit.com", "gateway.reddit.com/desktopapi"] });</script>
      
    
  <div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><div class=""></div><iframe id="gtm-99d55450-3600-42b8-837e-c5d29139cb16" name="{&quot;referrer&quot;:&quot;&quot;,&quot;href&quot;:&quot;https://www.reddit.com/r/androidapps/search/?q=photo&amp;sort=new&quot;,&quot;hostname&quot;:&quot;www.reddit.com&quot;,&quot;origin&quot;:&quot;https://www.reddit.com&quot;,&quot;pathname&quot;:&quot;/r/androidapps/search/&quot;,&quot;search&quot;:&quot;q=photo&amp;sort=new&quot;,&quot;hash&quot;:&quot;=undefined&quot;,&quot;user&quot;:&quot;000000000cu8q90h8v&quot;}" src="https://www.redditmedia.com/gtm/jail?id=GTM-5XVNS82" style="display: none;"></iframe></body></html>