from wagtail import blocks

class LinkBlock(blocks.StructBlock):
    link = blocks.RichTextBlock(features=['link'], required=True)
    visible = blocks.BooleanBlock(required=False, default=True)

    class Meta:
        template="streams/link_block.html"
        icon = 'link'
        label = 'Link'

class SidebarBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250,required=True)
    link = blocks.RichTextBlock(features=['link'], required=True)
    visible = blocks.BooleanBlock(required=False, default=True)

    class Meta:
        template = "streams/sidebar_block.html"
        icon = 'edit'
        label = 'Content'


