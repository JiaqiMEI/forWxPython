;;; generated by wxGlade
;;;

(asdf:operate 'asdf:load-op 'wxcl)
(use-package "FFI")
(ffi:default-foreign-language :stdc)


;;; begin wxGlade: dependencies
(use-package :wxCL)
(use-package :wxColour)
(use-package :wxEvent)
(use-package :wxEvtHandler)
(use-package :wxFont)
(use-package :wxFrame)
(use-package :wxSizer)
(use-package :wxStaticText)
(use-package :wxWindow)
(use-package :wx_main)
(use-package :wx_wrapper)
;;; end wxGlade

;;; begin wxGlade: extracode
;;; end wxGlade


(defclass MyFrame()
        ((top-window :initform nil :accessor slot-top-window)
        (sizer-1 :initform nil :accessor slot-sizer-1)
        (label-1 :initform nil :accessor slot-label-1)))

(defun make-MyFrame ()
        (let ((obj (make-instance 'MyFrame)))
          (init obj)
          (set-properties obj)
          (do-layout obj)
          obj))

(defmethod init ((obj MyFrame))
"Method creates the objects contained in the class."
        ;;; begin wxGlade: MyFrame.__init__
        (setf (slot-top-window obj) (wxFrame_create nil wxID_ANY "" -1 -1 -1 -1 wxDEFAULT_FRAME_STYLE))
        (wxFrame_SetTitle (slot-top-window obj) (_"MyFrame"))
        
        (setf (slot-sizer-1 obj) (wxBoxSizer_Create wxVERTICAL))
        
        (setf (slot-label-1 obj) (wxStaticText_Create (slot-top-window obj) wxID_ANY (_"Extraproperty example") -1 -1 -1 -1 0))
        (wxWindow_SetFont (slot-label-1 obj) (wxFont_Create 40 wxDEFAULT wxNORMAL wxNORMAL 0 "" wxFONTENCODING_DEFAULT))
        (wxStaticText_SetFoobar (slot-(slot-label-1 obj) obj) 1)
        (wxSizer_AddWindow (slot-sizer-1 obj) (slot-label-1 obj) 1 wxALL 5 nil)
        
        (wxWindow_SetSizer (slot-top-window obj) (slot-sizer-1 obj))
        (wxSizer_Fit (slot-sizer-1 obj) (slot-top-window obj))
        
        (wxFrame_layout (slot-MyFrame self))
        ;;; end wxGlade
        )

;;; end of class MyFrame


