(setq inhibit-startup-screen t)

;; show cursor position within line
(column-number-mode 1)


(when (version<= "26.0.50" emacs-version )
  (global-display-line-numbers-mode))

;; highlight current line
(global-hl-line-mode 1)


(when (member "Hack" (font-family-list)) (set-frame-font "Menlo-14" t t))




(if (display-graphic-p)
    (progn
      (setq initial-frame-alist
            '(
              (tool-bar-lines . 0)
              (width . 106) ; chars
              (height . 60) ; lines
              (left . 50)
              (top . 50)))
      (setq default-frame-alist
            '(
              (tool-bar-lines . 0)
              (width . 106)
              (height . 60)
              (left . 50)
              (top . 50))))
  (progn
    (setq initial-frame-alist '( (tool-bar-lines . 0)))
    (setq default-frame-alist '( (tool-bar-lines . 0)))))
