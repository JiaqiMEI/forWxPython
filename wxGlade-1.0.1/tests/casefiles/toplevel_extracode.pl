#!/usr/bin/perl -w -- 
#
# generated by wxGlade
#
# To get wxPerl visit http://www.wxperl.it
#

use Wx qw[:allclasses];
use strict;

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# frame extra code
# dialog extra code
# end wxGlade

package MyFrame;

use Wx qw[:everything];
use base qw(Wx::Frame);
use strict;

sub new {
    my( $self, $parent, $id, $title, $pos, $size, $style, $name ) = @_;
    $parent = undef              unless defined $parent;
    $id     = -1                 unless defined $id;
    $title  = ""                 unless defined $title;
    $pos    = wxDefaultPosition  unless defined $pos;
    $size   = wxDefaultSize      unless defined $size;
    $name   = ""                 unless defined $name;

    # begin wxGlade: MyFrame::new
    # frame extra code before
    $style = wxDEFAULT_FRAME_STYLE
        unless defined $style;

    $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
    $self->SetSize(Wx::Size->new(400, 300));
    $self->SetTitle("frame");
    
    $self->{sizer_1} = Wx::BoxSizer->new(wxVERTICAL);
    
    $self->{sizer_1}->Add(0, 0, 0, 0, 0);
    
    $self->SetSizer($self->{sizer_1});
    
    $self->Layout();
    # frame extra code after
    Wx::Event::EVT_CLOSE($self, $self->GetId, $self->can('on_close_frame'));
    Wx::Event::EVT_MENU_CLOSE($self, $self->GetId, $self->can('on_menu_close_frame'));

    # end wxGlade
    return $self;

}


sub on_close_frame {
    my ($self, $event) = @_;
    # wxGlade: MyFrame::on_close_frame <event_handler>
    warn "Event handler (on_close_frame) not implemented";
    $event->Skip;
    # end wxGlade
}


sub on_menu_close_frame {
    my ($self, $event) = @_;
    # wxGlade: MyFrame::on_menu_close_frame <event_handler>
    warn "Event handler (on_menu_close_frame) not implemented";
    $event->Skip;
    # end wxGlade
}


# end of class MyFrame

1;

package MyDialog;

use Wx qw[:everything];
use base qw(Wx::Dialog);
use strict;

sub new {
    my( $self, $parent, $id, $title, $pos, $size, $style, $name ) = @_;
    $parent = undef              unless defined $parent;
    $id     = -1                 unless defined $id;
    $title  = ""                 unless defined $title;
    $pos    = wxDefaultPosition  unless defined $pos;
    $size   = wxDefaultSize      unless defined $size;
    $name   = ""                 unless defined $name;

    # begin wxGlade: MyDialog::new
    # dialog extra code before
    $style = wxDEFAULT_DIALOG_STYLE
        unless defined $style;

    $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
    $self->SetTitle("dialog");
    
    $self->{sizer_1} = Wx::BoxSizer->new(wxVERTICAL);
    
    $self->{sizer_1}->Add(0, 0, 0, 0, 0);
    
    $self->SetSizer($self->{sizer_1});
    $self->{sizer_1}->Fit($self);
    
    $self->Layout();
    # dialog extra code after
    Wx::Event::EVT_CLOSE($self, $self->GetId, $self->can('on_close_dialog'));

    # end wxGlade
    return $self;

}


sub on_close_dialog {
    my ($self, $event) = @_;
    # wxGlade: MyDialog::on_close_dialog <event_handler>
    warn "Event handler (on_close_dialog) not implemented";
    $event->Skip;
    # end wxGlade
}


# end of class MyDialog

1;

package MyMenuBar;

use Wx qw[:everything];
use base qw(Wx::MenuBar);
use strict;

sub new {
    my( $self,  ) = @_;
    # begin wxGlade: MyMenuBar::new
    # menubar extracode before
    $self = $self->SUPER::new( @_[1 .. $#_] );
    my $wxglade_tmp_menu;
    # menubar extracode after
    # end wxGlade
    return $self;

}


# end of class MyMenuBar

1;

package wxToolBar;

use Wx qw[:everything];
use base qw(Wx::ToolBar);
use strict;

sub new {
    my( $self,  ) = @_;
    # begin wxGlade: wxToolBar::new
    # toolbar extracode before
    $self = $self->SUPER::new( @_[1 .. $#_] );
    $self->Realize();
    # toolbar extracode after
    # end wxGlade
    return $self;

}


# end of class wxToolBar

1;

package MyDialog1;

use Wx qw[:everything];
use base qw(Wx::Panel);
use strict;

sub new {
    my( $self, $parent, $id, $pos, $size, $style, $name ) = @_;
    $parent = undef              unless defined $parent;
    $id     = -1                 unless defined $id;
    $pos    = wxDefaultPosition  unless defined $pos;
    $size   = wxDefaultSize      unless defined $size;
    $name   = ""                 unless defined $name;

    # begin wxGlade: MyDialog1::new
    # panel extracode before
    $style = wxTAB_TRAVERSAL
        unless defined $style;

    $self = $self->SUPER::new( $parent, $id, $pos, $size, $style, $name );
    
    $self->{sizer_1} = Wx::BoxSizer->new(wxVERTICAL);
    
    $self->{sizer_1}->Add(0, 0, 0, 0, 0);
    
    $self->SetSizer($self->{sizer_1});
    $self->{sizer_1}->Fit($self);
    
    $self->Layout();
    # panel extracode after
    # end wxGlade
    return $self;

}


# end of class MyDialog1

1;

package MyApp;

use base qw(Wx::App);
use strict;

sub OnInit {
    my( $self ) = shift;

    Wx::InitAllImageHandlers();

    my $frame = MyFrame->new();

    $self->SetTopWindow($frame);
    $frame->Show(1);

    return 1;
}
# end of class MyApp

package main;

unless(caller){
    my $app = MyApp->new();
    $app->MainLoop();
}
